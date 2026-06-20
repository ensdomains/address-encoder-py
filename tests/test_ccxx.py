from __future__ import annotations

import pytest

from address_encoder.coins.ccxx import decode_ccxx_address, encode_ccxx_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('XVVxhJAGNXP32xAcfCm1mVDLs5dCeodLjL', 'a914c7188637dfd328e6911d63da67cdbea52507dd3087'),
        ('XKcgJ1jyjwbGCE7wT6GRMKZGjFrkNs2sLb', 'a9145aac7ca95006faf9244907af1e2b873a6a58e1af87')
])
def test_ccxx_decode(text: str, hex_value: str) -> None:
    assert decode_ccxx_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('XVVxhJAGNXP32xAcfCm1mVDLs5dCeodLjL', 'a914c7188637dfd328e6911d63da67cdbea52507dd3087'),
        ('XKcgJ1jyjwbGCE7wT6GRMKZGjFrkNs2sLb', 'a9145aac7ca95006faf9244907af1e2b873a6a58e1af87')
])
def test_ccxx_encode(expected_text: str, hex_value: str) -> None:
    assert encode_ccxx_address(bytes.fromhex(hex_value)) == expected_text

