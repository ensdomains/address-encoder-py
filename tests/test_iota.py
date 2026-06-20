from __future__ import annotations

import pytest

from address_encoder.coins.iota import decode_iota_address, encode_iota_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('iota1qpw6k49dedaxrt854rau02talgfshgt0jlm5w8x9nk5ts6f5x5m759nh2ml', '5dab54adcb7a61acf4a8fbc7a97dfa130ba16f97f7471cc59da8b869343537ea'),
        ('iota1qrhacyfwlcnzkvzteumekfkrrwks98mpdm37cj4xx3drvmjvnep6xqgyzyx', 'efdc112efe262b304bcf379b26c31bad029f616ee3ec4aa6345a366e4c9e43a3')
])
def test_iota_decode(text: str, hex_value: str) -> None:
    assert decode_iota_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('iota1qpw6k49dedaxrt854rau02talgfshgt0jlm5w8x9nk5ts6f5x5m759nh2ml', '5dab54adcb7a61acf4a8fbc7a97dfa130ba16f97f7471cc59da8b869343537ea'),
        ('iota1qrhacyfwlcnzkvzteumekfkrrwks98mpdm37cj4xx3drvmjvnep6xqgyzyx', 'efdc112efe262b304bcf379b26c31bad029f616ee3ec4aa6345a366e4c9e43a3')
])
def test_iota_encode(expected_text: str, hex_value: str) -> None:
    assert encode_iota_address(bytes.fromhex(hex_value)) == expected_text

