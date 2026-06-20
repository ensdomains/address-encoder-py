from __future__ import annotations

import pytest

from address_encoder.coins.tfuel import decode_tfuel_address, encode_tfuel_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('0x3599CF49e80A01BCb879A19599C8a6cd8C8d9aa6', '3599cf49e80a01bcb879a19599c8a6cd8c8d9aa6')
])
def test_tfuel_decode(text: str, hex_value: str) -> None:
    assert decode_tfuel_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('0x3599CF49e80A01BCb879A19599C8a6cd8C8d9aa6', '3599cf49e80a01bcb879a19599c8a6cd8c8d9aa6')
])
def test_tfuel_encode(expected_text: str, hex_value: str) -> None:
    assert encode_tfuel_address(bytes.fromhex(hex_value)) == expected_text

