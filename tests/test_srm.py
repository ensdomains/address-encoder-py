from __future__ import annotations

import pytest

from address_encoder.coins.srm import decode_srm_address, encode_srm_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('6ZRCB7AAqGre6c72PRz3MHLC73VMYvJ8bi9KHf1HFpNk', '52986010573739df4b58ba50e39cf3f335b89cc7d1cb1d32b5de04efa068c939')
])
def test_srm_decode(text: str, hex_value: str) -> None:
    assert decode_srm_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('6ZRCB7AAqGre6c72PRz3MHLC73VMYvJ8bi9KHf1HFpNk', '52986010573739df4b58ba50e39cf3f335b89cc7d1cb1d32b5de04efa068c939')
])
def test_srm_encode(expected_text: str, hex_value: str) -> None:
    assert encode_srm_address(bytes.fromhex(hex_value)) == expected_text

