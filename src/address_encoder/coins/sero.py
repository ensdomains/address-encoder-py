from __future__ import annotations

from address_encoder.types import CoinCoder
from address_encoder.utils.base58_ import base58_unchecked_decode, base58_unchecked_encode

encode_sero_address = base58_unchecked_encode


def decode_sero_address(source: str) -> bytes:
    decoded = base58_unchecked_decode(source)
    if len(decoded) != 96:
        raise ValueError("Unrecognised address format")
    return decoded


sero = CoinCoder(
    name="sero",
    coin_type=569,
    encode=encode_sero_address,
    decode=decode_sero_address,
)

