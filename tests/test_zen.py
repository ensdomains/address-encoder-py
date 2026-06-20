from __future__ import annotations

import pytest

from address_encoder.coins.zen import decode_zen_address, encode_zen_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('znc3p7CFNTsz1s6CceskrTxKevQLPoDK4cK', '20897843a3fcc6ab7d02d40946360c070b13cf7b9795'),
        ('zswRHzwXtwKVmP8ffKKgWz6A7TB97Fuzx7w', '2096b9d286b397a019f3a41ea6495dbce88d753f28a3')
])
def test_zen_decode(text: str, hex_value: str) -> None:
    assert decode_zen_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('znc3p7CFNTsz1s6CceskrTxKevQLPoDK4cK', '20897843a3fcc6ab7d02d40946360c070b13cf7b9795'),
        ('zswRHzwXtwKVmP8ffKKgWz6A7TB97Fuzx7w', '2096b9d286b397a019f3a41ea6495dbce88d753f28a3')
])
def test_zen_encode(expected_text: str, hex_value: str) -> None:
    assert encode_zen_address(bytes.fromhex(hex_value)) == expected_text

