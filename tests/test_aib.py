from __future__ import annotations

import pytest

from address_encoder.coins.aib import decode_aib_address, encode_aib_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('AJc4bPnvyvdUhFqaGLB8hhiAPyJdcZvs4Z', '76a9141f0d5afac97c916cdaccc0dd1c41cb03fde8452f88ac')
])
def test_aib_decode(text: str, hex_value: str) -> None:
    assert decode_aib_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('AJc4bPnvyvdUhFqaGLB8hhiAPyJdcZvs4Z', '76a9141f0d5afac97c916cdaccc0dd1c41cb03fde8452f88ac')
])
def test_aib_encode(expected_text: str, hex_value: str) -> None:
    assert encode_aib_address(bytes.fromhex(hex_value)) == expected_text

