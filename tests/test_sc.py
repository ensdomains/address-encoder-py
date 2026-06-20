from __future__ import annotations

import pytest

from address_encoder.coins.sc import decode_sc_address, encode_sc_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('dfb563d6ec6ff876a059fcc96380a6d6718e1a7237e81580123070976243b77988cf8d0b7398', 'dfb563d6ec6ff876a059fcc96380a6d6718e1a7237e81580123070976243b779')
])
def test_sc_decode(text: str, hex_value: str) -> None:
    assert decode_sc_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('dfb563d6ec6ff876a059fcc96380a6d6718e1a7237e81580123070976243b77988cf8d0b7398', 'dfb563d6ec6ff876a059fcc96380a6d6718e1a7237e81580123070976243b779')
])
def test_sc_encode(expected_text: str, hex_value: str) -> None:
    assert encode_sc_address(bytes.fromhex(hex_value)) == expected_text

