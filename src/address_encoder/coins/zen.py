from __future__ import annotations

from address_encoder.types import CoinCoder
from address_encoder.utils.base58_ import base58_check_decode, base58_check_encode

_VALID_PREFIXES = (
    bytes([0x20, 0x89]),
    bytes([0x1C, 0xB8]),
    bytes([0x20, 0x96]),
    bytes([0x1C, 0xBD]),
    bytes([0x16, 0x9A]),
)


def encode_zen_address(source: bytes) -> str:
    prefix = source[:2]
    if prefix not in _VALID_PREFIXES:
        raise ValueError("Invalid prefix")
    return base58_check_encode(source)


def decode_zen_address(source: str) -> bytes:
    decoded = base58_check_decode(source)
    prefix = decoded[:2]
    if prefix not in _VALID_PREFIXES:
        raise ValueError("Invalid prefix")
    return decoded


zen = CoinCoder(
    name="zen",
    coin_type=121,
    encode=encode_zen_address,
    decode=decode_zen_address,
)

