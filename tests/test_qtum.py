from __future__ import annotations

import pytest

from address_encoder.coins.qtum import decode_qtum_address, encode_qtum_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('Qc6iYCZWn4BauKXGYirRG8pMtgdHMk2dzn', '3aa9f8f3b055324f6b2d6bcac328ec2d7e3cd22d8b')
])
def test_qtum_decode(text: str, hex_value: str) -> None:
    assert decode_qtum_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('Qc6iYCZWn4BauKXGYirRG8pMtgdHMk2dzn', '3aa9f8f3b055324f6b2d6bcac328ec2d7e3cd22d8b')
])
def test_qtum_encode(expected_text: str, hex_value: str) -> None:
    assert encode_qtum_address(bytes.fromhex(hex_value)) == expected_text

