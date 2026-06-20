from __future__ import annotations

import hashlib

from Crypto.Hash import keccak

from address_encoder.types import CoinCoder
from address_encoder.utils.base58_ import base58_unchecked_decode, base58_unchecked_encode


def _vsys_checksum(source: bytes) -> bool:
    if source[0] != 5 or source[1] != 77 or len(source) != 26:
        return False
    checksum = source[-4:]
    new_checksum = keccak.new(
        digest_bits=256,
        data=hashlib.blake2b(source[:-4], digest_size=32).digest(),
    ).digest()[:4]
    return checksum == new_checksum


def encode_vsys_address(source: bytes) -> str:
    if not _vsys_checksum(source):
        raise ValueError("Unrecognised address format")
    return base58_unchecked_encode(source)


def decode_vsys_address(source: str) -> bytes:
    encoded = source[8:] if source.startswith("address:") else source
    if len(encoded) > 36:
        raise ValueError("Unrecognised address format")
    decoded = base58_unchecked_decode(encoded)
    if not _vsys_checksum(decoded):
        raise ValueError("Unrecognised address format")
    return decoded


vsys = CoinCoder(
    name="vsys",
    coin_type=360,
    encode=encode_vsys_address,
    decode=decode_vsys_address,
)

