from __future__ import annotations

from address_encoder.types import CoinCoder
from address_encoder.utils.base58_ import base58_check_decode, base58_check_encode

_VERSION = bytes([0x00])


def encode_hnt_address(source: bytes) -> str:
    return base58_check_encode(_VERSION + source)


def decode_hnt_address(source: str) -> bytes:
    decoded = base58_check_decode(source)
    if decoded[0] != 0:
        raise ValueError("Unrecognised address format")
    return decoded[1:]


hnt = CoinCoder(
    name="hnt",
    coin_type=904,
    encode=encode_hnt_address,
    decode=decode_hnt_address,
)

