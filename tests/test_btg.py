from __future__ import annotations

import pytest

from address_encoder.coins.btg import decode_btg_address, encode_btg_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('GT7Hz8QWPNmrZ9Z1mEgpYKN7Jdp97eoQjN', '76a91465a16059864a2fdbc7c99a4723a8395bc6f188eb88ac'),
        ('AQRA16uKrFpxzR17yidYtJDn2t287dc1XY', 'a9145ece0cadddc415b1980f001785947120acdb36fc87'),
        ('btg1zw508d6qejxtdg4y5r3zarvaryvl9f8z2', '5210751e76e8199196d454941c45d1b3a323'),
        ('btg1pw508d6qejxtdg4y5r3zarvary0c5xw7kw508d6qejxtdg4y5r3zarvary0c5xw7kdd2qs6', '5128751e76e8199196d454941c45d1b3a323f1433bd6751e76e8199196d454941c45d1b3a323f1433bd6')
])
def test_btg_decode(text: str, hex_value: str) -> None:
    assert decode_btg_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('GT7Hz8QWPNmrZ9Z1mEgpYKN7Jdp97eoQjN', '76a91465a16059864a2fdbc7c99a4723a8395bc6f188eb88ac'),
        ('AQRA16uKrFpxzR17yidYtJDn2t287dc1XY', 'a9145ece0cadddc415b1980f001785947120acdb36fc87'),
        ('btg1zw508d6qejxtdg4y5r3zarvaryvl9f8z2', '5210751e76e8199196d454941c45d1b3a323'),
        ('btg1pw508d6qejxtdg4y5r3zarvary0c5xw7kw508d6qejxtdg4y5r3zarvary0c5xw7kdd2qs6', '5128751e76e8199196d454941c45d1b3a323f1433bd6751e76e8199196d454941c45d1b3a323f1433bd6')
])
def test_btg_encode(expected_text: str, hex_value: str) -> None:
    assert encode_btg_address(bytes.fromhex(hex_value)) == expected_text

