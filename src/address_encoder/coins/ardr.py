from __future__ import annotations

from address_encoder.types import CoinCoder

_PREFIX = "ARDOR"
_ALPHABET = "23456789ABCDEFGHJKLMNPQRSTUVWXYZ"
_CODEWORD_MAP = [3, 2, 1, 0, 7, 6, 5, 4, 13, 14, 15, 16, 12, 8, 9, 10, 11]

_GLOG = [
    0, 0, 1, 18, 2, 5, 19, 11, 3, 29, 6, 27, 20, 8, 12, 23, 4, 10, 30, 17, 7, 22,
    28, 26, 21, 25, 9, 16, 13, 14, 24, 15,
]
_GEXP = [
    1, 2, 4, 8, 16, 5, 10, 20, 13, 26, 17, 7, 14, 28, 29, 31, 27, 19, 3, 6, 12,
    24, 21, 15, 30, 25, 23, 11, 22, 9, 18, 1,
]


def _gmult(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return _GEXP[(_GLOG[a] + _GLOG[b]) % 31]


def _ardr_checksum(source: bytes) -> bool:
    sum_value = 0
    for i in range(1, 5):
        t = 0
        for j in range(31):
            if j > 12 and j < 27:
                continue
            pos = j - 14 if j > 26 else j
            t ^= _gmult(source[pos], _GEXP[(i * j) % 31])
        sum_value |= t
    return sum_value == 0


def encode_ardr_address(source: bytes) -> str:
    chars = [""] * 17
    for index, byte in enumerate(source):
        write_index = _CODEWORD_MAP[index]
        chars[write_index] = _ALPHABET[16 * ((byte & 0xF0) >> 4) + (byte & 0x0F)]
    return (
        f"{_PREFIX}-{''.join(chars[0:4])}-{''.join(chars[4:8])}-"
        f"{''.join(chars[8:12])}-{''.join(chars[12:17])}"
    )


def decode_ardr_address(source: str) -> bytes:
    if not source.startswith(f"{_PREFIX}-") or len(source) != 26:
        raise ValueError("Unrecognised address format")

    joined = source[6:]
    codeword = bytearray([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    j = 0
    for i in range(20):
        char = joined[i]
        if char == "-":
            continue
        pos = _ALPHABET.index(char)
        write_index = _CODEWORD_MAP[j]
        j += 1
        codeword[write_index] = pos

    if not _ardr_checksum(bytes(codeword)):
        raise ValueError("Unrecognised address format")

    return bytes(codeword)


ardr = CoinCoder(
    name="ardr",
    coin_type=16754,
    encode=encode_ardr_address,
    decode=decode_ardr_address,
)

