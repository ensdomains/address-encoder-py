from __future__ import annotations

import pytest

from address_encoder.coins.bsv import decode_bsv_address, encode_bsv_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('1AGNa15ZQXAZUgFiqJ2i7Z2DPU2J6hW62i', '65a16059864a2fdbc7c99a4723a8395bc6f188eb'),
        ('1Ax4gZtb7gAit2TivwejZHYtNNLT18PUXJ', '6d23156cbbdcc82a5a47eee4c2c7c583c18b6bf4')
])
def test_bsv_decode(text: str, hex_value: str) -> None:
    assert decode_bsv_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('1AGNa15ZQXAZUgFiqJ2i7Z2DPU2J6hW62i', '65a16059864a2fdbc7c99a4723a8395bc6f188eb'),
        ('1Ax4gZtb7gAit2TivwejZHYtNNLT18PUXJ', '6d23156cbbdcc82a5a47eee4c2c7c583c18b6bf4')
])
def test_bsv_encode(expected_text: str, hex_value: str) -> None:
    assert encode_bsv_address(bytes.fromhex(hex_value)) == expected_text

