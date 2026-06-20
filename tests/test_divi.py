from __future__ import annotations

import pytest

from address_encoder.coins.divi import decode_divi_address, encode_divi_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('D8gBQyHPm7A673utQQwBaQcX2Kz91wJovR', '76a91426c95750c1afe443b3351ea5923d5bae09c2a74b88ac'),
        ('DSQvV5yKP5m2tR6uShpt8zmeM8UavPhwfH', '76a914e958e753703fa13eb63b39a92d1f17f06abead5e88ac')
])
def test_divi_decode(text: str, hex_value: str) -> None:
    assert decode_divi_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('D8gBQyHPm7A673utQQwBaQcX2Kz91wJovR', '76a91426c95750c1afe443b3351ea5923d5bae09c2a74b88ac'),
        ('DSQvV5yKP5m2tR6uShpt8zmeM8UavPhwfH', '76a914e958e753703fa13eb63b39a92d1f17f06abead5e88ac')
])
def test_divi_encode(expected_text: str, hex_value: str) -> None:
    assert encode_divi_address(bytes.fromhex(hex_value)) == expected_text

