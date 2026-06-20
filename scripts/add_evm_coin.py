#!/usr/bin/env python3
"""Add one or more EVM chains to the coin type map."""

from __future__ import annotations

from _maintainer import (
    COIN_MAPS_PATH,
    evm_chain_id_to_coin_type,
    read_coin_maps,
    write_coin_maps,
)
from _maintainer import ask, ask_int, ask_yes_no


def main() -> None:
    evm, non_evm = read_coin_maps()
    new_coins: list[tuple[int, tuple[str, str]]] = []

    while True:
        coin_symbol = ask("Coin Symbol: ").lower().strip()
        coin_name = ask("Coin Name: ").strip()
        chain_id = ask_int("Chain ID: ")
        coin_type = evm_chain_id_to_coin_type(chain_id)
        new_coins.append((coin_type, (coin_symbol, coin_name)))

        if not ask_yes_no("Add another coin? (y/n): "):
            break

    if not new_coins:
        print("No coins added.")
        return

    for coin_type, entry in new_coins:
        evm[coin_type] = entry

    write_coin_maps(evm, non_evm)
    print("Adding new coins:", ", ".join(display for _, (_, display) in new_coins))
    print(f"Updated {COIN_MAPS_PATH}")
    print("\nNext step: python3 scripts/format_supported_coins.py")
    print("Done!")


if __name__ == "__main__":
    main()
