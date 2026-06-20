from __future__ import annotations

import pytest

from address_encoder.coins.neo import decode_neo_address, encode_neo_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('AXaXZjZGA3qhQRTCsyG5uFKr9HeShgVhTF', '17ad5cac596a1ef6c18ac1746dfd304f93964354b5')
])
def test_neo_decode(text: str, hex_value: str) -> None:
    assert decode_neo_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('AXaXZjZGA3qhQRTCsyG5uFKr9HeShgVhTF', '17ad5cac596a1ef6c18ac1746dfd304f93964354b5')
])
def test_neo_encode(expected_text: str, hex_value: str) -> None:
    assert encode_neo_address(bytes.fromhex(hex_value)) == expected_text

