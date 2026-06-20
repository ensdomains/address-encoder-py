from __future__ import annotations

import pytest

from address_encoder.coins.grin import decode_grin_address, encode_grin_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('grin1k6m6sjpwc047zdhsdj9r77v5nnxm33hx7wxqvw5dhd9vl0d7t4fsaqt0lg', 'b6b7a8482ec3ebe136f06c8a3f79949ccdb8c6e6f38c063a8dbb4acfbdbe5d53')
])
def test_grin_decode(text: str, hex_value: str) -> None:
    assert decode_grin_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('grin1k6m6sjpwc047zdhsdj9r77v5nnxm33hx7wxqvw5dhd9vl0d7t4fsaqt0lg', 'b6b7a8482ec3ebe136f06c8a3f79949ccdb8c6e6f38c063a8dbb4acfbdbe5d53')
])
def test_grin_encode(expected_text: str, hex_value: str) -> None:
    assert encode_grin_address(bytes.fromhex(hex_value)) == expected_text

