from __future__ import annotations

import pytest

from address_encoder.coins.dot import decode_dot_address, encode_dot_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('1FRMM8PEiWXYax7rpS6X4XZX1aAAxSWx1CrKTyrVYhV24fg', '0aff6865635ae11013a83835c019d44ec3f865145943f487ae82a8e7bed3a66b')
])
def test_dot_decode(text: str, hex_value: str) -> None:
    assert decode_dot_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('1FRMM8PEiWXYax7rpS6X4XZX1aAAxSWx1CrKTyrVYhV24fg', '0aff6865635ae11013a83835c019d44ec3f865145943f487ae82a8e7bed3a66b')
])
def test_dot_encode(expected_text: str, hex_value: str) -> None:
    assert encode_dot_address(bytes.fromhex(hex_value)) == expected_text

