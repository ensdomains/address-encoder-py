from __future__ import annotations

import pytest

from address_encoder.coins.ar import decode_ar_address, encode_ar_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('GRQ7swQO1AMyFgnuAPI7AvGQlW3lzuQuwlJbIpWV7xk', '19143bb3040ed403321609ee00f23b02f190956de5cee42ec2525b229595ef19')
])
def test_ar_decode(text: str, hex_value: str) -> None:
    assert decode_ar_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('GRQ7swQO1AMyFgnuAPI7AvGQlW3lzuQuwlJbIpWV7xk', '19143bb3040ed403321609ee00f23b02f190956de5cee42ec2525b229595ef19')
])
def test_ar_encode(expected_text: str, hex_value: str) -> None:
    assert encode_ar_address(bytes.fromhex(hex_value)) == expected_text

