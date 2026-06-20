from __future__ import annotations

import pytest

from address_encoder.coins.kmd import decode_kmd_address, encode_kmd_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('RDNC9mLrN48pVGDQ5jSoPb2nRsUPJ5t2R7', '76a9142cd2a4e3d1c2738ee4fce61e73ea822dcaacb9b488ac')
])
def test_kmd_decode(text: str, hex_value: str) -> None:
    assert decode_kmd_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('RDNC9mLrN48pVGDQ5jSoPb2nRsUPJ5t2R7', '76a9142cd2a4e3d1c2738ee4fce61e73ea822dcaacb9b488ac')
])
def test_kmd_encode(expected_text: str, hex_value: str) -> None:
    assert encode_kmd_address(bytes.fromhex(hex_value)) == expected_text

