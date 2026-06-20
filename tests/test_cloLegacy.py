from __future__ import annotations

import pytest

from address_encoder.coins.cloLegacy import decode_cloLegacy_address, encode_cloLegacy_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('0x5aAeb6053F3E94C9b9A09f33669435E7Ef1BeAed', '5aaeb6053f3e94c9b9a09f33669435e7ef1beaed')
])
def test_cloLegacy_decode(text: str, hex_value: str) -> None:
    assert decode_cloLegacy_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('0x5aAeb6053F3E94C9b9A09f33669435E7Ef1BeAed', '5aaeb6053f3e94c9b9a09f33669435e7ef1beaed')
])
def test_cloLegacy_encode(expected_text: str, hex_value: str) -> None:
    assert encode_cloLegacy_address(bytes.fromhex(hex_value)) == expected_text

