from __future__ import annotations

import pytest

from address_encoder.coins.wicc import decode_wicc_address, encode_wicc_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('WPCCQwJafaApw6482EkDR6V84arfa47VmT', '76a91405b4701f113f51576fd7f6422dfe6ab00f41739488ac'),
        ('WV116oEVxKUzrafgcRZXCNdDN7r7hjt4xV', '76a91445672c77361c4f90f95b7c4c721f375a6a99766888ac')
])
def test_wicc_decode(text: str, hex_value: str) -> None:
    assert decode_wicc_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('WPCCQwJafaApw6482EkDR6V84arfa47VmT', '76a91405b4701f113f51576fd7f6422dfe6ab00f41739488ac'),
        ('WV116oEVxKUzrafgcRZXCNdDN7r7hjt4xV', '76a91445672c77361c4f90f95b7c4c721f375a6a99766888ac')
])
def test_wicc_encode(expected_text: str, hex_value: str) -> None:
    assert encode_wicc_address(bytes.fromhex(hex_value)) == expected_text

