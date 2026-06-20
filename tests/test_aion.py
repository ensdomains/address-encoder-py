from __future__ import annotations

import pytest

from address_encoder.coins.aion import decode_aion_address, encode_aion_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('0xa0c24fbbecf42184d1ca8e9401ddaa2a99f69f3560e3d6c673de3c8a0be2a8eb', 'a0c24fbbecf42184d1ca8e9401ddaa2a99f69f3560e3d6c673de3c8a0be2a8eb')
])
def test_aion_decode(text: str, hex_value: str) -> None:
    assert decode_aion_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('0xa0c24fbbecf42184d1ca8e9401ddaa2a99f69f3560e3d6c673de3c8a0be2a8eb', 'a0c24fbbecf42184d1ca8e9401ddaa2a99f69f3560e3d6c673de3c8a0be2a8eb')
])
def test_aion_encode(expected_text: str, hex_value: str) -> None:
    assert encode_aion_address(bytes.fromhex(hex_value)) == expected_text

