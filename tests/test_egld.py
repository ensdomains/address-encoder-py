from __future__ import annotations

import pytest

from address_encoder.coins.egld import decode_egld_address, encode_egld_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('erd1qdzvfpa7gqjsnfhdxhvcp2mlysc80uz60yjhxre3lwl00q0jd4nqgauy9q', '0344c487be402509a6ed35d980ab7f243077f05a7925730f31fbbef781f26d66')
])
def test_egld_decode(text: str, hex_value: str) -> None:
    assert decode_egld_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('erd1qdzvfpa7gqjsnfhdxhvcp2mlysc80uz60yjhxre3lwl00q0jd4nqgauy9q', '0344c487be402509a6ed35d980ab7f243077f05a7925730f31fbbef781f26d66')
])
def test_egld_encode(expected_text: str, hex_value: str) -> None:
    assert encode_egld_address(bytes.fromhex(hex_value)) == expected_text

