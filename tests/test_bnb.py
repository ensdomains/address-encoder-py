from __future__ import annotations

import pytest

from address_encoder.coins.bnb import decode_bnb_address, encode_bnb_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('bnb1grpf0955h0ykzq3ar5nmum7y6gdfl6lxfn46h2', '40c2979694bbc961023d1d27be6fc4d21a9febe6')
])
def test_bnb_decode(text: str, hex_value: str) -> None:
    assert decode_bnb_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('bnb1grpf0955h0ykzq3ar5nmum7y6gdfl6lxfn46h2', '40c2979694bbc961023d1d27be6fc4d21a9febe6')
])
def test_bnb_encode(expected_text: str, hex_value: str) -> None:
    assert encode_bnb_address(bytes.fromhex(hex_value)) == expected_text

