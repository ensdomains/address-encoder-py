from __future__ import annotations

import pytest

from address_encoder.coins.hnt import decode_hnt_address, encode_hnt_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('13M8dUbxymE3xtiAXszRkGMmezMhBS8Li7wEsMojLdb4Sdxc4wc', '01351a71c22fefec2231936ad2826b217ece39d9f77fc6c49639926299c3869295'),
        ('112qB3YaH5bZkCnKA5uRH7tBtGNv2Y5B4smv1jsmvGUzgKT71QpE', '00f11444921875e2ef7435513a1d1f1b0fa49e3242956a24383912ec5d4f194077')
])
def test_hnt_decode(text: str, hex_value: str) -> None:
    assert decode_hnt_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('13M8dUbxymE3xtiAXszRkGMmezMhBS8Li7wEsMojLdb4Sdxc4wc', '01351a71c22fefec2231936ad2826b217ece39d9f77fc6c49639926299c3869295'),
        ('112qB3YaH5bZkCnKA5uRH7tBtGNv2Y5B4smv1jsmvGUzgKT71QpE', '00f11444921875e2ef7435513a1d1f1b0fa49e3242956a24383912ec5d4f194077')
])
def test_hnt_encode(expected_text: str, hex_value: str) -> None:
    assert encode_hnt_address(bytes.fromhex(hex_value)) == expected_text

