from __future__ import annotations

import pytest

from address_encoder.coins.flux import decode_flux_address, encode_flux_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('t1XWTigDqS5Dy9McwQc752ShtZV1ffTMJB3', '76a91495921ba2fc5277d8a35b0e2d339987d51681c51d88ac'),
        ('t3c51GjrkUg7pUiS8bzNdTnW2hD25egWUih', 'a914c008da0bbc92b35ff71f613ca10ff11e2a6ae2fe87')
])
def test_flux_decode(text: str, hex_value: str) -> None:
    assert decode_flux_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('t1XWTigDqS5Dy9McwQc752ShtZV1ffTMJB3', '76a91495921ba2fc5277d8a35b0e2d339987d51681c51d88ac'),
        ('t3c51GjrkUg7pUiS8bzNdTnW2hD25egWUih', 'a914c008da0bbc92b35ff71f613ca10ff11e2a6ae2fe87')
])
def test_flux_encode(expected_text: str, hex_value: str) -> None:
    assert encode_flux_address(bytes.fromhex(hex_value)) == expected_text

