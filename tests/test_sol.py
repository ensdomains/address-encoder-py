from __future__ import annotations

import pytest

from address_encoder.coins.sol import decode_sol_address, encode_sol_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('AHy6YZA8BsHgQfVkk7MbwpAN94iyN7Nf1zN4nPqUN32Q', '8a11e71b96cabbe3216e3153b09694f39fc85022cbc076f79846a3ab4d8c1991'),
        ('2gVkYWexTHR5Hb2aLeQN3tnngvWzisFKXDUPrgMHpdST', '18f9d8d877393bbbe8d697a8a2e52879cc7e84f467656d1cce6bab5a8d2637ec'),
        ('CNR8RPMxjY28VsPA6KFq3B8PUdZnrTSC5HSFwKPBR29Z', 'a8ed08e3e8fe204de45e7295cc1ad53db096621b878f8c546e5c09f5e48f70b4')
])
def test_sol_decode(text: str, hex_value: str) -> None:
    assert decode_sol_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('AHy6YZA8BsHgQfVkk7MbwpAN94iyN7Nf1zN4nPqUN32Q', '8a11e71b96cabbe3216e3153b09694f39fc85022cbc076f79846a3ab4d8c1991'),
        ('2gVkYWexTHR5Hb2aLeQN3tnngvWzisFKXDUPrgMHpdST', '18f9d8d877393bbbe8d697a8a2e52879cc7e84f467656d1cce6bab5a8d2637ec'),
        ('CNR8RPMxjY28VsPA6KFq3B8PUdZnrTSC5HSFwKPBR29Z', 'a8ed08e3e8fe204de45e7295cc1ad53db096621b878f8c546e5c09f5e48f70b4')
])
def test_sol_encode(expected_text: str, hex_value: str) -> None:
    assert encode_sol_address(bytes.fromhex(hex_value)) == expected_text

