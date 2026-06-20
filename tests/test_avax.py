from __future__ import annotations

import pytest

from address_encoder.coins.avax import decode_avax_address, encode_avax_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('avax1a5h6v9weng8guuah6aamagea0xhsd04mvs2zun', 'ed2fa615d99a0e8e73b7d77bbea33d79af06bebb'),
        ('P-avax1a5h6v9weng8guuah6aamagea0xhsd04mvs2zun', 'ed2fa615d99a0e8e73b7d77bbea33d79af06bebb'),
        ('X-avax1a5h6v9weng8guuah6aamagea0xhsd04mvs2zun', 'ed2fa615d99a0e8e73b7d77bbea33d79af06bebb')
])
def test_avax_decode(text: str, hex_value: str) -> None:
    assert decode_avax_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('avax1a5h6v9weng8guuah6aamagea0xhsd04mvs2zun', 'ed2fa615d99a0e8e73b7d77bbea33d79af06bebb'),
        ('avax1a5h6v9weng8guuah6aamagea0xhsd04mvs2zun', 'ed2fa615d99a0e8e73b7d77bbea33d79af06bebb'),
        ('avax1a5h6v9weng8guuah6aamagea0xhsd04mvs2zun', 'ed2fa615d99a0e8e73b7d77bbea33d79af06bebb')
])
def test_avax_decode_canonical(text: str, hex_value: str) -> None:
    assert decode_avax_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('avax1a5h6v9weng8guuah6aamagea0xhsd04mvs2zun', 'ed2fa615d99a0e8e73b7d77bbea33d79af06bebb'),
        ('avax1a5h6v9weng8guuah6aamagea0xhsd04mvs2zun', 'ed2fa615d99a0e8e73b7d77bbea33d79af06bebb'),
        ('avax1a5h6v9weng8guuah6aamagea0xhsd04mvs2zun', 'ed2fa615d99a0e8e73b7d77bbea33d79af06bebb')
])
def test_avax_encode(expected_text: str, hex_value: str) -> None:
    assert encode_avax_address(bytes.fromhex(hex_value)) == expected_text

