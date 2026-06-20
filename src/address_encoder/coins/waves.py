from __future__ import annotations

import hashlib

from Crypto.Hash import keccak

from address_encoder.types import CoinCoder
from address_encoder.utils.base58_ import base58_unchecked_decode, base58_unchecked_encode

_CHECKSUM_LENGTH = 4


def _waves_checksum(data: bytes) -> bytes:
    return keccak.new(digest_bits=256, data=hashlib.blake2b(data, digest_size=32).digest()).digest()


def _waves_checksum_decode(data: bytes) -> bytes:
    payload, checksum = data[:-_CHECKSUM_LENGTH], data[-_CHECKSUM_LENGTH:]
    if _waves_checksum(payload)[:_CHECKSUM_LENGTH] != checksum:
        raise ValueError("Invalid checksum")
    return payload


encode_waves_address = base58_unchecked_encode


def decode_waves_address(source: str) -> bytes:
    decoded = base58_unchecked_decode(source)
    if decoded[0] != 1:
        raise ValueError("Invalid address format")
    if decoded[1] != 87 or len(decoded) != 26:
        raise ValueError("Invalid address format")
    _waves_checksum_decode(decoded)
    return decoded


waves = CoinCoder(
    name="waves",
    coin_type=5741564,
    encode=encode_waves_address,
    decode=decode_waves_address,
)

