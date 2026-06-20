from __future__ import annotations

import pytest

from address_encoder.coins.iris import decode_iris_address, encode_iris_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('iaa1k5y45px87c42ttxgk8x4y6w0y9gzgcwvvunht5', 'b5095a04c7f62aa5acc8b1cd5269cf21502461cc')
])
def test_iris_decode(text: str, hex_value: str) -> None:
    assert decode_iris_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('iaa1k5y45px87c42ttxgk8x4y6w0y9gzgcwvvunht5', 'b5095a04c7f62aa5acc8b1cd5269cf21502461cc')
])
def test_iris_encode(expected_text: str, hex_value: str) -> None:
    assert encode_iris_address(bytes.fromhex(hex_value)) == expected_text

