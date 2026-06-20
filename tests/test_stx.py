from __future__ import annotations

import pytest

from address_encoder.coins.stx import decode_stx_address, encode_stx_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('SP2J6ZY48GV1EZ5V2V5RB9MP66SW86PYKKNRV9EJ7', 'a46ff88886c2ef9762d970b4d2c63678835bd39d71b4ba47'),
        ('SM2J6ZY48GV1EZ5V2V5RB9MP66SW86PYKKQVX8X0G', 'a46ff88886c2ef9762d970b4d2c63678835bd39df7d47410')
])
def test_stx_decode(text: str, hex_value: str) -> None:
    assert decode_stx_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('SP2J6ZY48GV1EZ5V2V5RB9MP66SW86PYKKNRV9EJ7', 'a46ff88886c2ef9762d970b4d2c63678835bd39d71b4ba47'),
        ('SM2J6ZY48GV1EZ5V2V5RB9MP66SW86PYKKQVX8X0G', 'a46ff88886c2ef9762d970b4d2c63678835bd39df7d47410')
])
def test_stx_encode(expected_text: str, hex_value: str) -> None:
    assert encode_stx_address(bytes.fromhex(hex_value)) == expected_text

