from __future__ import annotations

import pytest

from address_encoder.coins.xtz import decode_xtz_address, encode_xtz_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('KT1BDEn6wobs7tDReKkGheXAhoq278TGaNn5', '011cd5f135e80fd8ebb6e43335b24ca6116edeba6900'),
        ('KT1BDEn6wobs7tDReKkGheXAhoq278TGaNn5', '011cd5f135e80fd8ebb6e43335b24ca6116edeba6900'),
        ('tz1XdRrrqrMfsFKA8iuw53xHzug9ipr6MuHq', '000083846eddd5d3c5ed96e962506253958649c84a74'),
        ('tz2Cfwk4ortcaqAGcVJKSxLiAdcFxXBLBoyY', '00012fcb1d9307f0b1f94c048ff586c09f46614c7e90'),
        ('tz3NdTPb3Ax2rVW2Kq9QEdzfYFkRwhrQRPhX', '0002193b2b3f6b8f8e1e6b39b4d442fc2b432f6427a8')
])
def test_xtz_decode(text: str, hex_value: str) -> None:
    assert decode_xtz_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('KT1BDEn6wobs7tDReKkGheXAhoq278TGaNn5', '011cd5f135e80fd8ebb6e43335b24ca6116edeba6900'),
        ('KT1BDEn6wobs7tDReKkGheXAhoq278TGaNn5', '011cd5f135e80fd8ebb6e43335b24ca6116edeba6900'),
        ('tz1XdRrrqrMfsFKA8iuw53xHzug9ipr6MuHq', '000083846eddd5d3c5ed96e962506253958649c84a74'),
        ('tz2Cfwk4ortcaqAGcVJKSxLiAdcFxXBLBoyY', '00012fcb1d9307f0b1f94c048ff586c09f46614c7e90'),
        ('tz3NdTPb3Ax2rVW2Kq9QEdzfYFkRwhrQRPhX', '0002193b2b3f6b8f8e1e6b39b4d442fc2b432f6427a8')
])
def test_xtz_encode(expected_text: str, hex_value: str) -> None:
    assert encode_xtz_address(bytes.fromhex(hex_value)) == expected_text

