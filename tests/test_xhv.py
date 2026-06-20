from __future__ import annotations

import pytest

from address_encoder.coins.xhv import decode_xhv_address, encode_xhv_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('hvs1VkXQ7qvBzrCuTofumZ52HNBhriXWP5kWcqZAG2VDXKuLwcCN5YaF2A4wmUXrZMGiz97eT9jXQBPp6vmRyTsk2ttY8z6YRU', 'f4b24b708551a04541bfc33b74edddf8180bee188a01b7581c66452619634bf0b54e866dc481be8f53d1d99a470080185e01c7760aac8c4b3e2336b6b1c53da731ff047530a5df')
])
def test_xhv_decode(text: str, hex_value: str) -> None:
    assert decode_xhv_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('hvs1VkXQ7qvBzrCuTofumZ52HNBhriXWP5kWcqZAG2VDXKuLwcCN5YaF2A4wmUXrZMGiz97eT9jXQBPp6vmRyTsk2ttY8z6YRU', 'f4b24b708551a04541bfc33b74edddf8180bee188a01b7581c66452619634bf0b54e866dc481be8f53d1d99a470080185e01c7760aac8c4b3e2336b6b1c53da731ff047530a5df')
])
def test_xhv_encode(expected_text: str, hex_value: str) -> None:
    assert encode_xhv_address(bytes.fromhex(hex_value)) == expected_text

