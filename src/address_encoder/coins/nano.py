from __future__ import annotations

import hashlib

from address_encoder.types import CoinCoder

_NANO_ALPHABET = "13456789abcdefghijkmnopqrstuwxyz"


def _convert_radix_nano(data: list[int], from_bits: int, to_bits: int) -> list[int]:
    leftover = (len(data) * from_bits) % to_bits
    offset = 0 if leftover == 0 else to_bits - leftover
    carry = 0
    pos = 0
    mask = (1 << to_bits) - 1
    result: list[int] = []

    for value in data:
        if value >= (1 << from_bits):
            raise ValueError(f"convertRadixNano: invalid data word={value} from={from_bits}")
        carry = (carry << from_bits) | value
        if pos + from_bits > 32:
            raise ValueError(f"convertRadixNano: carry overflow pos={pos} from={from_bits}")
        pos += from_bits
        while pos >= to_bits:
            pos -= to_bits
            result.append((carry >> (pos + offset)) & mask)
    carry = (carry << (to_bits - (pos + offset))) & mask
    if pos > 0:
        result.append(carry)
    return result


def _nano_radix_encode(source: bytes) -> list[int]:
    return _convert_radix_nano(list(source), 8, 5)


def _nano_radix_decode(source: list[int]) -> bytes:
    leftover = (len(source) * 5) % 8
    result = _convert_radix_nano(source, 5, 8)
    if leftover != 0:
        result = result[1:]
    return bytes(result)


def _nano_base32_encode(source: bytes) -> str:
    values = _nano_radix_encode(source)
    return "".join(_NANO_ALPHABET[value] for value in values)


def _nano_base32_decode(source: str) -> bytes:
    values = [_NANO_ALPHABET.index(char) for char in source]
    return _nano_radix_decode(values)


def encode_nano_address(source: bytes) -> str:
    encoded = _nano_base32_encode(source)
    checksum = hashlib.blake2b(source, digest_size=5).digest()[::-1]
    checksum_encoded = _nano_base32_encode(checksum)
    return f"nano_{encoded}{checksum_encoded}"


def decode_nano_address(source: str) -> bytes:
    decoded = _nano_base32_decode(source[5:])
    return decoded[:-5]


nano = CoinCoder(
    name="nano",
    coin_type=165,
    encode=encode_nano_address,
    decode=decode_nano_address,
)

