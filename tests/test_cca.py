from __future__ import annotations

import pytest

from address_encoder.coins.cca import decode_cca_address, encode_cca_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('5jZrpsZVkNhDKEuNcYZ1kk2wNWJRbaKy22', '76a914c3c95e1effb0f6ebde0ac0751d6bfd69ad98511c88ac'),
        ('5mi7oAoMVL7cVJhXsmWxnTDxTUiBUkR996', '76a914db49719be13e8221f6d568a01f9d14adc4f887ff88ac')
])
def test_cca_decode(text: str, hex_value: str) -> None:
    assert decode_cca_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('5jZrpsZVkNhDKEuNcYZ1kk2wNWJRbaKy22', '76a914c3c95e1effb0f6ebde0ac0751d6bfd69ad98511c88ac'),
        ('5mi7oAoMVL7cVJhXsmWxnTDxTUiBUkR996', '76a914db49719be13e8221f6d568a01f9d14adc4f887ff88ac')
])
def test_cca_encode(expected_text: str, hex_value: str) -> None:
    assert encode_cca_address(bytes.fromhex(hex_value)) == expected_text

