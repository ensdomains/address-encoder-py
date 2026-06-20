from __future__ import annotations

import pytest

from address_encoder.coins.nano import decode_nano_address, encode_nano_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('nano_15dng9kx49xfumkm4q6qpaxneie6oynebiwpums3ktdd6t3f3dhp69nxgb38', '0d7471e5d11faddce5315c97b23b464184afa8c4c396dcf219696b2682d0adf6'),
        ('nano_1anrzcuwe64rwxzcco8dkhpyxpi8kd7zsjc1oeimpc3ppca4mrjtwnqposrs', '2298fab7c61058e77ea554cb93edeeda0692cbfcc540ab213b2836b29029e23a')
])
def test_nano_decode(text: str, hex_value: str) -> None:
    assert decode_nano_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('nano_15dng9kx49xfumkm4q6qpaxneie6oynebiwpums3ktdd6t3f3dhp69nxgb38', '0d7471e5d11faddce5315c97b23b464184afa8c4c396dcf219696b2682d0adf6'),
        ('nano_1anrzcuwe64rwxzcco8dkhpyxpi8kd7zsjc1oeimpc3ppca4mrjtwnqposrs', '2298fab7c61058e77ea554cb93edeeda0692cbfcc540ab213b2836b29029e23a')
])
def test_nano_encode(expected_text: str, hex_value: str) -> None:
    assert encode_nano_address(bytes.fromhex(hex_value)) == expected_text

