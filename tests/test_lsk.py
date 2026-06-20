from __future__ import annotations

import pytest

from address_encoder.coins.lsk import decode_lsk_address, encode_lsk_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('5506432865724830000L', '4c6ac7845d109130'),
        ('10588416556841527004L', '92f19cc2346766dc'),
        ('4980451641598555896L', '451e1e61667e36f8')
])
def test_lsk_decode(text: str, hex_value: str) -> None:
    assert decode_lsk_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('5506432865724830000L', '4c6ac7845d109130'),
        ('10588416556841527004L', '92f19cc2346766dc'),
        ('4980451641598555896L', '451e1e61667e36f8')
])
def test_lsk_encode(expected_text: str, hex_value: str) -> None:
    assert encode_lsk_address(bytes.fromhex(hex_value)) == expected_text

