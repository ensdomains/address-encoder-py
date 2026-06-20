from __future__ import annotations

import pytest

from address_encoder.coins.gxc import decode_gxc_address, encode_gxc_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('GXC6UKk9URcsCuGxLuRDqEuGzAqDkgKbG8AuWXFXsyzc2r9z7A1kw', '02d085655f8060a79a4b12b14e442b8a554ba867bdadce3c2dc39e1a42a01827c0')
])
def test_gxc_decode(text: str, hex_value: str) -> None:
    assert decode_gxc_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('GXC6UKk9URcsCuGxLuRDqEuGzAqDkgKbG8AuWXFXsyzc2r9z7A1kw', '02d085655f8060a79a4b12b14e442b8a554ba867bdadce3c2dc39e1a42a01827c0')
])
def test_gxc_encode(expected_text: str, hex_value: str) -> None:
    assert encode_gxc_address(bytes.fromhex(hex_value)) == expected_text

