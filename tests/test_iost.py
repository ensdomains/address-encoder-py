from __future__ import annotations

import pytest

from address_encoder.coins.iost import decode_iost_address, encode_iost_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('BkHuWzs6x2wUcuDwcodwQSaWUfZHiN7SfF3vBKy1U2Qg', '9fabf5897177aabbd3c3d6052b351fe6c6c36d603dba257eb5bad3a17930ca39')
])
def test_iost_decode(text: str, hex_value: str) -> None:
    assert decode_iost_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('BkHuWzs6x2wUcuDwcodwQSaWUfZHiN7SfF3vBKy1U2Qg', '9fabf5897177aabbd3c3d6052b351fe6c6c36d603dba257eb5bad3a17930ca39')
])
def test_iost_encode(expected_text: str, hex_value: str) -> None:
    assert encode_iost_address(bytes.fromhex(hex_value)) == expected_text

