from __future__ import annotations

from collections.abc import Callable

BECH32_CHARSET = "qpzry9x8gf2tvdw0s3jn54khce6mua7l"
BECH32_GENERATOR = [0x3B6A57B2, 0x26508E6D, 0x1EA119FA, 0x3D4233DD, 0x2A1462B3]
BECH32M_CONST = 0x2BC830A3

Encoder = Callable[[bytes], str]
Decoder = Callable[[str], bytes]


def _polymod(values: list[int]) -> int:
    checksum = 1
    for value in values:
        top = checksum >> 25
        checksum = ((checksum & 0x1FFFFFF) << 5) ^ value
        for index in range(5):
            if (top >> index) & 1:
                checksum ^= BECH32_GENERATOR[index]
    return checksum


def _hrp_expand(hrp: str) -> list[int]:
    return [ord(char) >> 5 for char in hrp] + [0] + [ord(char) & 31 for char in hrp]


def _create_checksum(hrp: str, data: list[int], spec: str) -> list[int]:
    const = 1 if spec == "bech32" else BECH32M_CONST
    values = _hrp_expand(hrp) + data
    polymod = _polymod(values + [0, 0, 0, 0, 0, 0]) ^ const
    return [(polymod >> 5 * (5 - index)) & 31 for index in range(6)]


def _bech32_encode(hrp: str, data: list[int], spec: str = "bech32") -> str:
    combined = data + _create_checksum(hrp, data, spec)
    return hrp + "1" + "".join(BECH32_CHARSET[value] for value in combined)


def _bech32_decode(source: str, spec: str | None = None, limit: int | None = None) -> tuple[str, list[int]]:
    if any(ord(char) < 33 or ord(char) > 126 for char in source):
        raise ValueError("Unrecognised address format")
    lowered = source.lower()
    if source != lowered and source != source.upper():
        raise ValueError("Unrecognised address format")
    source = lowered
    pos = source.rfind("1")
    if pos < 1 or pos + 7 > len(source) or (limit is not None and len(source) > limit):
        raise ValueError("Unrecognised address format")
    hrp = source[:pos]
    data = [BECH32_CHARSET.index(char) for char in source[pos + 1 :]]
    for spec_name in ([spec] if spec else ["bech32", "bech32m"]):
        if _polymod(_hrp_expand(hrp) + data) == (1 if spec_name == "bech32" else BECH32M_CONST):
            return hrp, data[:-6]
    raise ValueError("Unrecognised address format")


def _convert_bits(
    data: list[int] | bytes,
    from_bits: int,
    to_bits: int,
    *,
    pad: bool = True,
) -> list[int]:
    acc = 0
    bits = 0
    result: list[int] = []
    max_value = (1 << to_bits) - 1
    values = list(data)
    for value in values:
        acc = (acc << from_bits) | value
        bits += from_bits
        while bits >= to_bits:
            bits -= to_bits
            result.append((acc >> bits) & max_value)
    if pad:
        if bits:
            result.append((acc << (to_bits - bits)) & max_value)
    elif bits >= from_bits or ((acc << (to_bits - bits)) & max_value):
        raise ValueError("Unrecognised address format")
    return result


def _to_words(data: bytes) -> list[int]:
    return _convert_bits(list(data), 8, 5)


def _from_words(words: list[int]) -> bytes:
    return bytes(_convert_bits(words, 5, 8, pad=False))


def create_plain_bech32_encoder(hrp: str, limit: int | None = None) -> Encoder:
    def encode(source: bytes) -> str:
        encoded = _bech32_encode(hrp, _to_words(source), "bech32")
        if limit is not None and len(encoded) > limit:
            raise ValueError("Unrecognised address format")
        return encoded

    return encode


def create_plain_bech32_decoder(hrp: str, limit: int | None = None) -> Decoder:
    def decode(source: str) -> bytes:
        for spec in ("bech32", "bech32m"):
            try:
                prefix, words = _bech32_decode(source, spec, limit)
            except ValueError:
                continue
            if prefix == hrp:
                return _from_words(words)
        raise ValueError("Unrecognised address format")

    return decode


def create_bech32_encoder(hrp: str, limit: int | None = None) -> Encoder:
    return create_plain_bech32_encoder(hrp, limit)


def create_bech32_decoder(hrp: str, limit: int | None = None) -> Decoder:
    return create_plain_bech32_decoder(hrp, limit)


def create_bech32m_encoder(hrp: str, limit: int | None = None) -> Encoder:
    def encode(source: bytes) -> str:
        encoded = _bech32_encode(hrp, _to_words(source), "bech32m")
        if limit is not None and len(encoded) > limit:
            raise ValueError("Unrecognised address format")
        return encoded

    return encode


def create_bech32m_decoder(hrp: str, limit: int | None = None) -> Decoder:
    def decode(source: str) -> bytes:
        prefix, words = _bech32_decode(source, "bech32m", limit)
        if prefix != hrp:
            raise ValueError("Unexpected human-readable part in bech32 encoded address")
        return _from_words(words)

    return decode


def create_bech32_segwit_encoder(hrp: str) -> Encoder:
    def encode(source: bytes) -> str:
        version = source[0]
        if 0x51 <= version <= 0x60:
            version -= 0x50
        elif version != 0x00:
            raise ValueError("Unrecognised address format")
        payload = source[2 : 2 + source[1]]
        if 0 < version < 17:
            words = [version] + _to_words(payload)
            return _bech32_encode(hrp, words, "bech32m")
        words = [version] + _to_words(payload)
        return _bech32_encode(hrp, words, "bech32")

    return encode


def create_bech32_segwit_decoder(hrp: str) -> Decoder:
    def decode(source: str) -> bytes:
        prefix = None
        words: list[int] = []
        for spec in ("bech32", "bech32m"):
            try:
                prefix, words = _bech32_decode(source, spec)
                break
            except ValueError:
                continue
        if prefix is None:
            raise ValueError("Unrecognised address format")
        if prefix != hrp:
            raise ValueError("Unexpected human-readable part in bech32 encoded address")
        script = _from_words(words[1:])
        version = words[0]
        if version > 0:
            version += 0x50
        return bytes([version, len(script)]) + script

    return decode
