from __future__ import annotations

import pytest

from address_encoder.coins.sys import decode_sys_address, encode_sys_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('SVoQzrfQpoiYsrHMXvwbgeJZooqw8zPF9Q', '76a9145d5113254a2fb792d209b2731b7c05ee9441aa9088ac'),
        ('SdQRVkLTiYCA75o4hE4TMjMCJL8CytF31G', '76a914b0b8ee03d302db1bd6ef689a73de764e3157909588ac'),
        ('sys1q42jdpqq4369ze73rskkrncplcv7mtejhdkxj90', '0014aaa4d080158e8a2cfa2385ac39e03fc33db5e657'),
        ('sys1qlfz9tcds52ajh25v2a85ur22rt2mm488twvs5l', '0014fa4455e1b0a2bb2baa8c574f4e0d4a1ad5bdd4e7')
])
def test_sys_decode(text: str, hex_value: str) -> None:
    assert decode_sys_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('SVoQzrfQpoiYsrHMXvwbgeJZooqw8zPF9Q', '76a9145d5113254a2fb792d209b2731b7c05ee9441aa9088ac'),
        ('SdQRVkLTiYCA75o4hE4TMjMCJL8CytF31G', '76a914b0b8ee03d302db1bd6ef689a73de764e3157909588ac'),
        ('sys1q42jdpqq4369ze73rskkrncplcv7mtejhdkxj90', '0014aaa4d080158e8a2cfa2385ac39e03fc33db5e657'),
        ('sys1qlfz9tcds52ajh25v2a85ur22rt2mm488twvs5l', '0014fa4455e1b0a2bb2baa8c574f4e0d4a1ad5bdd4e7')
])
def test_sys_encode(expected_text: str, hex_value: str) -> None:
    assert encode_sys_address(bytes.fromhex(hex_value)) == expected_text

