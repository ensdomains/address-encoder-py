from __future__ import annotations

import pytest

from address_encoder.coins.celoLegacy import decode_celoLegacy_address, encode_celoLegacy_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('0x67316300f17f063085Ca8bCa4bd3f7a5a3C66275', '67316300f17f063085ca8bca4bd3f7a5a3c66275')
])
def test_celoLegacy_decode(text: str, hex_value: str) -> None:
    assert decode_celoLegacy_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('0x67316300f17f063085Ca8bCa4bd3f7a5a3C66275', '67316300f17f063085ca8bca4bd3f7a5a3c66275')
])
def test_celoLegacy_encode(expected_text: str, hex_value: str) -> None:
    assert encode_celoLegacy_address(bytes.fromhex(hex_value)) == expected_text

