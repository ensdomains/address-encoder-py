from __future__ import annotations

import pytest

from address_encoder.coins.ela import decode_ela_address, encode_ela_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('EQDZ4T6YyVkg9mb2cAuLEu8iBKbajQAywF', '214d797cc92303dac242b17026e79bbea28eb642f29f0d3582')
])
def test_ela_decode(text: str, hex_value: str) -> None:
    assert decode_ela_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('EQDZ4T6YyVkg9mb2cAuLEu8iBKbajQAywF', '214d797cc92303dac242b17026e79bbea28eb642f29f0d3582')
])
def test_ela_encode(expected_text: str, hex_value: str) -> None:
    assert encode_ela_address(bytes.fromhex(hex_value)) == expected_text

