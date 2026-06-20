from __future__ import annotations

import pytest

from address_encoder.coins.doge import decode_doge_address, encode_doge_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('DBXu2kgc3xtvCUWFcxFE3r9hEYgmuaaCyD', '76a9144620b70031f0e9437e374a2100934fba4911046088ac'),
        ('AF8ekvSf6eiSBRspJjnfzK6d1EM6pnPq3G', 'a914f8f5d99a9fc21aa676e74d15e7b8134557615bda87')
])
def test_doge_decode(text: str, hex_value: str) -> None:
    assert decode_doge_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('DBXu2kgc3xtvCUWFcxFE3r9hEYgmuaaCyD', '76a9144620b70031f0e9437e374a2100934fba4911046088ac'),
        ('AF8ekvSf6eiSBRspJjnfzK6d1EM6pnPq3G', 'a914f8f5d99a9fc21aa676e74d15e7b8134557615bda87')
])
def test_doge_encode(expected_text: str, hex_value: str) -> None:
    assert encode_doge_address(bytes.fromhex(hex_value)) == expected_text

