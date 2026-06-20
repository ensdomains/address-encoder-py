from __future__ import annotations

import pytest

from address_encoder.coins.near import decode_near_address, encode_near_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('9902c136629fc630416e50d4f2fef6aff867ea7e.lockup.near', '393930326331333636323966633633303431366535306434663266656636616666383637656137652e6c6f636b75702e6e656172'),
        ('blah.com', '626c61682e636f6d'),
        ('9685af3fe2dc231e5069ccff8ec6950eb961d42ebb9116a8ab9c0d38f9e45249', '39363835616633666532646332333165353036396363666638656336393530656239363164343265626239313136613861623963306433386639653435323439')
])
def test_near_decode(text: str, hex_value: str) -> None:
    assert decode_near_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('9902c136629fc630416e50d4f2fef6aff867ea7e.lockup.near', '393930326331333636323966633633303431366535306434663266656636616666383637656137652e6c6f636b75702e6e656172'),
        ('blah.com', '626c61682e636f6d'),
        ('9685af3fe2dc231e5069ccff8ec6950eb961d42ebb9116a8ab9c0d38f9e45249', '39363835616633666532646332333165353036396363666638656336393530656239363164343265626239313136613861623963306433386639653435323439')
])
def test_near_encode(expected_text: str, hex_value: str) -> None:
    assert encode_near_address(bytes.fromhex(hex_value)) == expected_text

