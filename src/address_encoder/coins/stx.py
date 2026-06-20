from __future__ import annotations

import hashlib

from address_encoder.types import CoinCoder
from address_encoder.utils.base32 import base32_crockford_normalise

_PREFIX = "S"
_LENGTH = 20
_CHECKSUM_LENGTH = 4
_P2PKH_VERSION = bytes([22])
_P2SH_VERSION = bytes([20])
_STX_ALPHABET = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"


def _convert_radix_stx(data: list[int], from_bits: int, to_bits: int, padding: bool) -> list[int]:
    carry = 0
    pos = 0
    mask = (1 << to_bits) - 1
    result: list[int] = []
    for value in reversed(data):
        carry = (value << pos) | carry
        pos += from_bits
        index = 0
        while pos >= to_bits:
            pos -= to_bits
            result.insert(0, ((carry >> (to_bits * index)) & mask))
            index += 1
        carry >>= to_bits * index
    if not padding and pos >= from_bits:
        raise ValueError("Excess padding")
    if not padding and carry:
        raise ValueError(f"Non-zero padding: {carry}")
    if padding and pos > 0:
        result.insert(0, carry)
    return result


def _stx_radix_encode(source: bytes) -> list[int]:
    return _convert_radix_stx(list(source), 8, 5, True)


def _stx_radix_decode(source: list[int]) -> bytes:
    return bytes(_convert_radix_stx(source, 5, 8, False))


def _stx_base32_encode(source: bytes) -> str:
    values = _stx_radix_encode(source)
    return "".join(_STX_ALPHABET[value] for value in values)


def _stx_base32_decode(source: str) -> bytes:
    values = [_STX_ALPHABET.index(char) for char in source]
    return _stx_radix_decode(values)


def _stx_checksum(data: bytes) -> bytes:
    first = hashlib.sha256(data).digest()
    return hashlib.sha256(first).digest()[:_CHECKSUM_LENGTH]


def encode_stx_address(source: bytes) -> str:
    if len(source) != _LENGTH + _CHECKSUM_LENGTH:
        raise ValueError("Unrecognised address format")
    hash160 = source[:_LENGTH]
    checksum = source[-_CHECKSUM_LENGTH:]
    if checksum == _stx_checksum(_P2PKH_VERSION + hash160):
        version = "P"
    elif checksum == _stx_checksum(_P2SH_VERSION + hash160):
        version = "M"
    else:
        raise ValueError("Unrecognised address format")
    encoded = _stx_base32_encode(source)
    return f"{_PREFIX}{version}{encoded}"


def decode_stx_address(source: str) -> bytes:
    if len(source) < 6:
        raise ValueError("Unrecognised address format")
    if source[0] != "S":
        raise ValueError("Unrecognised address format")
    normalised = base32_crockford_normalise(source)
    version = normalised[1]
    if version == "P":
        version_bytes = _P2PKH_VERSION
    elif version == "M":
        version_bytes = _P2SH_VERSION
    else:
        raise ValueError("Unrecognised address format")
    payload = _stx_base32_decode(normalised[2:])
    decoded = payload[:-_CHECKSUM_LENGTH]
    checksum = payload[-_CHECKSUM_LENGTH:]
    if _stx_checksum(version_bytes + decoded) != checksum:
        raise ValueError("Unrecognised address format")
    return payload


stx = CoinCoder(
    name="stx",
    coin_type=5757,
    encode=encode_stx_address,
    decode=decode_stx_address,
)

