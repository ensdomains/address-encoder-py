from __future__ import annotations

import pytest

from address_encoder.coins.atom import decode_atom_address, encode_atom_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('cosmos1depk54cuajgkzea6zpgkq36tnjwdzv4afc3d27', '6e436a571cec916167ba105160474b9c9cd132bd')
])
def test_atom_decode(text: str, hex_value: str) -> None:
    assert decode_atom_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('cosmos1depk54cuajgkzea6zpgkq36tnjwdzv4afc3d27', '6e436a571cec916167ba105160474b9c9cd132bd')
])
def test_atom_encode(expected_text: str, hex_value: str) -> None:
    assert encode_atom_address(bytes.fromhex(hex_value)) == expected_text

