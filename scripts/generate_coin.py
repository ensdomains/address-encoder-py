#!/usr/bin/env python3
"""Scaffold a new non-EVM coin module, test, and registry entry."""

from __future__ import annotations

from _maintainer import (
    COINS_DIR,
    TESTS_DIR,
    normalise_coin_name,
    read_coin_maps,
    regenerate_registry,
    write_coin_maps,
)
from _maintainer import ask, ask_int, ask_yes_no


def build_coin_module(coin_name: str, coin_type: int, *, is_legacy: bool) -> str:
    return f'''from __future__ import annotations

from address_encoder.types import CoinCoder

# TODO: Implement {coin_name} address encoding/decoding.


def encode_{coin_name}_address(source: bytes) -> str:
    raise NotImplementedError("Not implemented")


def decode_{coin_name}_address(source: str) -> bytes:
    raise NotImplementedError("Not implemented")


{coin_name} = CoinCoder(
    name="{coin_name}",
    coin_type={coin_type},
    encode=encode_{coin_name}_address,
    decode=decode_{coin_name}_address,
)
'''


def build_test_module(coin_name: str) -> str:
    return f'''from __future__ import annotations

import pytest

from address_encoder.coins.{coin_name} import decode_{coin_name}_address, encode_{coin_name}_address


@pytest.mark.parametrize(("text", "hex_value"), [
    ("ADDRESS_HERE", "HEX_HERE"),
])
def test_{coin_name}_decode(text: str, hex_value: str) -> None:
    assert decode_{coin_name}_address(text).hex() == hex_value.lower()


@pytest.mark.parametrize(("expected_text", "hex_value"), [
    ("ADDRESS_HERE", "HEX_HERE"),
])
def test_{coin_name}_encode(expected_text: str, hex_value: str) -> None:
    assert encode_{coin_name}_address(bytes.fromhex(hex_value)) == expected_text
'''


def main() -> None:
    if ask_yes_no("Is this an EVM chain? (y/n): "):
        print("Use scripts/add_evm_coin.py for EVM chains.")
        return

    raw_name = ask("Coin Name: ")
    coin_type = ask_int("Coin Type: ")
    full_name = ask("Full Name: ")

    coin_name, is_legacy = normalise_coin_name(raw_name)
    if is_legacy and not full_name.startswith("[LEGACY]"):
        full_name = f"[LEGACY] {full_name}"

    coin_path = COINS_DIR / f"{coin_name}.py"
    test_path = TESTS_DIR / f"test_{coin_name}.py"
    if coin_path.exists() or test_path.exists():
        raise SystemExit(f"Coin module or test already exists for {coin_name}")

    coin_path.write_text(build_coin_module(coin_name, coin_type, is_legacy=is_legacy))
    test_path.write_text(build_test_module(coin_name))
    print(f"Created {coin_path}")
    print(f"Created {test_path}")

    evm, non_evm = read_coin_maps()
    non_evm[coin_type] = (coin_name, full_name)
    write_coin_maps(evm, non_evm)
    print(f"Added {coin_name} to coin maps")

    regenerate_registry()

    print(
        "\nNext steps:\n"
        f"  1. Implement encode/decode in {coin_path}\n"
        f"  2. Add test vectors to {test_path}\n"
        "  3. Run: python3 scripts/format_supported_coins.py\n"
        "  4. Run: pytest"
    )


if __name__ == "__main__":
    main()
