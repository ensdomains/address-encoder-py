from __future__ import annotations

import pytest

from address_encoder.coins.xvg import decode_xvg_address, encode_xvg_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('D7MKQnLxXEqn84PN42jWAVhvrXEuULLV9r', '76a914183ffcc41f3095bea7ff324e52a65b46c74126e188ac')
])
def test_xvg_decode(text: str, hex_value: str) -> None:
    assert decode_xvg_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('D7MKQnLxXEqn84PN42jWAVhvrXEuULLV9r', '76a914183ffcc41f3095bea7ff324e52a65b46c74126e188ac')
])
def test_xvg_encode(expected_text: str, hex_value: str) -> None:
    assert encode_xvg_address(bytes.fromhex(hex_value)) == expected_text

