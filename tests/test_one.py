from __future__ import annotations

import pytest

from address_encoder.coins.one import decode_one_address, encode_one_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('one103q7qe5t2505lypvltkqtddaef5tzfxwsse4z7', '7c41e0668b551f4f902cfaec05b5bdca68b124ce')
])
def test_one_decode(text: str, hex_value: str) -> None:
    assert decode_one_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('one103q7qe5t2505lypvltkqtddaef5tzfxwsse4z7', '7c41e0668b551f4f902cfaec05b5bdca68b124ce')
])
def test_one_encode(expected_text: str, hex_value: str) -> None:
    assert encode_one_address(bytes.fromhex(hex_value)) == expected_text

