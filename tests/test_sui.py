from __future__ import annotations

import pytest

from address_encoder.coins.sui import decode_sui_address, encode_sui_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('0x21dcef5bbc5ec6d1789e8b92d3cb2c4d6855da09bd8197f8b256ca15714a7c47', '21dcef5bbc5ec6d1789e8b92d3cb2c4d6855da09bd8197f8b256ca15714a7c47'),
        ('0x0000000000000000000000000000000000000000000000000000000000000001', '0000000000000000000000000000000000000000000000000000000000000001'),
        ('0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef', '1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef')
])
def test_sui_decode(text: str, hex_value: str) -> None:
    assert decode_sui_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('0x21dcef5bbc5ec6d1789e8b92d3cb2c4d6855da09bd8197f8b256ca15714a7c47', '21dcef5bbc5ec6d1789e8b92d3cb2c4d6855da09bd8197f8b256ca15714a7c47'),
        ('0x0000000000000000000000000000000000000000000000000000000000000001', '0000000000000000000000000000000000000000000000000000000000000001'),
        ('0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef', '1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef')
])
def test_sui_encode(expected_text: str, hex_value: str) -> None:
    assert encode_sui_address(bytes.fromhex(hex_value)) == expected_text

