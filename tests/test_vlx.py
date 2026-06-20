from __future__ import annotations

import pytest

from address_encoder.coins.vlx import decode_vlx_address, encode_vlx_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('VDTHiswjSTkLFbfh2S5XFsqkLzC11HoBD6', '461ea68e5e13c72abf1bd2f0bcae4650521712cdb76276f0d5')
])
def test_vlx_decode(text: str, hex_value: str) -> None:
    assert decode_vlx_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('VDTHiswjSTkLFbfh2S5XFsqkLzC11HoBD6', '461ea68e5e13c72abf1bd2f0bcae4650521712cdb76276f0d5')
])
def test_vlx_encode(expected_text: str, hex_value: str) -> None:
    assert encode_vlx_address(bytes.fromhex(hex_value)) == expected_text

