from __future__ import annotations

import pytest

from address_encoder.coins.ewtLegacy import decode_ewtLegacy_address, encode_ewtLegacy_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('0x2ce42c2B3aCff7eddcfd32DCB0703F1870b0eBe1', '2ce42c2b3acff7eddcfd32dcb0703f1870b0ebe1')
])
def test_ewtLegacy_decode(text: str, hex_value: str) -> None:
    assert decode_ewtLegacy_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('0x2ce42c2B3aCff7eddcfd32DCB0703F1870b0eBe1', '2ce42c2b3acff7eddcfd32dcb0703f1870b0ebe1')
])
def test_ewtLegacy_encode(expected_text: str, hex_value: str) -> None:
    assert encode_ewtLegacy_address(bytes.fromhex(hex_value)) == expected_text

