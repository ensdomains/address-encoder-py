from __future__ import annotations

import pytest

from address_encoder.coins.ont import decode_ont_address, encode_ont_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('ALvmTSEjNREwcRNJiLcTkxCnsXBfbZEUFK', '3887346ea0b83129ff21f1ef3e6008a80373d1b3'),
        ('AavjHwiNfkr7xKGHBpNEQYSL5QiKgRjZf1', 'd21728df85b2b457908bd33def8ff493d47f184a'),
        ('AGmV3oHqzfAs3VFiqmn6cecxCXVNyg6tNh', '0ae542fee226c044dc19b036db7cec939777596f')
])
def test_ont_decode(text: str, hex_value: str) -> None:
    assert decode_ont_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('ALvmTSEjNREwcRNJiLcTkxCnsXBfbZEUFK', '3887346ea0b83129ff21f1ef3e6008a80373d1b3'),
        ('AavjHwiNfkr7xKGHBpNEQYSL5QiKgRjZf1', 'd21728df85b2b457908bd33def8ff493d47f184a'),
        ('AGmV3oHqzfAs3VFiqmn6cecxCXVNyg6tNh', '0ae542fee226c044dc19b036db7cec939777596f')
])
def test_ont_encode(expected_text: str, hex_value: str) -> None:
    assert encode_ont_address(bytes.fromhex(hex_value)) == expected_text

