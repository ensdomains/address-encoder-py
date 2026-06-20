from __future__ import annotations

from address_encoder.types import CoinCoder
from address_encoder.utils.base58_ import base58_unchecked_decode, base58_unchecked_encode

_PREFIX_REFERENCE = ["a", "b", "c", "d", "e"]


def _decode_prefix(source: str) -> str:
    for char in source:
        if ord(char) >= 97:
            return source[source.index(char) + 1 :]
    raise ValueError("Unrecognised address format")


def _signed_byte(byte: int) -> int:
    return byte - 256 if byte > 127 else byte


def encode_nuls_address(source: bytes) -> str:
    chain_id = (source[0] & 0xFF) | ((source[1] & 0xFF) << 8)
    payload = bytearray(len(source) + 1)
    xor = 0x00
    for index, byte in enumerate(source):
        value = _signed_byte(byte)
        payload[index] = value & 0xFF
        xor ^= value
    payload[len(source)] = xor & 0xFF

    if chain_id == 1:
        prefix = "NULS"
    elif chain_id == 2:
        prefix = "tNULS"
    else:
        chain_id_bytes = bytes([chain_id & 0xFF, (chain_id >> 8) & 0xFF])
        prefix = base58_unchecked_encode(chain_id_bytes).upper()

    return prefix + _PREFIX_REFERENCE[len(prefix) - 1] + base58_unchecked_encode(bytes(payload))


def decode_nuls_address(source: str) -> bytes:
    if source.startswith("NULS"):
        source_without_prefix = source[5:]
    elif source.startswith("tNULS"):
        source_without_prefix = source[6:]
    else:
        source_without_prefix = _decode_prefix(source)

    payload = bytearray(base58_unchecked_decode(source_without_prefix))
    xor = 0x00
    for index in range(len(payload) - 1):
        value = _signed_byte(payload[index])
        payload[index] = value & 0xFF
        xor ^= value
    if xor < 0:
        xor += 256
    if xor != payload[-1]:
        raise ValueError("Unrecognised address format")
    return bytes(payload[:-1])


nuls = CoinCoder(
    name="nuls",
    coin_type=8964,
    encode=encode_nuls_address,
    decode=decode_nuls_address,
)

