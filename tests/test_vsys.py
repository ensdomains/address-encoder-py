from __future__ import annotations

import pytest

from address_encoder.coins.vsys import decode_vsys_address, encode_vsys_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('ARF12jvtjz9caUFmiwBeRe1SPRGQhUWKrtd', '054d878288c4d4e2dd250560e303476b2152703557a0d3aa3396')
])
def test_vsys_decode(text: str, hex_value: str) -> None:
    assert decode_vsys_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('ARF12jvtjz9caUFmiwBeRe1SPRGQhUWKrtd', '054d878288c4d4e2dd250560e303476b2152703557a0d3aa3396')
])
def test_vsys_encode(expected_text: str, hex_value: str) -> None:
    assert encode_vsys_address(bytes.fromhex(hex_value)) == expected_text

