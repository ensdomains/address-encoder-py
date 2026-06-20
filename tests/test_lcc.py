from __future__ import annotations

import pytest

from address_encoder.coins.lcc import decode_lcc_address, encode_lcc_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('CJkeBGuySxGcdY1wupo7FXT1h8bbv4zFHt', '76a914191b4f0395e2e66c9c1d9ab5e77a3455acf2c67188ac'),
        ('MV5hqZU1rNDZ4fubL3Jpc7GMDGHmaVtreg', 'a914e8592f26abbbc754209ae58b131d54312a313b5787'),
        ('lcc1q45yjegxencjtxslypllvyqfz0xk77mdklxzrcr', '0014ad092ca0d99e24b343e40ffec2012279adef6db6')
])
def test_lcc_decode(text: str, hex_value: str) -> None:
    assert decode_lcc_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('CJkeBGuySxGcdY1wupo7FXT1h8bbv4zFHt', '76a914191b4f0395e2e66c9c1d9ab5e77a3455acf2c67188ac'),
        ('MV5hqZU1rNDZ4fubL3Jpc7GMDGHmaVtreg', 'a914e8592f26abbbc754209ae58b131d54312a313b5787'),
        ('lcc1q45yjegxencjtxslypllvyqfz0xk77mdklxzrcr', '0014ad092ca0d99e24b343e40ffec2012279adef6db6')
])
def test_lcc_encode(expected_text: str, hex_value: str) -> None:
    assert encode_lcc_address(bytes.fromhex(hex_value)) == expected_text

