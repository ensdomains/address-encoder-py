from __future__ import annotations

import pytest

from address_encoder.coins.rbtc import decode_rbtc_address, encode_rbtc_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('0x5aaEB6053f3e94c9b9a09f33669435E7ef1bEAeD', '5aaEB6053f3e94c9b9a09f33669435E7ef1bEAeD')
])
def test_rbtc_decode(text: str, hex_value: str) -> None:
    assert decode_rbtc_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('0x5aaEB6053f3e94c9b9a09f33669435E7ef1bEAeD', '5aaEB6053f3e94c9b9a09f33669435E7ef1bEAeD')
])
def test_rbtc_encode(expected_text: str, hex_value: str) -> None:
    assert encode_rbtc_address(bytes.fromhex(hex_value)) == expected_text

