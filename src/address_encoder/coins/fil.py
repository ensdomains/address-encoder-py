from __future__ import annotations

import hashlib

from address_encoder.types import CoinCoder
from address_encoder.utils.base32 import (
    base32_unpadded_decode,
    base32_unpadded_encode,
    decode_leb128,
    encode_leb128,
)


def _validate_fil_address(address: str) -> bool:
    if len(address) < 3:
        return False
    if address[0] != "f":
        return False
    if address[1] == "0":
        return len(address) <= 22
    if address[1] in ("1", "2"):
        return len(address) == 41
    if address[1] == "3":
        return len(address) == 86
    return False


def _fil_checksum(source: bytes) -> bytes:
    return hashlib.blake2b(source, digest_size=4).digest()


def encode_fil_address(source: bytes) -> str:
    payload = source[1:]
    protocol = source[0]
    if protocol == 0:
        decoded = decode_leb128(payload)
        return f"f{protocol}{decoded}"
    checksum = hashlib.blake2b(source, digest_size=4).digest()
    encoded = base32_unpadded_encode(payload + checksum).lower()
    return f"f{protocol}{encoded}"


def decode_fil_address(source: str) -> bytes:
    if not _validate_fil_address(source):
        raise ValueError("Unrecognised address format")

    protocol = int(source[1], 10)
    protocol_byte = bytes([protocol])
    encoded = source[2:]

    if protocol == 0:
        return protocol_byte + encode_leb128(int(encoded))

    payload_with_checksum = base32_unpadded_decode(encoded.upper())
    payload = payload_with_checksum[:-4]
    checksum = payload_with_checksum[-4:]
    decoded = protocol_byte + payload
    if _fil_checksum(decoded) != checksum:
        raise ValueError("Unrecognised address format")
    return decoded


fil = CoinCoder(
    name="fil",
    coin_type=461,
    encode=encode_fil_address,
    decode=decode_fil_address,
)

