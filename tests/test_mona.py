from __future__ import annotations

import pytest

from address_encoder.coins.mona import decode_mona_address, encode_mona_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('MHxgS2XMXjeJ4if2PRRbWYcdwZPWfdwaDT', '76a9146e5bb7226a337fe8307b4192ae5c3fab9fa9edf588ac'),
        ('PHjTKtgYLTJ9D2Bzw2f6xBB41KBm2HeGfg', 'a9146449f568c9cd2378138f2636e1567112a184a9e887'),
        ('mona1zw508d6qejxtdg4y5r3zarvaryvz8pq8u', '5210751e76e8199196d454941c45d1b3a323')
])
def test_mona_decode(text: str, hex_value: str) -> None:
    assert decode_mona_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('MHxgS2XMXjeJ4if2PRRbWYcdwZPWfdwaDT', '76a9146e5bb7226a337fe8307b4192ae5c3fab9fa9edf588ac'),
        ('PHjTKtgYLTJ9D2Bzw2f6xBB41KBm2HeGfg', 'a9146449f568c9cd2378138f2636e1567112a184a9e887'),
        ('mona1zw508d6qejxtdg4y5r3zarvaryvz8pq8u', '5210751e76e8199196d454941c45d1b3a323')
])
def test_mona_encode(expected_text: str, hex_value: str) -> None:
    assert encode_mona_address(bytes.fromhex(hex_value)) == expected_text

