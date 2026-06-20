from __future__ import annotations

from address_encoder.consts.coin_maps import (
    COIN_NAME_TO_TYPE,
    COIN_TYPE_TO_NAME,
    EVM_COIN_NAME_TO_TYPE,
    EVM_COIN_TYPE_TO_NAME,
    NON_EVM_COIN_NAME_TO_TYPE,
    NON_EVM_COIN_TYPE_TO_NAME,
)
from address_encoder.coins import COINS
from address_encoder.types import CoinCoder
from address_encoder.utils.evm import SLIP44_MSB, coin_type_to_evm_chain_id

__all__ = [
    "COIN_NAME_TO_TYPE",
    "COIN_TYPE_TO_NAME",
    "EVM_COIN_NAME_TO_TYPE",
    "EVM_COIN_TYPE_TO_NAME",
    "NON_EVM_COIN_NAME_TO_TYPE",
    "NON_EVM_COIN_TYPE_TO_NAME",
    "CoinCoder",
    "SLIP44_MSB",
    "coin_type_to_evm_chain_id",
    "get_coder_by_coin_name",
    "get_coder_by_coin_type",
]


def get_coder_by_coin_name(name: str) -> CoinCoder:
    """Return the address codec for a coin symbol such as ``btc`` or ``op``."""
    coin = COINS.get(name)
    if coin is not None:
        return coin

    coin_type = COIN_NAME_TO_TYPE.get(name)
    if coin_type is None:
        raise ValueError(f"Unsupported coin: {name}")

    if coin_type >= SLIP44_MSB:
        eth = COINS["eth"]
        evm_chain_id = coin_type_to_evm_chain_id(coin_type)
        return CoinCoder(
            name=name,
            coin_type=coin_type,
            evm_chain_id=evm_chain_id,
            encode=eth.encode,
            decode=eth.decode,
        )

    raise ValueError(f"Unsupported coin: {name}")


def get_coder_by_coin_type(coin_type: int) -> CoinCoder:
    """Return the address codec for a SLIP-44 coin type."""
    names = COIN_TYPE_TO_NAME.get(coin_type)

    if coin_type >= SLIP44_MSB:
        evm_chain_id = coin_type_to_evm_chain_id(coin_type)
        is_unknown_chain = names is None
        name = f"Unknown Chain ({evm_chain_id})" if is_unknown_chain else names[0]
        eth = COINS["eth"]
        return CoinCoder(
            name=name,
            coin_type=coin_type,
            evm_chain_id=evm_chain_id,
            is_unknown_chain=is_unknown_chain,
            encode=eth.encode,
            decode=eth.decode,
        )

    if names is None:
        raise ValueError(f"Unsupported coin type: {coin_type}")

    return get_coder_by_coin_name(names[0])
