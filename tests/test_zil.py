from __future__ import annotations

import pytest

from address_encoder.coins.zil import decode_zil_address, encode_zil_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('zil139tkqvc8rw92e6jrs40gawwc3mmdmmauv3x3yz', '89576033071b8aacea43855e8eb9d88ef6ddefbc')
])
def test_zil_decode(text: str, hex_value: str) -> None:
    assert decode_zil_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('zil139tkqvc8rw92e6jrs40gawwc3mmdmmauv3x3yz', '89576033071b8aacea43855e8eb9d88ef6ddefbc')
])
def test_zil_encode(expected_text: str, hex_value: str) -> None:
    assert encode_zil_address(bytes.fromhex(hex_value)) == expected_text

