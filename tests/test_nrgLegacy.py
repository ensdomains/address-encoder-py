from __future__ import annotations

import pytest

from address_encoder.coins.nrgLegacy import decode_nrgLegacy_address, encode_nrgLegacy_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('0x7e534bc64A80e56dB3eEDBd1b54639C3A9a7CDEA', '7e534bc64a80e56db3eedbd1b54639c3a9a7cdea')
])
def test_nrgLegacy_decode(text: str, hex_value: str) -> None:
    assert decode_nrgLegacy_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('0x7e534bc64A80e56dB3eEDBd1b54639C3A9a7CDEA', '7e534bc64a80e56db3eedbd1b54639c3a9a7cdea')
])
def test_nrgLegacy_encode(expected_text: str, hex_value: str) -> None:
    assert encode_nrgLegacy_address(bytes.fromhex(hex_value)) == expected_text

