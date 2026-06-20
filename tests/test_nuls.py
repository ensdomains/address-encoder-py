from __future__ import annotations

import pytest

from address_encoder.coins.nuls import decode_nuls_address, encode_nuls_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('NULSd6HgXY3zLvEoCRUa6yFXwpnF8gqrDeToT', '0100013ba3e3c56062266262514c74fafb01852af99fec'),
        ('tNULSeBaMvEtDfvZuukDf2mVyfGo3DdiN8KLRG', '020001f7ec6473df12e751d64cf20a8baa7edd50810f81'),
        ('AHUcC84FN4CWrhuMgvvGPy6UacBvcutgQ4rAR', '79ff019fe3eff24409addcefe8f5115e17e5dfdd5f04c2'),
        ('APNcCm4yik6XXquTHUNbHqfPhGrfcSoGoMudc', '80ff01acfa253cc35655e300061e2563f813c5e4b9589c')
])
def test_nuls_decode(text: str, hex_value: str) -> None:
    assert decode_nuls_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('NULSd6HgXY3zLvEoCRUa6yFXwpnF8gqrDeToT', '0100013ba3e3c56062266262514c74fafb01852af99fec'),
        ('tNULSeBaMvEtDfvZuukDf2mVyfGo3DdiN8KLRG', '020001f7ec6473df12e751d64cf20a8baa7edd50810f81'),
        ('AHUcC84FN4CWrhuMgvvGPy6UacBvcutgQ4rAR', '79ff019fe3eff24409addcefe8f5115e17e5dfdd5f04c2'),
        ('APNcCm4yik6XXquTHUNbHqfPhGrfcSoGoMudc', '80ff01acfa253cc35655e300061e2563f813c5e4b9589c')
])
def test_nuls_encode(expected_text: str, hex_value: str) -> None:
    assert encode_nuls_address(bytes.fromhex(hex_value)) == expected_text

