from __future__ import annotations

import hashlib

from address_encoder.types import CoinCoder
from address_encoder.utils.base58_ import base58_unchecked_decode, base58_unchecked_encode


def _nas_checksum(data: bytes) -> bytes:
    return hashlib.sha3_256(data).digest()[:4]


def _nas_checksum_encode(data: bytes) -> bytes:
    return data + _nas_checksum(data)


def _nas_checksum_decode(data: bytes) -> bytes:
    payload, checksum = data[:-4], data[-4:]
    if _nas_checksum(payload) != checksum:
        raise ValueError("Invalid checksum")
    return payload


def encode_nas_address(source: bytes) -> str:
    checksummed = _nas_checksum_encode(source)
    return base58_unchecked_encode(checksummed)


def decode_nas_address(source: str) -> bytes:
    decoded = base58_unchecked_decode(source)
    if len(decoded) != 26 or decoded[0] != 25 or decoded[1] not in (87, 88):
        raise ValueError("Unrecognised address format")
    return _nas_checksum_decode(decoded)


nas = CoinCoder(
    name="nas",
    coin_type=2718,
    encode=encode_nas_address,
    decode=decode_nas_address,
)

