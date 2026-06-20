from __future__ import annotations

from address_encoder.types import CoinCoder
from address_encoder.utils.bytes_ import base10_to_bytes, bytes_to_base10


def encode_lsk_address(source: bytes) -> str:
    return f"{bytes_to_base10(source)}L"


def decode_lsk_address(source: str) -> bytes:
    if len(source) < 2 or len(source) > 22:
        raise ValueError("Invalid address length")
    if not source.endswith("L") or "." in source:
        raise ValueError("Invalid address format")
    return base10_to_bytes(source[:-1])


lsk = CoinCoder(
    name="lsk",
    coin_type=134,
    encode=encode_lsk_address,
    decode=decode_lsk_address,
)

