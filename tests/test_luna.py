from __future__ import annotations

import pytest

from address_encoder.coins.luna import decode_luna_address, encode_luna_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('terra1pdx498r0hrc2fj36sjhs8vuhrz9hd2cw0tmam9', '0b4d529c6fb8f0a4ca3a84af03b397188b76ab0e')
])
def test_luna_decode(text: str, hex_value: str) -> None:
    assert decode_luna_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('terra1pdx498r0hrc2fj36sjhs8vuhrz9hd2cw0tmam9', '0b4d529c6fb8f0a4ca3a84af03b397188b76ab0e')
])
def test_luna_encode(expected_text: str, hex_value: str) -> None:
    assert encode_luna_address(bytes.fromhex(hex_value)) == expected_text

