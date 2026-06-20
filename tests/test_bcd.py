from __future__ import annotations

import pytest

from address_encoder.coins.bcd import decode_bcd_address, encode_bcd_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('1AGNa15ZQXAZUgFiqJ2i7Z2DPU2J6hW62i', '76a91465a16059864a2fdbc7c99a4723a8395bc6f188eb88ac'),
        ('3CMNFxN1oHBc4R1EpboAL5yzHGgE611Xou', 'a91474f209f6ea907e2ea48f74fae05782ae8a66525787')
])
def test_bcd_decode(text: str, hex_value: str) -> None:
    assert decode_bcd_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('1AGNa15ZQXAZUgFiqJ2i7Z2DPU2J6hW62i', '76a91465a16059864a2fdbc7c99a4723a8395bc6f188eb88ac'),
        ('3CMNFxN1oHBc4R1EpboAL5yzHGgE611Xou', 'a91474f209f6ea907e2ea48f74fae05782ae8a66525787')
])
def test_bcd_encode(expected_text: str, hex_value: str) -> None:
    assert encode_bcd_address(bytes.fromhex(hex_value)) == expected_text

