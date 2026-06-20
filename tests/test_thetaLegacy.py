from __future__ import annotations

import pytest

from address_encoder.coins.thetaLegacy import decode_thetaLegacy_address, encode_thetaLegacy_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('0x314159265dD8dbb310642f98f50C066173C1259b', '314159265dd8dbb310642f98f50c066173c1259b')
])
def test_thetaLegacy_decode(text: str, hex_value: str) -> None:
    assert decode_thetaLegacy_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('0x314159265dD8dbb310642f98f50C066173C1259b', '314159265dd8dbb310642f98f50c066173c1259b')
])
def test_thetaLegacy_encode(expected_text: str, hex_value: str) -> None:
    assert encode_thetaLegacy_address(bytes.fromhex(hex_value)) == expected_text

