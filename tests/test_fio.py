from __future__ import annotations

import pytest

from address_encoder.coins.fio import decode_fio_address, encode_fio_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('FIO7tkpmicyK2YWShSKef6B9XXqBN6LpDJo69oRDfhn67CEnj3L2G', '038bb1a68d19eb9139734d0f38da55cfcea955ed8f0baf42f12502e244293c08eb')
])
def test_fio_decode(text: str, hex_value: str) -> None:
    assert decode_fio_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('FIO7tkpmicyK2YWShSKef6B9XXqBN6LpDJo69oRDfhn67CEnj3L2G', '038bb1a68d19eb9139734d0f38da55cfcea955ed8f0baf42f12502e244293c08eb')
])
def test_fio_encode(expected_text: str, hex_value: str) -> None:
    assert encode_fio_address(bytes.fromhex(hex_value)) == expected_text

