from __future__ import annotations

import hashlib

from address_encoder.types import CoinCoder
from address_encoder.utils.base32 import base32_unpadded_decode, base32_unpadded_encode


def _algo_checksum(data: bytes) -> bytes:
    return hashlib.new("sha512-256", data).digest()[-4:]


def _algo_checksum_encode(data: bytes) -> bytes:
    return data + _algo_checksum(data)


def _algo_checksum_decode(data: bytes) -> bytes:
    payload, checksum = data[:-4], data[-4:]
    if _algo_checksum(payload) != checksum:
        raise ValueError("Invalid checksum")
    return payload


def encode_algo_address(source: bytes) -> str:
    checksummed = _algo_checksum_encode(source)
    return base32_unpadded_encode(checksummed)


def decode_algo_address(source: str) -> bytes:
    decoded = base32_unpadded_decode(source)
    if len(decoded) != 36:
        raise ValueError("Unrecognised address format")
    return _algo_checksum_decode(decoded)


algo = CoinCoder(
    name="algo",
    coin_type=283,
    encode=encode_algo_address,
    decode=decode_algo_address,
)

