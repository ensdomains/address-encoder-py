from __future__ import annotations

import pytest

from address_encoder.coins.dcr import decode_dcr_address, encode_dcr_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('DsnBFk2BdqYP3WEmChpL7TSonhpxUAi8wiA', '073fe8b089c48ba23c60c64c5226d47acfb26565e313934d5d73')
])
def test_dcr_decode(text: str, hex_value: str) -> None:
    assert decode_dcr_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('DsnBFk2BdqYP3WEmChpL7TSonhpxUAi8wiA', '073fe8b089c48ba23c60c64c5226d47acfb26565e313934d5d73')
])
def test_dcr_encode(expected_text: str, hex_value: str) -> None:
    assert encode_dcr_address(bytes.fromhex(hex_value)) == expected_text

