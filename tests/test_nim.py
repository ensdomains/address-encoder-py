from __future__ import annotations

import pytest

from address_encoder.coins.nim import decode_nim_address, encode_nim_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('NQ18 GAL5 Y1FC 66VV PE1X J82Q 0A2F LYPB 2EY7', '82a85f85ec31bbdbb83e920580284fa7eeb13be7')
])
def test_nim_decode(text: str, hex_value: str) -> None:
    assert decode_nim_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('NQ18 GAL5 Y1FC 66VV PE1X J82Q 0A2F LYPB 2EY7', '82a85f85ec31bbdbb83e920580284fa7eeb13be7')
])
def test_nim_encode(expected_text: str, hex_value: str) -> None:
    assert encode_nim_address(bytes.fromhex(hex_value)) == expected_text

