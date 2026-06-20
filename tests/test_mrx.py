from __future__ import annotations

import pytest

from address_encoder.coins.mrx import decode_mrx_address, encode_mrx_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('MPYAKTYDaEMEXWFSxHeMtpXNNiSjK4TVch', '32ab8959869ee2579028abdf6a199b049bfae6dc3b')
])
def test_mrx_decode(text: str, hex_value: str) -> None:
    assert decode_mrx_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('MPYAKTYDaEMEXWFSxHeMtpXNNiSjK4TVch', '32ab8959869ee2579028abdf6a199b049bfae6dc3b')
])
def test_mrx_encode(expected_text: str, hex_value: str) -> None:
    assert encode_mrx_address(bytes.fromhex(hex_value)) == expected_text

