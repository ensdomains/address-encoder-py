from __future__ import annotations

from Crypto.Hash import keccak

from address_encoder.types import CoinCoder
from address_encoder.utils.base32 import base32_decode, base32_encode
from address_encoder.utils.bytes_ import bytes_to_hex_without_prefix


def encode_xem_address(source: bytes) -> str:
    return base32_encode(source)


def decode_xem_address(source: str) -> bytes:
    address = source.upper().replace("-", "")
    if not address or len(address) != 40:
        raise ValueError("Invalid address")
    decoded = base32_decode(address)
    checksum = bytes_to_hex_without_prefix(keccak.new(digest_bits=256, data=decoded[:21]).digest())[:8]
    if checksum != bytes_to_hex_without_prefix(decoded[21:]):
        raise ValueError("Invalid address")
    return decoded


xem = CoinCoder(
    name="xem",
    coin_type=43,
    encode=encode_xem_address,
    decode=decode_xem_address,
)

