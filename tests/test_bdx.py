from __future__ import annotations

import pytest

from address_encoder.coins.bdx import decode_bdx_address, encode_bdx_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('bxdBHRJaUhrFjfHLVESP2KQ7j56LVXhgxBCiJB2fdKvuauVSUpxAqVF3gTvEx9fcd4MditoVxumV3VYFyY35S9TK19JAmCMXz', 'd101a272642ddf45581910432620975c8a3385df68e1bb3d3cfe4ce1c97b4c5ecab46cca3eca869e100670ba171e59a77b5b8543ecdabc9aaa9f861374856e3e10a8dd024d2d')
])
def test_bdx_decode(text: str, hex_value: str) -> None:
    assert decode_bdx_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('bxdBHRJaUhrFjfHLVESP2KQ7j56LVXhgxBCiJB2fdKvuauVSUpxAqVF3gTvEx9fcd4MditoVxumV3VYFyY35S9TK19JAmCMXz', 'd101a272642ddf45581910432620975c8a3385df68e1bb3d3cfe4ce1c97b4c5ecab46cca3eca869e100670ba171e59a77b5b8543ecdabc9aaa9f861374856e3e10a8dd024d2d')
])
def test_bdx_encode(expected_text: str, hex_value: str) -> None:
    assert encode_bdx_address(bytes.fromhex(hex_value)) == expected_text

