from __future__ import annotations

import pytest

from address_encoder.coins.nas import decode_nas_address, encode_nas_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('n1FF1nz6tarkDVwWQkMnnwFPuPKUaQTdptE', '195707f964ff495324635f22c7b486e05d7e67c7af5c'),
        ('n1sLnoc7j57YfzAVP8tJ3yK5a2i56QrTDdK', '195893f59359e3de8ddb7b4e8e9fe51afcf27c59a4c1')
])
def test_nas_decode(text: str, hex_value: str) -> None:
    assert decode_nas_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('n1FF1nz6tarkDVwWQkMnnwFPuPKUaQTdptE', '195707f964ff495324635f22c7b486e05d7e67c7af5c'),
        ('n1sLnoc7j57YfzAVP8tJ3yK5a2i56QrTDdK', '195893f59359e3de8ddb7b4e8e9fe51afcf27c59a4c1')
])
def test_nas_encode(expected_text: str, hex_value: str) -> None:
    assert encode_nas_address(bytes.fromhex(hex_value)) == expected_text

