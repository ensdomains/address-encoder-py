from __future__ import annotations

import re

from address_encoder.types import CoinCoder
from address_encoder.utils.bytes_ import bytes_to_hex, hex_to_bytes
from address_encoder.utils.hex_ import strip_hex_prefix

_ADDRESS_REGEX = re.compile(r"^(0x[a-fA-F0-9]{64}|[a-fA-F0-9]{64})$")


def encode_sui_address(source: bytes) -> str:
    if len(source) != 32:
        raise ValueError("Unrecognised address format")
    return bytes_to_hex(source).lower()


def decode_sui_address(source: str) -> bytes:
    stripped = strip_hex_prefix(source)
    if not _ADDRESS_REGEX.fullmatch(source) and not re.fullmatch(r"^[a-fA-F0-9]{64}$", stripped):
        raise ValueError("Unrecognised address format")
    decoded = hex_to_bytes(f"0x{stripped}")
    if len(decoded) != 32:
        raise ValueError("Unrecognised address format")
    return decoded


sui = CoinCoder(
    name="sui",
    coin_type=784,
    encode=encode_sui_address,
    decode=decode_sui_address,
)

