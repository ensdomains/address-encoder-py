from __future__ import annotations

PREFIX = "bitcoincash"
PREFIX_BYTES = bytes([2, 9, 20, 3, 15, 9, 14, 3, 1, 19, 8, 0])
HASH_SIZE = [160, 192, 224, 256, 320, 384, 448, 512]
HASH_SIZE_LOOKUP = {size: index for index, size in enumerate(HASH_SIZE)}
BCH_CHARSET = "qpzry9x8gf2tvdw0s3jn54khce6mua7l"
GENERATOR = [0x98F2BC8E61, 0x79B76D99E2, 0xF33E5FB3C4, 0xAE2EABE2A8, 0x1E4F43E470]


def _polymod(data: bytes) -> int:
    checksum = 1
    for value in data:
        top_bits = checksum >> 35
        checksum = ((checksum & 0x07FFFFFFFF) << 5) ^ value
        for index, generator in enumerate(GENERATOR):
            if (top_bits >> index) & 1:
                checksum ^= generator
    return checksum ^ 1


def _convert_bits(data: list[int], from_bits: int, to_bits: int, *, pad: bool = False) -> list[int]:
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
    if bits > 0:
        if pad:
            result.append((acc << (to_bits - bits)) & max_value)
        elif (acc & ((1 << bits) - 1)) != 0:
            raise ValueError("Non-zero padding")
    return result


def _radix5_encode(data: bytes) -> list[int]:
    return _convert_bits(list(data), 8, 5, pad=True)


def _radix5_decode(data: list[int]) -> list[int]:
    return _convert_bits(data, 5, 8, pad=False)


def _bch_base32_encode(payload: list[int]) -> str:
    return "".join(BCH_CHARSET[value] for value in payload)


def _bch_base32_decode(payload: str) -> list[int]:
    return [BCH_CHARSET.index(char) for char in payload]


def _checksum_to_uint5_array(checksum: int) -> bytes:
    result = bytearray(8)
    for index in range(8):
        result[7 - index] = checksum & 31
        checksum >>= 5
    return bytes(result)


def _normalise_bch_address(value: str) -> str:
    lowercased = value.lower()
    if value == lowercased:
        return lowercased
    uppercased = value.upper()
    if value == uppercased:
        return lowercased
    raise ValueError("Unrecognised address format")


def _is_checksum_valid(source: list[int]) -> bool:
    return _polymod(PREFIX_BYTES + bytes(source)) == 0


def encode_bch_address_with_version(version: int, source: bytes) -> str:
    version_byte = bytes([version + HASH_SIZE_LOOKUP[len(source) * 8]])
    radix5_encoded = _radix5_encode(version_byte + source)
    payload_data = list(radix5_encoded)
    checksum_data = PREFIX_BYTES + bytes(payload_data) + bytes(8)
    checksum = _checksum_to_uint5_array(_polymod(checksum_data))
    payload = payload_data + list(checksum)
    return f"{PREFIX}:{_bch_base32_encode(payload)}"


def decode_bch_address_to_type_and_hash(source: str) -> tuple[int, bytes]:
    normalised = _normalise_bch_address(source)
    if ":" in normalised:
        prefix, payload = normalised.split(":", 1)
        if prefix != PREFIX:
            raise ValueError("Unrecognised address format")
    else:
        payload = normalised
    base32_decoded = _bch_base32_decode(payload)
    if not _is_checksum_valid(base32_decoded):
        raise ValueError("Invalid checksum")
    version_byte, *hash_bytes = _radix5_decode(base32_decoded[:-8])
    if HASH_SIZE[version_byte & 7] != len(hash_bytes) * 8:
        raise ValueError("Unrecognised address format")
    return version_byte & 120, bytes(hash_bytes)
