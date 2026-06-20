from __future__ import annotations

import base64

BASE32_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"


def base32_encode(data: bytes) -> str:
    return base64.b32encode(data).decode()


def base32_decode(source: str) -> bytes:
    return base64.b32decode(source, casefold=True)


def _convert_bits(data: list[int], from_bits: int, to_bits: int, *, pad: bool = True) -> list[int]:
    acc = 0
    bits = 0
    result: list[int] = []
    max_value = (1 << to_bits) - 1
    for value in data:
        acc = (acc << from_bits) | value
        bits += from_bits
        while bits >= to_bits:
            bits -= to_bits
            result.append((acc >> bits) & max_value)
    if pad and bits:
        result.append((acc << (to_bits - bits)) & max_value)
    return result


def base32_unpadded_encode(data: bytes) -> str:
    bits = _convert_bits(list(data), 8, 5)
    return "".join(BASE32_ALPHABET[value] for value in bits)


def base32_unpadded_decode(source: str) -> bytes:
    values = [BASE32_ALPHABET.index(char) for char in source.upper()]
    return bytes(_convert_bits(values, 5, 8, pad=False))


def base32_crockford_normalise(source: str) -> str:
    return source.upper().replace("O", "0").replace("I", "1").replace("L", "1")


def encode_leb128(value: int) -> bytes:
    result = bytearray()
    current = value
    while True:
        byte = current & 0x7F
        current >>= 7
        if current:
            byte |= 0x80
        result.append(byte)
        if not current:
            break
    return bytes(result)


def decode_leb128(source: bytes) -> int:
    result = 0
    shift = 0
    for byte in source:
        result |= (byte & 0x7F) << shift
        if (byte & 0x80) == 0:
            break
        shift += 7
    return result
