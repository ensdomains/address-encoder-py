from __future__ import annotations

import pytest

from address_encoder.coins.xch import decode_xch_address, encode_xch_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('xch1f0ryxk6qn096hefcwrdwpuph2hm24w69jnzezhkfswk0z2jar7aq5zzpfj', '4bc6435b409bcbabe53870dae0f03755f6aabb4594c5915ec983acf12a5d1fba')
])
def test_xch_decode(text: str, hex_value: str) -> None:
    assert decode_xch_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('xch1f0ryxk6qn096hefcwrdwpuph2hm24w69jnzezhkfswk0z2jar7aq5zzpfj', '4bc6435b409bcbabe53870dae0f03755f6aabb4594c5915ec983acf12a5d1fba')
])
def test_xch_encode(expected_text: str, hex_value: str) -> None:
    assert encode_xch_address(bytes.fromhex(hex_value)) == expected_text

