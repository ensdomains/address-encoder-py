from __future__ import annotations

import cbor2
import pytest

from address_encoder.utils.base58_ import base58_unchecked_encode
from address_encoder.utils.byron import byron_decode, byron_encode
from address_encoder.utils.crc32 import crc32

ADDRESS = bytes.fromhex("83581cba970ad36654d8dd8f74274b733452ddeab9a62a397746be3c42ccdda000")
TEXT = "Ae2tdPwUPEZFRbyhz3cpfC2CumGzNkFBN2L42rcUc2yjQpEkxDbkPodpMAi"


def _encode_cbor(value: object) -> str:
    return base58_unchecked_encode(cbor2.dumps(value))


def test_byron_round_trip() -> None:
    assert byron_encode(ADDRESS) == TEXT
    assert byron_decode(TEXT) == ADDRESS


# Truncated inputs from the upstream cborDecode() regression tests
@pytest.mark.parametrize(
    "data",
    [
        [],
        [0xBF],
        [0x9F],
        [0x5F],
        [0x7F],
        [0xBF, 0x01],
        [0xA1, 0x01],
        [0x81],
        [0x18],
        [0x19, 0x00],
        [0x1A, 0x00],
        [0x1B, 0x00],
        [0xFA, 0x00],
        [0xFB, 0x00],
        [0x41],
        [0x61],
        [0x61, 0xC2, 0xA2],
        [0x7F, 0x61, 0xC2, 0xA2, 0xFF],
        [0x9B, 0x00, 0x20, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    ],
)
def test_byron_rejects_truncated_cbor(data: list[int]) -> None:
    with pytest.raises(ValueError, match="Unrecognised address format"):
        byron_decode(base58_unchecked_encode(bytes(data)))


@pytest.mark.parametrize(
    "value",
    [
        5,
        {0: 1, 1: 2},
        [],
        [cbor2.CBORTag(24, ADDRESS)],
        [ADDRESS, crc32(ADDRESS)],
        [cbor2.CBORTag(24, ADDRESS), crc32(ADDRESS), 0],
        [cbor2.CBORTag(100, ADDRESS), crc32(ADDRESS)],
        [cbor2.CBORTag(24, 5), 0],
        [cbor2.CBORTag(24, "text"), 0],
        [cbor2.CBORTag(24, ADDRESS), crc32(ADDRESS) + 1],
        [cbor2.CBORTag(24, ADDRESS), str(crc32(ADDRESS))],
    ],
)
def test_byron_rejects_malformed_structure(value: object) -> None:
    with pytest.raises(ValueError, match="Unrecognised address format"):
        byron_decode(_encode_cbor(value))


def test_byron_rejects_trailing_bytes() -> None:
    data = cbor2.dumps([cbor2.CBORTag(24, ADDRESS), crc32(ADDRESS)]) + b"\x00"
    with pytest.raises(ValueError, match="Unrecognised address format"):
        byron_decode(base58_unchecked_encode(data))
