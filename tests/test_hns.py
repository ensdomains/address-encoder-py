from __future__ import annotations

import pytest

from address_encoder.coins.hns import decode_hns_address, encode_hns_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('hs1qd42hrldu5yqee58se4uj6xctm7nk28r70e84vx', '6d5571fdbca1019cd0f0cd792d1b0bdfa7651c7e')
])
def test_hns_decode(text: str, hex_value: str) -> None:
    assert decode_hns_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('hs1qd42hrldu5yqee58se4uj6xctm7nk28r70e84vx', '6d5571fdbca1019cd0f0cd792d1b0bdfa7651c7e')
])
def test_hns_encode(expected_text: str, hex_value: str) -> None:
    assert encode_hns_address(bytes.fromhex(hex_value)) == expected_text

