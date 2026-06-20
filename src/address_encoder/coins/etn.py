from __future__ import annotations

from Crypto.Hash import keccak

from address_encoder.types import CoinCoder
from address_encoder.utils.base58_ import base58xmr_decode, base58xmr_encode

_TYPE = 18


def _etn_checksum(data: bytes) -> bytes:
    return keccak.new(digest_bits=256, data=data).digest()[:4]


def _etn_checksum_encode(data: bytes) -> bytes:
    return data + _etn_checksum(data)


def _etn_checksum_decode(data: bytes) -> bytes:
    payload, checksum = data[:-4], data[-4:]
    if _etn_checksum(payload) != checksum:
        raise ValueError("Invalid checksum")
    return payload


def encode_etn_address(source: bytes) -> str:
    source_with_type = bytes([_TYPE]) + source
    checksummed = _etn_checksum_encode(source_with_type)
    return base58xmr_encode(checksummed)


def decode_etn_address(source: str) -> bytes:
    decoded = base58xmr_decode(source)
    if decoded[0] != _TYPE:
        raise ValueError("Unrecognised address format")
    checksummed = _etn_checksum_decode(decoded)
    return checksummed[1:]


etn = CoinCoder(
    name="etn",
    coin_type=415,
    encode=encode_etn_address,
    decode=decode_etn_address,
)

