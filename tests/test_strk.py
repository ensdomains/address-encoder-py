from __future__ import annotations

import pytest

from address_encoder.coins.strk import decode_strk_address, encode_strk_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('0x02Fd23d9182193775423497fc0c472E156C57C69E4089A1967fb288A2d84e914', '02fd23d9182193775423497fc0c472e156c57c69e4089a1967fb288a2d84e914')
])
def test_strk_decode(text: str, hex_value: str) -> None:
    assert decode_strk_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('0x02Fd23d9182193775423497fc0c472E156C57C69E4089A1967fb288A2d84e914', '02fd23d9182193775423497fc0c472e156c57c69e4089a1967fb288a2d84e914')
])
def test_strk_encode(expected_text: str, hex_value: str) -> None:
    assert encode_strk_address(bytes.fromhex(hex_value)) == expected_text

