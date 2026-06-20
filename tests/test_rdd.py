from __future__ import annotations

import pytest

from address_encoder.coins.rdd import decode_rdd_address, encode_rdd_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('RkQDYcqiv7mzQfNYMc8FfYv3dtQ8wuSGoM', '76a914814089fb909f05918d54e530f0ad8e339a4edffe88ac'),
        ('3QJmV3qfvL9SuYo34YihAf3sRCW3qSinyC', 'a914f815b036d9bbbce5e9f2a00abd1bf3dc91e9551087')
])
def test_rdd_decode(text: str, hex_value: str) -> None:
    assert decode_rdd_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('RkQDYcqiv7mzQfNYMc8FfYv3dtQ8wuSGoM', '76a914814089fb909f05918d54e530f0ad8e339a4edffe88ac'),
        ('3QJmV3qfvL9SuYo34YihAf3sRCW3qSinyC', 'a914f815b036d9bbbce5e9f2a00abd1bf3dc91e9551087')
])
def test_rdd_encode(expected_text: str, hex_value: str) -> None:
    assert encode_rdd_address(bytes.fromhex(hex_value)) == expected_text

