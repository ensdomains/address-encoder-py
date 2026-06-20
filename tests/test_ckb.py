from __future__ import annotations

import pytest

from address_encoder.coins.ckb import decode_ckb_address, encode_ckb_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('ckb1qyqt8xaupvm8837nv3gtc9x0ekkj64vud3jqfwyw5v', '0100b39bbc0b3673c7d36450bc14cfcdad2d559c6c64')
])
def test_ckb_decode(text: str, hex_value: str) -> None:
    assert decode_ckb_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('ckb1qyqt8xaupvm8837nv3gtc9x0ekkj64vud3jqfwyw5v', '0100b39bbc0b3673c7d36450bc14cfcdad2d559c6c64')
])
def test_ckb_encode(expected_text: str, hex_value: str) -> None:
    assert encode_ckb_address(bytes.fromhex(hex_value)) == expected_text

