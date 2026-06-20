from __future__ import annotations

import pytest

from address_encoder.coins.ark import decode_ark_address, encode_ark_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('AKkCgA5To85YSAgJgxUw8dKJsHkCzsu2dy', '172b8f8e3490db00c6cc0dda2d2b9626e681500e29')
])
def test_ark_decode(text: str, hex_value: str) -> None:
    assert decode_ark_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('AKkCgA5To85YSAgJgxUw8dKJsHkCzsu2dy', '172b8f8e3490db00c6cc0dda2d2b9626e681500e29')
])
def test_ark_encode(expected_text: str, hex_value: str) -> None:
    assert encode_ark_address(bytes.fromhex(hex_value)) == expected_text

