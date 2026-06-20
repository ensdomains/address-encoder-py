#!/usr/bin/env python3
"""Regenerate supported-cryptocurrencies.md from the coin type maps."""

from __future__ import annotations

import re

from _maintainer import (
    DOCS_PATH,
    coin_type_to_evm_chain_id,
    markdown_table,
    read_coin_maps,
)


def build_name_to_type(
    mapping: dict[int, tuple[str, str]],
) -> dict[str, int]:
    return {symbol: coin_type for coin_type, (symbol, _) in mapping.items()}


def existing_encoding_types(content: str) -> dict[int, str]:
    encoding_types: dict[int, str] = {}
    for line in content.splitlines():
        if not line.startswith("|"):
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) < 4 or not parts[0].isdigit():
            continue
        encoding_types[int(parts[0])] = parts[3]
    return encoding_types


def main() -> None:
    evm, non_evm = read_coin_maps()
    evm_name_to_type = build_name_to_type(evm)
    non_evm_name_to_type = build_name_to_type(non_evm)
    existing = existing_encoding_types(DOCS_PATH.read_text()) if DOCS_PATH.exists() else {}

    evm_rows = [
        [
            coin_type_to_evm_chain_id(coin_type),
            symbol,
            display,
            coin_type,
        ]
        for coin_type, (symbol, display) in sorted(evm.items())
    ]

    legacy_rows = []
    for coin_type, (symbol, display) in sorted(non_evm.items()):
        if not symbol.endswith("Legacy"):
            continue
        replacement_name = symbol[:-6]
        replacement = non_evm_name_to_type.get(replacement_name) or evm_name_to_type.get(
            replacement_name
        )
        legacy_rows.append(
            [
                coin_type,
                symbol,
                re.sub(r"^\[LEGACY\] ", "", display),
                replacement_name,
                replacement if replacement is not None else "",
            ]
        )

    main_rows = []
    for coin_type, (symbol, display) in sorted(non_evm.items()):
        if symbol.endswith("Legacy"):
            continue
        encoding_type = existing.get(
            coin_type,
            "[UNKNOWN ENCODING TYPE, PLEASE ADD BEFORE MERGING]",
        )
        main_rows.append([coin_type, symbol, display, encoding_type])

    markdown = "\n".join(
        [
            "## Supported Cryptocurrencies",
            "",
            "### EVM Chains",
            "",
            "The following EVM chains are supported:",
            "",
            markdown_table(["Chain ID", "Name", "Full Name", "Coin Type"], evm_rows),
            "",
            "### Legacy Coins",
            "",
            "The following legacy coins are supported:",
            "",
            markdown_table(
                [
                    "Coin Type",
                    "Name",
                    "Full Name",
                    "Replacement Name",
                    "Replacement Coin Type",
                ],
                legacy_rows,
            ),
            "",
            "### Coins",
            "",
            "The following coins are supported:",
            "",
            markdown_table(["Coin Type", "Name", "Full Name", "Encoding Type"], main_rows),
            "",
        ]
    )
    DOCS_PATH.parent.mkdir(parents=True, exist_ok=True)
    DOCS_PATH.write_text(markdown)
    print(f"Updated {DOCS_PATH}")


if __name__ == "__main__":
    main()
