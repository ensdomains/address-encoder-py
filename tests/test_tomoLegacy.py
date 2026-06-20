from __future__ import annotations

import pytest

from address_encoder.coins.tomoLegacy import decode_tomoLegacy_address, encode_tomoLegacy_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('0xf5C9206843DAe847DdFd551ef7b850895430EcA3', 'f5c9206843dae847ddfd551ef7b850895430eca3'),
        ('0x15813DAE07E373DC800690031A1385eB7faDe49F', '15813dae07e373dc800690031a1385eb7fade49f')
])
def test_tomoLegacy_decode(text: str, hex_value: str) -> None:
    assert decode_tomoLegacy_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('0xf5C9206843DAe847DdFd551ef7b850895430EcA3', 'f5c9206843dae847ddfd551ef7b850895430eca3'),
        ('0x15813DAE07E373DC800690031A1385eB7faDe49F', '15813dae07e373dc800690031a1385eb7fade49f')
])
def test_tomoLegacy_encode(expected_text: str, hex_value: str) -> None:
    assert encode_tomoLegacy_address(bytes.fromhex(hex_value)) == expected_text

