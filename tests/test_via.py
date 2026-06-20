from __future__ import annotations

import pytest

from address_encoder.coins.via import decode_via_address, encode_via_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('Vxgc5PCLkzNkDLkuduQEcrUBF1Z1UUHnav', '76a914f8d8b16d9409898a976b66bad157b91b71dc18ca88ac'),
        ('EYg9j8ieF6BQzS9doHnjg3Faj7SdAhfqnV', 'a914aa423f4ab9ea252abc360ec1dada62ef2527245987')
])
def test_via_decode(text: str, hex_value: str) -> None:
    assert decode_via_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('Vxgc5PCLkzNkDLkuduQEcrUBF1Z1UUHnav', '76a914f8d8b16d9409898a976b66bad157b91b71dc18ca88ac'),
        ('EYg9j8ieF6BQzS9doHnjg3Faj7SdAhfqnV', 'a914aa423f4ab9ea252abc360ec1dada62ef2527245987')
])
def test_via_encode(expected_text: str, hex_value: str) -> None:
    assert encode_via_address(bytes.fromhex(hex_value)) == expected_text

