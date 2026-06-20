from __future__ import annotations

from Crypto.Hash import keccak

from address_encoder.types import CoinCoder
from address_encoder.utils.base58_ import base58xmr_decode, base58xmr_encode

_VALID_TAGS = (bytes([0x06]), bytes([0xCE, 0xF6, 0x22]))


def _bcn_checksum(data: bytes) -> bytes:
    return keccak.new(digest_bits=256, data=data).digest()[:4]


def _bcn_checksum_decode(data: bytes) -> bytes:
    payload, checksum = data[:-4], data[-4:]
    if _bcn_checksum(payload) != checksum:
        raise ValueError("Invalid checksum")
    return payload


def encode_bcn_address(source: bytes) -> str:
    checksum = _bcn_checksum(source)
    return base58xmr_encode(source + checksum)


def decode_bcn_address(source: str) -> bytes:
    decoded = base58xmr_decode(source)
    tag = decoded[:-68]
    if len(decoded) < 68 or tag not in _VALID_TAGS:
        raise ValueError("Unrecognised address format")
    return _bcn_checksum_decode(decoded)


bcn = CoinCoder(
    name="bcn",
    coin_type=204,
    encode=encode_bcn_address,
    decode=decode_bcn_address,
)

