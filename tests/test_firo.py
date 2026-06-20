from __future__ import annotations

import pytest

from address_encoder.coins.firo import decode_firo_address, encode_firo_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('aJpBLBFFkxY1iGfBmZCTWQQABPqakQwWZ3', '76a914c6870ff00109a0aaca255e609de7d40d245aa61788ac'),
        ('a4roLhCKc2m3RtG7ucoxyJrCk2JqayqdSr', '76a9142d743121ff929299be3c4488ce64e22634d58d5f88ac'),
        ('Zzn3ivpQZ3XoTnEBUuqPuVCMJ3JBGoxmsi', '76a91400ad9d984a8217ffe6548ef5c91b12e6c8d2c10788ac')
])
def test_firo_decode(text: str, hex_value: str) -> None:
    assert decode_firo_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('aJpBLBFFkxY1iGfBmZCTWQQABPqakQwWZ3', '76a914c6870ff00109a0aaca255e609de7d40d245aa61788ac'),
        ('a4roLhCKc2m3RtG7ucoxyJrCk2JqayqdSr', '76a9142d743121ff929299be3c4488ce64e22634d58d5f88ac'),
        ('Zzn3ivpQZ3XoTnEBUuqPuVCMJ3JBGoxmsi', '76a91400ad9d984a8217ffe6548ef5c91b12e6c8d2c10788ac')
])
def test_firo_encode(expected_text: str, hex_value: str) -> None:
    assert encode_firo_address(bytes.fromhex(hex_value)) == expected_text

