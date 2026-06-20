from __future__ import annotations

from address_encoder.types import CoinCoder
from address_encoder.utils.bytes_ import bytes_to_string, string_to_bytes
from address_encoder.utils.near import validate_near_address


def encode_near_address(source: bytes) -> str:
    encoded = bytes_to_string(source)
    if not validate_near_address(encoded):
        raise ValueError("Unrecognised address format")
    return encoded


def decode_near_address(source: str) -> bytes:
    if not validate_near_address(source):
        raise ValueError("Unrecognised address format")
    return string_to_bytes(source)


near = CoinCoder(
    name="near",
    coin_type=397,
    encode=encode_near_address,
    decode=decode_near_address,
)

