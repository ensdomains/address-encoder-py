from __future__ import annotations

from address_encoder.types import CoinCoder
from address_encoder.utils.base58_ import base58_unchecked_decode, base58_unchecked_encode


def encode_sol_address(source: bytes) -> str:
    if len(source) != 32:
        raise ValueError("Unrecognised address format")
    encoded = base58_unchecked_encode(source)
    if len(encoded) < 32 or len(encoded) > 44:
        raise ValueError("Unrecognised address format")
    return encoded


def decode_sol_address(source: str) -> bytes:
    if len(source) < 32 or len(source) > 44:
        raise ValueError("Unrecognised address format")
    decoded = base58_unchecked_decode(source)
    if len(decoded) != 32:
        raise ValueError("Unrecognised address format")
    return decoded


sol = CoinCoder(
    name="sol",
    coin_type=501,
    encode=encode_sol_address,
    decode=decode_sol_address,
)

