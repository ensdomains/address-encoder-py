from __future__ import annotations

import pytest

from address_encoder.coins.wan import decode_wan_address, encode_wan_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('0x2eF088E183231C9bEA30d8430937D3A57b7327D4', '2ef088e183231c9bea30d8430937d3a57b7327d4')
])
def test_wan_decode(text: str, hex_value: str) -> None:
    assert decode_wan_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('0x2eF088E183231C9bEA30d8430937D3A57b7327D4', '2ef088e183231c9bea30d8430937d3a57b7327d4')
])
def test_wan_encode(expected_text: str, hex_value: str) -> None:
    assert encode_wan_address(bytes.fromhex(hex_value)) == expected_text

