from __future__ import annotations

import pytest

from address_encoder.coins.lrg import decode_lrg_address, encode_lrg_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('DM8Zwin2rJczpjy2TXY5UZbZQLkUhYBH61', '76a914af687904a4e15a2f1cac37dfb6cbceb9dba8afb788ac'),
        ('6bNNutYQz11WrkVCrj1nUS1dBGyoVZjdEg', 'a914e613c7be9b53e1a47fd4edb3ea9777cf29dce30f87')
])
def test_lrg_decode(text: str, hex_value: str) -> None:
    assert decode_lrg_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('DM8Zwin2rJczpjy2TXY5UZbZQLkUhYBH61', '76a914af687904a4e15a2f1cac37dfb6cbceb9dba8afb788ac'),
        ('6bNNutYQz11WrkVCrj1nUS1dBGyoVZjdEg', 'a914e613c7be9b53e1a47fd4edb3ea9777cf29dce30f87')
])
def test_lrg_encode(expected_text: str, hex_value: str) -> None:
    assert encode_lrg_address(bytes.fromhex(hex_value)) == expected_text

