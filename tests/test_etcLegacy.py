from __future__ import annotations

import pytest

from address_encoder.coins.etcLegacy import decode_etcLegacy_address, encode_etcLegacy_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('0x314159265dD8dbb310642f98f50C066173C1259b', '314159265dd8dbb310642f98f50c066173c1259b')
])
def test_etcLegacy_decode(text: str, hex_value: str) -> None:
    assert decode_etcLegacy_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('0x314159265dD8dbb310642f98f50C066173C1259b', '314159265dd8dbb310642f98f50c066173c1259b')
])
def test_etcLegacy_encode(expected_text: str, hex_value: str) -> None:
    assert encode_etcLegacy_address(bytes.fromhex(hex_value)) == expected_text

