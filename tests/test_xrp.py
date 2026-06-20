from __future__ import annotations

import pytest

from address_encoder.coins.xrp import decode_xrp_address, encode_xrp_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('rf1BiGeXwwQoi8Z2ueFYTEXSwuJYfV2Jpn', '004b4e9c06f24296074f7bc48f92a97916c6dc5ea9'),
        ('X7qvLs7gSnNoKvZzNWUT2e8st17QPY64PPe7zriLNuJszeg', '05444b4e9c06f24296074f7bc48f92a97916c6dc5ea9000000000000000000')
])
def test_xrp_decode(text: str, hex_value: str) -> None:
    assert decode_xrp_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('rf1BiGeXwwQoi8Z2ueFYTEXSwuJYfV2Jpn', '004b4e9c06f24296074f7bc48f92a97916c6dc5ea9'),
        ('X7qvLs7gSnNoKvZzNWUT2e8st17QPY64PPe7zriLNuJszeg', '05444b4e9c06f24296074f7bc48f92a97916c6dc5ea9000000000000000000')
])
def test_xrp_encode(expected_text: str, hex_value: str) -> None:
    assert encode_xrp_address(bytes.fromhex(hex_value)) == expected_text

