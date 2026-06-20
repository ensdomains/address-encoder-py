from __future__ import annotations

import pytest

from address_encoder.coins.ltc import decode_ltc_address, encode_ltc_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('LaMT348PWRnrqeeWArpwQPbuanpXDZGEUz', '76a914a5f4d12ce3685781b227c1f39548ddef429e978388ac'),
        ('MQMcJhpWHYVeQArcZR3sBgyPZxxRtnH441', 'a914b48297bff5dadecc5f36145cec6a5f20d57c8f9b87'),
        ('ltc1qdp7p2rpx4a2f80h7a4crvppczgg4egmv5c78w8', '0014687c150c26af5493befeed7036043812115ca36c')
])
def test_ltc_decode(text: str, hex_value: str) -> None:
    assert decode_ltc_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('LaMT348PWRnrqeeWArpwQPbuanpXDZGEUz', '76a914a5f4d12ce3685781b227c1f39548ddef429e978388ac'),
        ('MQMcJhpWHYVeQArcZR3sBgyPZxxRtnH441', 'a914b48297bff5dadecc5f36145cec6a5f20d57c8f9b87'),
        ('ltc1qdp7p2rpx4a2f80h7a4crvppczgg4egmv5c78w8', '0014687c150c26af5493befeed7036043812115ca36c')
])
def test_ltc_encode(expected_text: str, hex_value: str) -> None:
    assert encode_ltc_address(bytes.fromhex(hex_value)) == expected_text

