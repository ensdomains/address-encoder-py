from __future__ import annotations

import re

from address_encoder.types import CoinCoder
from address_encoder.utils.bytes_ import bytes_to_hex, hex_without_prefix_to_bytes

_HEX_REGEX = re.compile(r"^[0-9A-Fa-f]{64}$")


def encode_aion_address(source: bytes) -> str:
    if len(source) != 32:
        raise ValueError("Unrecognised address format")
    return bytes_to_hex(source)


def decode_aion_address(source: str) -> bytes:
    no_prefix = source[2:] if source.startswith("0x") else source
    if len(no_prefix) != 64:
        raise ValueError("Unrecognised address format")
    if not _HEX_REGEX.fullmatch(no_prefix):
        raise ValueError("Unrecognised address format")
    return hex_without_prefix_to_bytes(no_prefix)


aion = CoinCoder(
    name="aion",
    coin_type=425,
    encode=encode_aion_address,
    decode=decode_aion_address,
)

