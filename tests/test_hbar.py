from __future__ import annotations

import pytest

from address_encoder.coins.hbar import decode_hbar_address, encode_hbar_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('255.255.1024', '000000ff00000000000000ff0000000000000400')
])
def test_hbar_decode(text: str, hex_value: str) -> None:
    assert decode_hbar_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('255.255.1024', '000000ff00000000000000ff0000000000000400')
])
def test_hbar_encode(expected_text: str, hex_value: str) -> None:
    assert encode_hbar_address(bytes.fromhex(hex_value)) == expected_text

