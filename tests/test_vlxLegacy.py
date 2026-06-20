from __future__ import annotations

import pytest

from address_encoder.coins.vlxLegacy import decode_vlxLegacy_address, encode_vlxLegacy_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('VDTHiswjSTkLFbfh2S5XFsqkLzC11HoBD6', '461ea68e5e13c72abf1bd2f0bcae4650521712cdb76276f0d5')
])
def test_vlxLegacy_decode(text: str, hex_value: str) -> None:
    assert decode_vlxLegacy_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('VDTHiswjSTkLFbfh2S5XFsqkLzC11HoBD6', '461ea68e5e13c72abf1bd2f0bcae4650521712cdb76276f0d5')
])
def test_vlxLegacy_encode(expected_text: str, hex_value: str) -> None:
    assert encode_vlxLegacy_address(bytes.fromhex(hex_value)) == expected_text

