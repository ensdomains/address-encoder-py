from __future__ import annotations

from address_encoder.types import CoinCoder
from address_encoder.utils.bytes_ import bytes_to_hex_without_prefix, hex_without_prefix_to_bytes

_HX_PREFIX = bytes([0x00])
_CX_PREFIX = bytes([0x01])


def encode_icx_address(source: bytes) -> str:
    if len(source) != 21:
        raise ValueError("Invalid address length")
    address_type = source[0]
    if address_type == 0x00:
        return f"hx{bytes_to_hex_without_prefix(source[1:])}"
    if address_type == 0x01:
        return f"cx{bytes_to_hex_without_prefix(source[1:])}"
    raise ValueError("Invalid address type")


def decode_icx_address(source: str) -> bytes:
    prefix = source[:2]
    body = source[2:]
    if prefix == "hx":
        return _HX_PREFIX + hex_without_prefix_to_bytes(body)
    if prefix == "cx":
        return _CX_PREFIX + hex_without_prefix_to_bytes(body)
    raise ValueError("Invalid address prefix")


icx = CoinCoder(
    name="icx",
    coin_type=74,
    encode=encode_icx_address,
    decode=decode_icx_address,
)

