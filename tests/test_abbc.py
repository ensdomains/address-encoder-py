from __future__ import annotations

import pytest

from address_encoder.coins.abbc import decode_abbc_address, encode_abbc_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('ABBC5i3zbGsuyexJc6NaHv81yPh2WeaqrtYMMVaEqcYLz9guAAV74A', '026bff3fc4dc3cde1dcb2068bef16624a260c6f0e330addb54f894bce7fa353de6'),
        ('ABBC5MTKdW6dFqEjYqQYMmLohCsALWcBAx2xRapzDTKAtz3XwKJcaf', '023d3a2e33a90f8f5bcbda1ec129ba1eee5e5f2ab6a77d652cbb0517f2b49669e8')
])
def test_abbc_decode(text: str, hex_value: str) -> None:
    assert decode_abbc_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('ABBC5i3zbGsuyexJc6NaHv81yPh2WeaqrtYMMVaEqcYLz9guAAV74A', '026bff3fc4dc3cde1dcb2068bef16624a260c6f0e330addb54f894bce7fa353de6'),
        ('ABBC5MTKdW6dFqEjYqQYMmLohCsALWcBAx2xRapzDTKAtz3XwKJcaf', '023d3a2e33a90f8f5bcbda1ec129ba1eee5e5f2ab6a77d652cbb0517f2b49669e8')
])
def test_abbc_encode(expected_text: str, hex_value: str) -> None:
    assert encode_abbc_address(bytes.fromhex(hex_value)) == expected_text

