from __future__ import annotations

from address_encoder.types import CoinCoder
from address_encoder.utils.base58_ import base58_check_decode, base58_check_encode

_TZ1_PREFIX = bytes([0x06, 0xA1, 0x9F])
_TZ2_PREFIX = bytes([0x06, 0xA1, 0xA1])
_TZ3_PREFIX = bytes([0x06, 0xA1, 0xA4])
_KT1_PREFIX = bytes([0x02, 0x5A, 0x79])


def encode_xtz_address(source: bytes) -> str:
    if len(source) not in (21, 22):
        raise ValueError("Unrecognised address format")
    version = source[0]
    if version == 0:
        if source[1] == 0x00:
            prefix = _TZ1_PREFIX
        elif source[1] == 0x01:
            prefix = _TZ2_PREFIX
        elif source[1] == 0x02:
            prefix = _TZ3_PREFIX
        else:
            raise ValueError("Unrecognised address format")
        return base58_check_encode(prefix + source[2:])
    if version == 1:
        return base58_check_encode(_KT1_PREFIX + source[1:21])
    raise ValueError("Unrecognised address format")


def decode_xtz_address(source: str) -> bytes:
    decoded = base58_check_decode(source)[3:]
    prefix = source[:3]
    if prefix == "tz1":
        return bytes([0x00, 0x00]) + decoded
    if prefix == "tz2":
        return bytes([0x00, 0x01]) + decoded
    if prefix == "tz3":
        return bytes([0x00, 0x02]) + decoded
    if prefix == "KT1":
        return bytes([0x01]) + decoded + bytes([0x00])
    raise ValueError("Unrecognised address format")


xtz = CoinCoder(
    name="xtz",
    coin_type=1729,
    encode=encode_xtz_address,
    decode=decode_xtz_address,
)

