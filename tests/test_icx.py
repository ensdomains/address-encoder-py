from __future__ import annotations

import pytest

from address_encoder.coins.icx import decode_icx_address, encode_icx_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('hx6b38701ddc411e6f4e84a04f6abade7661a207e2', '006b38701ddc411e6f4e84a04f6abade7661a207e2'),
        ('cxa4524257b3511fb9574009785c1f1e73cf4097e7', '01a4524257b3511fb9574009785c1f1e73cf4097e7')
])
def test_icx_decode(text: str, hex_value: str) -> None:
    assert decode_icx_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('hx6b38701ddc411e6f4e84a04f6abade7661a207e2', '006b38701ddc411e6f4e84a04f6abade7661a207e2'),
        ('cxa4524257b3511fb9574009785c1f1e73cf4097e7', '01a4524257b3511fb9574009785c1f1e73cf4097e7')
])
def test_icx_encode(expected_text: str, hex_value: str) -> None:
    assert encode_icx_address(bytes.fromhex(hex_value)) == expected_text

