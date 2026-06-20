from __future__ import annotations

import pytest

from address_encoder.coins.ppc import decode_ppc_address, encode_ppc_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('PRL8bojUujzDGA6HRapzprXWFxMyhpS7Za', '76a914b7a1c4349e794ee3484b8f433a7063eb614dfdc788ac')
])
def test_ppc_decode(text: str, hex_value: str) -> None:
    assert decode_ppc_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('PRL8bojUujzDGA6HRapzprXWFxMyhpS7Za', '76a914b7a1c4349e794ee3484b8f433a7063eb614dfdc788ac')
])
def test_ppc_encode(expected_text: str, hex_value: str) -> None:
    assert encode_ppc_address(bytes.fromhex(hex_value)) == expected_text

