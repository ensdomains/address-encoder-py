from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"
SRC_DIR = REPO_ROOT / "src"
COINS_DIR = SRC_DIR / "address_encoder" / "coins"
CODERS_PATH = SRC_DIR / "address_encoder" / "coders.py"
COIN_MAPS_PATH = SRC_DIR / "address_encoder" / "consts" / "coin_maps.py"
DOCS_PATH = REPO_ROOT / "docs" / "supported-cryptocurrencies.md"
TESTS_DIR = REPO_ROOT / "tests"
VENV_PYTHON = REPO_ROOT / ".venv" / "bin" / "python"

SLIP44_MSB = 0x80000000


def resolve_python() -> str:
    if VENV_PYTHON.is_file():
        return str(VENV_PYTHON)
    return sys.executable


def python_env() -> dict[str, str]:
    import os

    env = os.environ.copy()
    env["PYTHONPATH"] = str(SRC_DIR)
    return env


def evm_chain_id_to_coin_type(chain_id: int) -> int:
    if chain_id >= SLIP44_MSB:
        raise ValueError("Invalid chainId")
    return (SLIP44_MSB | chain_id) & 0xFFFFFFFF


def coin_type_to_evm_chain_id(coin_type: int) -> int:
    if (coin_type & SLIP44_MSB) == 0:
        raise ValueError("Coin type is not an EVM chain")
    return ((SLIP44_MSB - 1) & coin_type) & 0xFFFFFFFF


def capitalise_coin(name: str) -> str:
    return name[0].upper() + name[1:]


def normalise_coin_name(raw_name: str) -> tuple[str, bool]:
    coin_name = raw_name.lower()
    is_legacy = coin_name.endswith("legacy")
    if is_legacy:
        coin_name = coin_name.replace("legacy", "Legacy")
    return coin_name, is_legacy


def display_name(coin_name: str, is_legacy: bool) -> str:
    if is_legacy:
        return coin_name.upper().replace("LEGACY", "_LEGACY")
    return coin_name.upper()


def parse_coin_maps(content: str) -> tuple[dict[int, tuple[str, str]], dict[int, tuple[str, str]]]:
    evm: dict[int, tuple[str, str]] = {}
    non_evm: dict[int, tuple[str, str]] = {}
    current: str | None = None
    for line in content.splitlines():
        if line.startswith("EVM_COIN_TYPE_TO_NAME"):
            current = "evm"
        elif line.startswith("NON_EVM_COIN_TYPE_TO_NAME"):
            current = "non_evm"
        match = re.search(r'^\s*(\d+):\s*\("([^"]+)",\s*"([^"]+)"\)', line)
        if match and current:
            entry = (match.group(2), match.group(3))
            target = evm if current == "evm" else non_evm
            target[int(match.group(1))] = entry
    return evm, non_evm


def read_coin_maps() -> tuple[dict[int, tuple[str, str]], dict[int, tuple[str, str]]]:
    return parse_coin_maps(COIN_MAPS_PATH.read_text())


def render_coin_maps(
    evm: dict[int, tuple[str, str]],
    non_evm: dict[int, tuple[str, str]],
) -> str:
    def render_map(name: str, mapping: dict[int, tuple[str, str]]) -> str:
        lines = [f"{name} = {{"]
        for coin_type in sorted(mapping):
            symbol, display = mapping[coin_type]
            lines.append(f'    {coin_type}: ("{symbol}", "{display}"),')
        lines.append("}")
        return "\n".join(lines)

    return (
        "from __future__ import annotations\n\n"
        + render_map("EVM_COIN_TYPE_TO_NAME", evm)
        + "\n\n"
        + render_map("NON_EVM_COIN_TYPE_TO_NAME", non_evm)
        + "\n\n"
        + "COIN_TYPE_TO_NAME = {**NON_EVM_COIN_TYPE_TO_NAME, **EVM_COIN_TYPE_TO_NAME}\n\n"
        + "EVM_COIN_NAME_TO_TYPE = {symbol: int(coin_type) for coin_type, (symbol, _) in EVM_COIN_TYPE_TO_NAME.items()}\n"
        + "NON_EVM_COIN_NAME_TO_TYPE = {symbol: int(coin_type) for coin_type, (symbol, _) in NON_EVM_COIN_TYPE_TO_NAME.items()}\n"
        + "COIN_NAME_TO_TYPE = {**NON_EVM_COIN_NAME_TO_TYPE, **EVM_COIN_NAME_TO_TYPE}\n"
    )


def write_coin_maps(
    evm: dict[int, tuple[str, str]],
    non_evm: dict[int, tuple[str, str]],
) -> None:
    COIN_MAPS_PATH.write_text(render_coin_maps(evm, non_evm))


def list_coin_modules() -> list[str]:
    return sorted(
        path.stem
        for path in COINS_DIR.glob("*.py")
        if path.stem not in {"__init__", "_registry"}
    )


def render_registry(coin_names: list[str]) -> str:
    imports = "\n".join(f"from address_encoder.coins.{name} import {name}" for name in coin_names)
    entries = ",\n    ".join(f'"{name}": {name}' for name in coin_names)
    return (
        "from __future__ import annotations\n\n"
        "from address_encoder.types import CoinCoder\n\n"
        f"{imports}\n\n"
        "COINS: dict[str, CoinCoder] = {\n"
        f"    {entries}\n"
        "}\n"
    )


def render_coders(coin_names: list[str]) -> str:
    imports = "\n".join(
        f"from address_encoder.coins.{name} import decode_{name}_address, encode_{name}_address"
        for name in coin_names
    )
    exports = [
        export
        for name in coin_names
        for export in (f"decode_{name}_address", f"encode_{name}_address")
    ]
    export_lines = ",\n    ".join(f'"{export}"' for export in exports)
    return (
        "from __future__ import annotations\n\n"
        f"{imports}\n\n"
        f"__all__ = [\n    {export_lines},\n]\n"
    )


def regenerate_registry() -> None:
    coin_names = list_coin_modules()
    registry = render_registry(coin_names)
    (COINS_DIR / "__init__.py").write_text(registry)
    (COINS_DIR / "_registry.py").write_text(registry)
    CODERS_PATH.write_text(render_coders(coin_names))
    print(f"Updated registry for {len(coin_names)} coin modules")


def markdown_table(headers: list[str], rows: list[list[object]]) -> str:
    header = "| " + " | ".join(headers) + " |"
    separator = "| " + " | ".join("---" for _ in headers) + " |"
    body = "\n".join("| " + " | ".join(str(cell) for cell in row) + " |" for row in rows)
    return "\n".join([header, separator, body])


def ask(prompt: str) -> str:
    return input(prompt).strip()


def ask_yes_no(prompt: str) -> bool:
    return ask(prompt).lower() == "y"


def ask_int(prompt: str) -> int:
    return int(ask(prompt))
