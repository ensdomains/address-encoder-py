from __future__ import annotations

from address_encoder.types import CoinCoder
from address_encoder.utils.base32 import base32_decode, base32_encode
from address_encoder.utils.bytes_ import hex_without_prefix_to_bytes

_VERSION_BYTE = bytes([0x30])


def _xlm_checksum(source: bytes) -> bytes:
    crc = 0
    for byte in source:
        code = (crc >> 8) & 0xFF
        code ^= byte & 0xFF
        code ^= code >> 4
        crc = (crc << 8) & 0xFFFF
        crc ^= code
        code = (code << 5) & 0xFFFF
        crc ^= code
        code = (code << 7) & 0xFFFF
        crc ^= code
    return hex_without_prefix_to_bytes(format(crc, "04x"))[::-1]


def encode_xlm_address(source: bytes) -> str:
    payload = _VERSION_BYTE + source
    payload_with_checksum = payload + _xlm_checksum(payload)
    return base32_encode(payload_with_checksum)


def decode_xlm_address(source: str) -> bytes:
    decoded = base32_decode(source)
    version = decoded[0]
    payload = decoded[:-2]
    output = payload[1:]
    checksum = decoded[-2:]
    if version != _VERSION_BYTE[0]:
        raise ValueError("Unrecognised address format")
    if _xlm_checksum(payload) != checksum:
        raise ValueError("Unrecognised address format")
    return output


xlm = CoinCoder(
    name="xlm",
    coin_type=148,
    encode=encode_xlm_address,
    decode=decode_xlm_address,
)

