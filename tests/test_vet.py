from __future__ import annotations

import pytest

from address_encoder.coins.vet import decode_vet_address, encode_vet_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('0x9760b32C0A515F6C8c4E6B7B89AF8964DDaCB985', '9760b32c0a515f6c8c4e6b7b89af8964ddacb985')
])
def test_vet_decode(text: str, hex_value: str) -> None:
    assert decode_vet_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('0x9760b32C0A515F6C8c4E6B7B89AF8964DDaCB985', '9760b32c0a515f6c8c4e6b7b89af8964ddacb985')
])
def test_vet_encode(expected_text: str, hex_value: str) -> None:
    assert encode_vet_address(bytes.fromhex(hex_value)) == expected_text

