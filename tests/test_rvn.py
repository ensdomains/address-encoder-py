from __future__ import annotations

import pytest

from address_encoder.coins.rvn import decode_rvn_address, encode_rvn_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('RJYZeWxr1Ly8YgcvJU1qD5MR9jUtk14HkN', '76a91465a16059864a2fdbc7c99a4723a8395bc6f188eb88ac'),
        ('rGtwTfEisPQ7k8KNggmT4kq2vHpbEV6evU', 'a91474f209f6ea907e2ea48f74fae05782ae8a66525787')
])
def test_rvn_decode(text: str, hex_value: str) -> None:
    assert decode_rvn_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('RJYZeWxr1Ly8YgcvJU1qD5MR9jUtk14HkN', '76a91465a16059864a2fdbc7c99a4723a8395bc6f188eb88ac'),
        ('rGtwTfEisPQ7k8KNggmT4kq2vHpbEV6evU', 'a91474f209f6ea907e2ea48f74fae05782ae8a66525787')
])
def test_rvn_encode(expected_text: str, hex_value: str) -> None:
    assert encode_rvn_address(bytes.fromhex(hex_value)) == expected_text

