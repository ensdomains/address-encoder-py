from __future__ import annotations

import pytest

from address_encoder.coins.ardr import decode_ardr_address, encode_ardr_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('ARDOR-MT4P-AHG4-A4NA-CCMM2', '15021913020e0f080a1313000a08021408')
])
def test_ardr_decode(text: str, hex_value: str) -> None:
    assert decode_ardr_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('ARDOR-MT4P-AHG4-A4NA-CCMM2', '15021913020e0f080a1313000a08021408')
])
def test_ardr_encode(expected_text: str, hex_value: str) -> None:
    assert encode_ardr_address(bytes.fromhex(hex_value)) == expected_text

