from __future__ import annotations

import pytest

from address_encoder.coins.eos import decode_eos_address, encode_eos_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('EOS7pyZLEjxhkSBYnPJf585vcZrqdQoA4KsRHDej6i3vsnV7aseh9', '03831c26f94b3af1a5f73ec3b961bc617b35bd99afe74bc1fe2c15d6d09bd4a416'),
        ('EOS51imoRdUT7THtgrrVxPfYwRk3V5jVmrj18D7hbk1FQFexNmCv1', '02106b727b87e01b0a298253655e7b0848ce3f4ec152ae6574643c0400ec3d1816')
])
def test_eos_decode(text: str, hex_value: str) -> None:
    assert decode_eos_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('EOS7pyZLEjxhkSBYnPJf585vcZrqdQoA4KsRHDej6i3vsnV7aseh9', '03831c26f94b3af1a5f73ec3b961bc617b35bd99afe74bc1fe2c15d6d09bd4a416'),
        ('EOS51imoRdUT7THtgrrVxPfYwRk3V5jVmrj18D7hbk1FQFexNmCv1', '02106b727b87e01b0a298253655e7b0848ce3f4ec152ae6574643c0400ec3d1816')
])
def test_eos_encode(expected_text: str, hex_value: str) -> None:
    assert encode_eos_address(bytes.fromhex(hex_value)) == expected_text

