from __future__ import annotations

import pytest

from address_encoder.coins.btm import decode_btm_address, encode_btm_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('bm1qw508d6qejxtdg4y5r3zarvary0c5xw7k23gyyf', '0014751e76e8199196d454941c45d1b3a323f1433bd6'),
        ('bm1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3qk5egtg', '00201863143c14c5166804bd19203356da136c985678cd4d27a1b8c6329604903262')
])
def test_btm_decode(text: str, hex_value: str) -> None:
    assert decode_btm_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('bm1qw508d6qejxtdg4y5r3zarvary0c5xw7k23gyyf', '0014751e76e8199196d454941c45d1b3a323f1433bd6'),
        ('bm1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3qk5egtg', '00201863143c14c5166804bd19203356da136c985678cd4d27a1b8c6329604903262')
])
def test_btm_encode(expected_text: str, hex_value: str) -> None:
    assert encode_btm_address(bytes.fromhex(hex_value)) == expected_text

