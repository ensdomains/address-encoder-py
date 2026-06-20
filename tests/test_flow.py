from __future__ import annotations

import pytest

from address_encoder.coins.flow import decode_flow_address, encode_flow_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('0xf233dcee88fe0abe', 'f233dcee88fe0abe')
])
def test_flow_decode(text: str, hex_value: str) -> None:
    assert decode_flow_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('0xf233dcee88fe0abe', 'f233dcee88fe0abe')
])
def test_flow_encode(expected_text: str, hex_value: str) -> None:
    assert encode_flow_address(bytes.fromhex(hex_value)) == expected_text

