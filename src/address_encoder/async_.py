from __future__ import annotations

import importlib

from address_encoder.consts.coin_maps import COIN_NAME_TO_TYPE, COIN_TYPE_TO_NAME
from address_encoder.types import CoinCoder
from address_encoder.utils.evm import SLIP44_MSB, coin_type_to_evm_chain_id

__all__ = ["get_coder_by_coin_name_async", "get_coder_by_coin_type_async"]


async def get_coder_by_coin_name_async(name: str) -> CoinCoder:
    """Lazily load and return the address codec for a coin symbol."""
    coin_type = COIN_NAME_TO_TYPE.get(name)
    if coin_type is None:
        raise ValueError(f"Unsupported coin: {name}")

    if coin_type >= SLIP44_MSB:
        eth_module = importlib.import_module("address_encoder.coins.eth")
        evm_chain_id = coin_type_to_evm_chain_id(coin_type)
        return CoinCoder(
            name=name,
            coin_type=coin_type,
            evm_chain_id=evm_chain_id,
            encode=eth_module.eth.encode,
            decode=eth_module.eth.decode,
        )

    module = importlib.import_module(f"address_encoder.coins.{name}")
    coin = getattr(module, name, None)
    if coin is None:
        raise ValueError(f"Failed to load coin: {name}")
    return coin


async def get_coder_by_coin_type_async(coin_type: int) -> CoinCoder:
    """Lazily load and return the address codec for a SLIP-44 coin type."""
    names = COIN_TYPE_TO_NAME.get(coin_type)

    if coin_type >= SLIP44_MSB:
        eth_module = importlib.import_module("address_encoder.coins.eth")
        evm_chain_id = coin_type_to_evm_chain_id(coin_type)
        is_unknown_chain = names is None
        name = f"Unknown Chain ({evm_chain_id})" if is_unknown_chain else names[0]
        return CoinCoder(
            name=name,
            coin_type=coin_type,
            evm_chain_id=evm_chain_id,
            is_unknown_chain=is_unknown_chain,
            encode=eth_module.eth.encode,
            decode=eth_module.eth.decode,
        )

    if names is None:
        raise ValueError(f"Unsupported coin type: {coin_type}")

    return await get_coder_by_coin_name_async(names[0])
