from __future__ import annotations

import pytest

from address_encoder.coins.waves import decode_waves_address, encode_waves_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('3PAP3wkgbGjdd1FuBLn9ajXvo6edBMCa115', '01575cb3839cef68f8b5650461fe707311e2919c73b945cf1edc')
])
def test_waves_decode(text: str, hex_value: str) -> None:
    assert decode_waves_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('3PAP3wkgbGjdd1FuBLn9ajXvo6edBMCa115', '01575cb3839cef68f8b5650461fe707311e2919c73b945cf1edc')
])
def test_waves_encode(expected_text: str, hex_value: str) -> None:
    assert encode_waves_address(bytes.fromhex(hex_value)) == expected_text

