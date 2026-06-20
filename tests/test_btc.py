from __future__ import annotations

import pytest

from address_encoder.coins.btc import decode_btc_address, encode_btc_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa', '76a91462e907b15cbf27d5425399ebf6f0fb50ebb88f1888ac'),
        ('3Ai1JZ8pdJb2ksieUV8FsxSNVJCpoPi8W6', 'a91462e907b15cbf27d5425399ebf6f0fb50ebb88f1887'),
        ('bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4', '0014751e76e8199196d454941c45d1b3a323f1433bd6'),
        ('bc1pw508d6qejxtdg4y5r3zarvary0c5xw7kw508d6qejxtdg4y5r3zarvary0c5xw7kt5nd6y', '5128751e76e8199196d454941c45d1b3a323f1433bd6751e76e8199196d454941c45d1b3a323f1433bd6'),
        ('bc1sw50qgdz25j', '6002751e'),
        ('bc1zw508d6qejxtdg4y5r3zarvaryvaxxpcs', '5210751e76e8199196d454941c45d1b3a323'),
        ('bc1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3qccfmv3', '00201863143c14c5166804bd19203356da136c985678cd4d27a1b8c6329604903262'),
        ('bc1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3qccfmv3', '00201863143c14c5166804bd19203356da136c985678cd4d27a1b8c6329604903262'),
        ('bc1p0xlxvlhemja6c4dqv22uapctqupfhlxm9h8z3k2e72q4k9hcz7vqzk5jj0', '512079be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798')
])
def test_btc_decode(text: str, hex_value: str) -> None:
    assert decode_btc_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa', '76a91462e907b15cbf27d5425399ebf6f0fb50ebb88f1888ac'),
        ('3Ai1JZ8pdJb2ksieUV8FsxSNVJCpoPi8W6', 'a91462e907b15cbf27d5425399ebf6f0fb50ebb88f1887'),
        ('bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4', '0014751e76e8199196d454941c45d1b3a323f1433bd6'),
        ('bc1pw508d6qejxtdg4y5r3zarvary0c5xw7kw508d6qejxtdg4y5r3zarvary0c5xw7kt5nd6y', '5128751e76e8199196d454941c45d1b3a323f1433bd6751e76e8199196d454941c45d1b3a323f1433bd6'),
        ('bc1sw50qgdz25j', '6002751e'),
        ('bc1zw508d6qejxtdg4y5r3zarvaryvaxxpcs', '5210751e76e8199196d454941c45d1b3a323'),
        ('bc1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3qccfmv3', '00201863143c14c5166804bd19203356da136c985678cd4d27a1b8c6329604903262'),
        ('bc1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3qccfmv3', '00201863143c14c5166804bd19203356da136c985678cd4d27a1b8c6329604903262'),
        ('bc1p0xlxvlhemja6c4dqv22uapctqupfhlxm9h8z3k2e72q4k9hcz7vqzk5jj0', '512079be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798')
])
def test_btc_encode(expected_text: str, hex_value: str) -> None:
    assert encode_btc_address(bytes.fromhex(hex_value)) == expected_text

