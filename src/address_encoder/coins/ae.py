from __future__ import annotations

from address_encoder.types import CoinCoder
from address_encoder.utils.base58_ import base58_check_decode, base58_check_encode

_PREFIX = bytes([0x30, 0x78])


def encode_ae_address(source: bytes) -> str:
    return f"ak_{base58_check_encode(source[2:])}"


def decode_ae_address(source: str) -> bytes:
    return _PREFIX + base58_check_decode(source[3:])


ae = CoinCoder(
    name="ae",
    coin_type=457,
    encode=encode_ae_address,
    decode=decode_ae_address,
)

