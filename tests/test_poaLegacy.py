from __future__ import annotations

import pytest

from address_encoder.coins.poaLegacy import decode_poaLegacy_address, encode_poaLegacy_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('0xF977814e90dA44bFA03b6295A0616a897441aceC', 'f977814e90da44bfa03b6295a0616a897441acec'),
        ('0xBE0eB53F46cd790Cd13851d5EFf43D12404d33E8', 'be0eb53f46cd790cd13851d5eff43d12404d33e8')
])
def test_poaLegacy_decode(text: str, hex_value: str) -> None:
    assert decode_poaLegacy_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('0xF977814e90dA44bFA03b6295A0616a897441aceC', 'f977814e90da44bfa03b6295a0616a897441acec'),
        ('0xBE0eB53F46cd790Cd13851d5EFf43D12404d33E8', 'be0eb53f46cd790cd13851d5eff43d12404d33e8')
])
def test_poaLegacy_encode(expected_text: str, hex_value: str) -> None:
    assert encode_poaLegacy_address(bytes.fromhex(hex_value)) == expected_text

