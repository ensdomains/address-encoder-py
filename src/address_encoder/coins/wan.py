from __future__ import annotations

from Crypto.Hash import keccak

from address_encoder.types import CoinCoder
from address_encoder.utils.bytes_ import bytes_to_hex_without_prefix, hex_to_bytes, string_to_bytes
from address_encoder.utils.hex_ import is_address


def _wan_checksum(address_bytes: bytes) -> str:
    address_str = bytes_to_hex_without_prefix(address_bytes)
    address = list(address_str)
    digest = keccak.new(digest_bits=256, data=string_to_bytes(address_str)).digest()
    for index in range(40):
        hash_byte = digest[index // 2]
        if index % 2 == 0:
            hash_byte >>= 4
        else:
            hash_byte &= 0x0F
        if address[index] > "9" and hash_byte <= 7:
            address[index] = address[index].upper()
    return f"0x{''.join(address)}"


def encode_wan_address(source: bytes) -> str:
    return _wan_checksum(source)


def decode_wan_address(source: str) -> bytes:
    if not is_address(source):
        raise ValueError("Unrecognised address format")
    decoded = hex_to_bytes(source)
    if _wan_checksum(decoded) != source:
        raise ValueError("Unrecognised address format")
    return decoded


wan = CoinCoder(
    name="wan",
    coin_type=5718350,
    encode=encode_wan_address,
    decode=decode_wan_address,
)

