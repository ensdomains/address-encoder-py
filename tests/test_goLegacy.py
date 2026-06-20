from __future__ import annotations

import pytest

from address_encoder.coins.goLegacy import decode_goLegacy_address, encode_goLegacy_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('0x314159265dD8dbb310642f98f50C066173C1259b', '314159265dd8dbb310642f98f50c066173c1259b')
])
def test_goLegacy_decode(text: str, hex_value: str) -> None:
    assert decode_goLegacy_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('0x314159265dD8dbb310642f98f50C066173C1259b', '314159265dd8dbb310642f98f50c066173c1259b')
])
def test_goLegacy_encode(expected_text: str, hex_value: str) -> None:
    assert encode_goLegacy_address(bytes.fromhex(hex_value)) == expected_text

