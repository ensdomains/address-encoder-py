from __future__ import annotations

import pytest

from address_encoder.coins.strat import decode_strat_address, encode_strat_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('SdMCMmLjD6NK8ssWt5nH2gtv6XkQXErBRs', '76a914b01cb711ec63be7441c350907682a73d00bf7d2888ac'),
        ('STrATiSwHPf36VbqWMUaduaN57A791YP9c', '76a91447e5efb0d23a8ffa492d33df862a93e039ab622088ac')
])
def test_strat_decode(text: str, hex_value: str) -> None:
    assert decode_strat_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('SdMCMmLjD6NK8ssWt5nH2gtv6XkQXErBRs', '76a914b01cb711ec63be7441c350907682a73d00bf7d2888ac'),
        ('STrATiSwHPf36VbqWMUaduaN57A791YP9c', '76a91447e5efb0d23a8ffa492d33df862a93e039ab622088ac')
])
def test_strat_encode(expected_text: str, hex_value: str) -> None:
    assert encode_strat_address(bytes.fromhex(hex_value)) == expected_text

