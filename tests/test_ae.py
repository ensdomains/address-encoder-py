from __future__ import annotations

import pytest

from address_encoder.coins.ae import decode_ae_address, encode_ae_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('ak_Gd6iMVsoonGuTF8LeswwDDN2NF5wYHAoTRtzwdEcfS32LWoxm', '30782378f892b7cc82c2d2739e994ec9953aa36461f1eb5a4a49a5b0de17b3d23ae8')
])
def test_ae_decode(text: str, hex_value: str) -> None:
    assert decode_ae_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('ak_Gd6iMVsoonGuTF8LeswwDDN2NF5wYHAoTRtzwdEcfS32LWoxm', '30782378f892b7cc82c2d2739e994ec9953aa36461f1eb5a4a49a5b0de17b3d23ae8')
])
def test_ae_encode(expected_text: str, hex_value: str) -> None:
    assert encode_ae_address(bytes.fromhex(hex_value)) == expected_text

