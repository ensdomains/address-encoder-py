from __future__ import annotations

import pytest

from address_encoder.coins.kava import decode_kava_address, encode_kava_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('kava1r4v2zdhdalfj2ydazallqvrus9fkphmglhn6u6', '1d58a136edefd32511bd177ff0307c815360df68')
])
def test_kava_decode(text: str, hex_value: str) -> None:
    assert decode_kava_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('kava1r4v2zdhdalfj2ydazallqvrus9fkphmglhn6u6', '1d58a136edefd32511bd177ff0307c815360df68')
])
def test_kava_encode(expected_text: str, hex_value: str) -> None:
    assert encode_kava_address(bytes.fromhex(hex_value)) == expected_text

