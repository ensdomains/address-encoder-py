from __future__ import annotations

from address_encoder.types import CoinCoder
from address_encoder.utils.base58_ import base58_check_decode, base58_check_encode


def encode_ark_address(source: bytes) -> str:
    return base58_check_encode(source)


def decode_ark_address(source: str) -> bytes:
    decoded = base58_check_decode(source)
    if decoded[0] != 23:
        raise ValueError("Invalid address")
    return decoded


ark = CoinCoder(
    name="ark",
    coin_type=111,
    encode=encode_ark_address,
    decode=decode_ark_address,
)

