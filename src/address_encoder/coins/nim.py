from __future__ import annotations

from address_encoder.types import CoinCoder

_CCODE = "NQ"
_NIM_ALPHABET = "0123456789ABCDEFGHJKLMNPQRSTUVXY"


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


def _nim_base32_encode(source: bytes) -> str:
    values = _convert_bits(list(source), 8, 5, pad=True)
    return "".join(_NIM_ALPHABET[value] for value in values)


def _nim_base32_decode(source: str) -> bytes:
    values = [_NIM_ALPHABET.index(char) for char in source]
    return bytes(_convert_bits(values, 5, 8, pad=False))


def _iban_check(data: str) -> int:
    num = "".join(char if char.isdigit() else str(ord(char) - 55) for char in data.upper())
    tmp = ""
    for index in range((len(num) + 5) // 6):
        chunk = num[index * 6 : index * 6 + 6]
        tmp = str(int(tmp + chunk) % 97)
    return int(tmp)


def _nim_checksum(source: str) -> str:
    return f"{98 - _iban_check(source + _CCODE + '00'):02d}"[-2:]


def encode_nim_address(source: bytes) -> str:
    base32_part = _nim_base32_encode(source)
    checksummed = _nim_checksum(base32_part)
    spaced = f"{_CCODE}{checksummed}{base32_part}"
    return " ".join(spaced[index : index + 4] for index in range(0, len(spaced), 4))


def decode_nim_address(source: str) -> bytes:
    if not source.startswith(_CCODE):
        raise ValueError("Unrecognised address format")
    no_whitespace = source.replace(" ", "")
    checksum = no_whitespace[2:4]
    base32_part = no_whitespace[4:]
    if checksum != _nim_checksum(base32_part):
        raise ValueError("Unrecognised address format")
    return _nim_base32_decode(base32_part)


nim = CoinCoder(
    name="nim",
    coin_type=242,
    encode=encode_nim_address,
    decode=decode_nim_address,
)

