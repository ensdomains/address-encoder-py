from __future__ import annotations

from address_encoder.types import CoinCoder
from address_encoder.utils.base58_ import base58_check_decode, base58_check_encode

_VERSION = bytes([0x17])


def encode_ont_address(source: bytes) -> str:
    return base58_check_encode(_VERSION + source)


def decode_ont_address(source: str) -> bytes:
    decoded = base58_check_decode(source)
    if decoded[0] != 0x17:
        raise ValueError("Unrecognised address format")
    return decoded[1:]


ont = CoinCoder(
    name="ont",
    coin_type=1024,
    encode=encode_ont_address,
    decode=decode_ont_address,
)

