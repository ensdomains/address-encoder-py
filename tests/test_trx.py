from __future__ import annotations

import pytest

from address_encoder.coins.trx import decode_trx_address, encode_trx_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('TUrMmF9Gd4rzrXsQ34ui3Wou94E7HFuJQh', '41cf1ecacaf90a04bb0297f9991ae1262d0a3399e1'),
        ('TJCnKsPa7y5okkXvQAidZBzqx3QyQ6sxMW', '415a523b449890854c8fc460ab602df9f31fe4293f')
])
def test_trx_decode(text: str, hex_value: str) -> None:
    assert decode_trx_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('TUrMmF9Gd4rzrXsQ34ui3Wou94E7HFuJQh', '41cf1ecacaf90a04bb0297f9991ae1262d0a3399e1'),
        ('TJCnKsPa7y5okkXvQAidZBzqx3QyQ6sxMW', '415a523b449890854c8fc460ab602df9f31fe4293f')
])
def test_trx_encode(expected_text: str, hex_value: str) -> None:
    assert encode_trx_address(bytes.fromhex(hex_value)) == expected_text

