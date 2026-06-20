from __future__ import annotations

import pytest

from address_encoder.coins.algo import decode_algo_address, encode_algo_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('7777777777777777777777777777777777777777777777777774MSJUVU', 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'),
        ('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAY5HFKQ', '0000000000000000000000000000000000000000000000000000000000000000')
])
def test_algo_decode(text: str, hex_value: str) -> None:
    assert decode_algo_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('7777777777777777777777777777777777777777777777777774MSJUVU', 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'),
        ('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAY5HFKQ', '0000000000000000000000000000000000000000000000000000000000000000')
])
def test_algo_encode(expected_text: str, hex_value: str) -> None:
    assert encode_algo_address(bytes.fromhex(hex_value)) == expected_text

