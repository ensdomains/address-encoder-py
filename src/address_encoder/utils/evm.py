from __future__ import annotations

SLIP44_MSB = 0x80000000


def is_evm_coin_type(coin_type: int) -> bool:
    return (coin_type & SLIP44_MSB) != 0


def evm_chain_id_to_coin_type(chain_id: int) -> int:
    if chain_id >= SLIP44_MSB:
        raise ValueError("Invalid chainId")
    return (SLIP44_MSB | chain_id) & 0xFFFFFFFF


def coin_type_to_evm_chain_id(coin_type: int) -> int:
    if (coin_type & SLIP44_MSB) == 0:
        raise ValueError("Coin type is not an EVM chain")
    return ((SLIP44_MSB - 1) & coin_type) & 0xFFFFFFFF
