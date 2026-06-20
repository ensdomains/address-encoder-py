from __future__ import annotations

import pytest

from address_encoder.coins.ttLegacy import decode_ttLegacy_address, encode_ttLegacy_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('0x1001EEc06f2aDff074fC2A9492e132c33d6bd54d', '1001eec06f2adff074fc2a9492e132c33d6bd54d')
])
def test_ttLegacy_decode(text: str, hex_value: str) -> None:
    assert decode_ttLegacy_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('0x1001EEc06f2aDff074fC2A9492e132c33d6bd54d', '1001eec06f2adff074fc2a9492e132c33d6bd54d')
])
def test_ttLegacy_encode(expected_text: str, hex_value: str) -> None:
    assert encode_ttLegacy_address(bytes.fromhex(hex_value)) == expected_text

