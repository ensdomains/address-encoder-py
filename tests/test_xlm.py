from __future__ import annotations

import pytest

from address_encoder.coins.xlm import decode_xlm_address, encode_xlm_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('GAI3GJ2Q3B35AOZJ36C4ANE3HSS4NK7WI6DNO4ZSHRAX6NG7BMX6VJER', '11b32750d877d03b29df85c0349b3ca5c6abf64786d773323c417f34df0b2fea')
])
def test_xlm_decode(text: str, hex_value: str) -> None:
    assert decode_xlm_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('GAI3GJ2Q3B35AOZJ36C4ANE3HSS4NK7WI6DNO4ZSHRAX6NG7BMX6VJER', '11b32750d877d03b29df85c0349b3ca5c6abf64786d773323c417f34df0b2fea')
])
def test_xlm_encode(expected_text: str, hex_value: str) -> None:
    assert encode_xlm_address(bytes.fromhex(hex_value)) == expected_text

