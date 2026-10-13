from __future__ import annotations

import pytest

from address_encoder.utils.bytes_ import hex_to_bytes, hex_without_prefix_to_bytes


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", b""),
        ("00", b"\x00"),
        ("beef", b"\xbe\xef"),
        ("DeAdBeEf", b"\xde\xad\xbe\xef"),
    ],
)
def test_hex_without_prefix_to_bytes(text: str, expected: bytes) -> None:
    assert hex_without_prefix_to_bytes(text) == expected


@pytest.mark.parametrize(
    "text",
    [
        "0xbeef",
        "abc",
        "zz",
        "be ef",
        " beef",
        "beef\n",
        "be_ef",
    ],
)
def test_hex_without_prefix_to_bytes_rejects_invalid(text: str) -> None:
    with pytest.raises(ValueError):
        hex_without_prefix_to_bytes(text)


def test_hex_to_bytes_is_unchanged() -> None:
    assert hex_to_bytes("0xbeef") == b"\xbe\xef"
    assert hex_to_bytes("0xabc") == b"\x0a\xbc"
