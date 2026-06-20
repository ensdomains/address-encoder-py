from __future__ import annotations

import pytest

from address_encoder.coins.bps import decode_bps_address, encode_bps_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('1AGNa15ZQXAZUgFiqJ2i7Z2DPU2J6hW62i', '76a91465a16059864a2fdbc7c99a4723a8395bc6f188eb88ac'),
        ('3CMNFxN1oHBc4R1EpboAL5yzHGgE611Xou', 'a91474f209f6ea907e2ea48f74fae05782ae8a66525787')
])
def test_bps_decode(text: str, hex_value: str) -> None:
    assert decode_bps_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('1AGNa15ZQXAZUgFiqJ2i7Z2DPU2J6hW62i', '76a91465a16059864a2fdbc7c99a4723a8395bc6f188eb88ac'),
        ('3CMNFxN1oHBc4R1EpboAL5yzHGgE611Xou', 'a91474f209f6ea907e2ea48f74fae05782ae8a66525787')
])
def test_bps_encode(expected_text: str, hex_value: str) -> None:
    assert encode_bps_address(bytes.fromhex(hex_value)) == expected_text

