from __future__ import annotations

import re

from Crypto.Hash import keccak

from address_encoder.types import CoinCoder
from address_encoder.utils.bytes_ import bytes_to_hex_without_prefix, hex_to_bytes

_ADDRESS_LENGTH = 32
_ADDRESS_REGEX = re.compile(r"^0x[a-fA-F0-9]{64}$")


def _raw_checksum_address(address: list[str], digest: bytes, length: int) -> str:
    for index in range(0, length, 2):
        if digest[index >> 1] >> 4 >= 8 and address[index]:
            address[index] = address[index].upper()
        if (digest[index >> 1] & 0x0F) >= 8 and address[index + 1]:
            address[index + 1] = address[index + 1].upper()
    return f"0x{''.join(address)}"


def _strk_checksum(source: bytes) -> str:
    chars = list(bytes_to_hex_without_prefix(source).lower())
    leading_zero_index = next((index for index, byte in enumerate(source) if byte != 0x00), -1)
    leading_zero_stripped = source[leading_zero_index:] if leading_zero_index > 0 else source
    digest = bytearray(32)
    digest[leading_zero_index:] = keccak.new(digest_bits=256, data=leading_zero_stripped).digest()
    return _raw_checksum_address(chars, bytes(digest), 64)


def encode_strk_address(source: bytes) -> str:
    if len(source) != _ADDRESS_LENGTH:
        raise ValueError("Unrecognised address format")
    return _strk_checksum(source)


def decode_strk_address(source: str) -> bytes:
    if not _ADDRESS_REGEX.fullmatch(source):
        raise ValueError("Unrecognised address format")
    decoded = hex_to_bytes(source)
    if _strk_checksum(decoded) != source:
        raise ValueError("Unrecognised address format")
    return decoded


strk = CoinCoder(
    name="strk",
    coin_type=9004,
    encode=encode_strk_address,
    decode=decode_strk_address,
)

