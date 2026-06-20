from __future__ import annotations

import hashlib

from address_encoder.utils.base58_ import base58_unchecked_decode, base58_unchecked_encode

PREFIX_STRING_BYTES = b"SS58PRE"


def _dot_checksum(source_with_type_prefix: bytes) -> bytes:
    return hashlib.blake2b(PREFIX_STRING_BYTES + source_with_type_prefix, digest_size=64).digest()[:2]


def create_dot_address_encoder(coin_type: int):
    def encode(source: bytes) -> str:
        source_with_type_prefix = bytes([coin_type]) + source
        checksum = _dot_checksum(source_with_type_prefix)
        return base58_unchecked_encode(source_with_type_prefix + checksum)

    return encode


def create_dot_address_decoder(coin_type: int):
    def decode(source: str) -> bytes:
        decoded = base58_unchecked_decode(source)
        if decoded[0] != coin_type:
            raise ValueError("Unrecognized address format")
        checksum = decoded[33:35]
        if checksum != _dot_checksum(decoded[:33]):
            raise ValueError("Unrecognized address format")
        return decoded[1:33]

    return decode
