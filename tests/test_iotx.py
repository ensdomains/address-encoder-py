from __future__ import annotations

import pytest

from address_encoder.coins.iotx import decode_iotx_address, encode_iotx_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('io1nyjs526mnqcsx4twa7nptkg08eclsw5c2dywp4', '99250a2b5b983103556eefa615d90f3e71f83a98')
])
def test_iotx_decode(text: str, hex_value: str) -> None:
    assert decode_iotx_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('io1nyjs526mnqcsx4twa7nptkg08eclsw5c2dywp4', '99250a2b5b983103556eefa615d90f3e71f83a98')
])
def test_iotx_encode(expected_text: str, hex_value: str) -> None:
    assert encode_iotx_address(bytes.fromhex(hex_value)) == expected_text

