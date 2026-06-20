from __future__ import annotations

import hashlib

from address_encoder.types import CoinCoder
from address_encoder.utils.bytes_ import bytes_to_hex_without_prefix, hex_without_prefix_to_bytes

_LENGTH = 32
_CHECKSUM_LENGTH = 6


def _sc_checksum(source: bytes) -> bytes:
    return hashlib.blake2b(source, digest_size=_LENGTH).digest()[:_CHECKSUM_LENGTH]


def encode_sc_address(source: bytes) -> str:
    checksum = _sc_checksum(source)
    return bytes_to_hex_without_prefix(source + checksum)


def decode_sc_address(source: str) -> bytes:
    if len(source) != 76:
        raise ValueError("Unrecognised address format")
    decoded = hex_without_prefix_to_bytes(source)
    payload = decoded[:-_CHECKSUM_LENGTH]
    checksum = decoded[-_CHECKSUM_LENGTH:]
    if _sc_checksum(payload) != checksum:
        raise ValueError("Unrecognised address format")
    return payload


sc = CoinCoder(
    name="sc",
    coin_type=1991,
    encode=encode_sc_address,
    decode=decode_sc_address,
)

