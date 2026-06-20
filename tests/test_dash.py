from __future__ import annotations

import pytest

from address_encoder.coins.dash import decode_dash_address, encode_dash_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('XtAG1982HcYJVibHxRZrBmdzL5YTzj4cA1', '76a914bfa98bb8a919330c432e4ff16563c5ab449604ad88ac'),
        ('7gks9gWVmGeir7m4MhsSxMzXC2eXXAuuRD', 'a9149d646d71f0815c0cfd8cd08aa9d391cd127f378687')
])
def test_dash_decode(text: str, hex_value: str) -> None:
    assert decode_dash_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('XtAG1982HcYJVibHxRZrBmdzL5YTzj4cA1', '76a914bfa98bb8a919330c432e4ff16563c5ab449604ad88ac'),
        ('7gks9gWVmGeir7m4MhsSxMzXC2eXXAuuRD', 'a9149d646d71f0815c0cfd8cd08aa9d391cd127f378687')
])
def test_dash_encode(expected_text: str, hex_value: str) -> None:
    assert encode_dash_address(bytes.fromhex(hex_value)) == expected_text

