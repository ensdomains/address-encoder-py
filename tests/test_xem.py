from __future__ import annotations

import pytest

from address_encoder.coins.xem import decode_xem_address, encode_xem_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('NAPRILC6USCTAY7NNXB4COVKQJL427NPCEERGKS6', '681f142c5ea4853063ed6dc3c13aaa8257cd7daf1109132a5e'),
        ('NAMOAVHFVPJ6FP32YP2GCM64WSRMKXA5KKYWWHPY', '6818e054e5abd3e2bf7ac3f46133dcb4a2c55c1d52b16b1df8')
])
def test_xem_decode(text: str, hex_value: str) -> None:
    assert decode_xem_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('NAPRILC6USCTAY7NNXB4COVKQJL427NPCEERGKS6', '681f142c5ea4853063ed6dc3c13aaa8257cd7daf1109132a5e'),
        ('NAMOAVHFVPJ6FP32YP2GCM64WSRMKXA5KKYWWHPY', '6818e054e5abd3e2bf7ac3f46133dcb4a2c55c1d52b16b1df8')
])
def test_xem_encode(expected_text: str, hex_value: str) -> None:
    assert encode_xem_address(bytes.fromhex(hex_value)) == expected_text

