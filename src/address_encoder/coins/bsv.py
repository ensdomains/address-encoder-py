from __future__ import annotations

from address_encoder.types import CoinCoder
from address_encoder.utils.base58_ import base58_check_decode, base58_check_encode

_VERSION = bytes([0x00])


def encode_bsv_address(source: bytes) -> str:
    return base58_check_encode(_VERSION + source)


def decode_bsv_address(source: str) -> bytes:
    decoded = base58_check_decode(source)
    if len(decoded) != 21:
        raise ValueError("Unrecognised address format")
    if decoded[0] != 0x00:
        raise ValueError("Unrecognised address format")
    return decoded[1:]


bsv = CoinCoder(
    name="bsv",
    coin_type=236,
    encode=encode_bsv_address,
    decode=decode_bsv_address,
)

