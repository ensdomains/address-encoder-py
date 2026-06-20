from __future__ import annotations

import pytest

from address_encoder.coins.rune import decode_rune_address, encode_rune_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('thor1kljxxccrheghavaw97u78le6yy3sdj7h696nl4', 'b7e4636303be517eb3ae2fb9e3ff3a212306cbd7'),
        ('thor1yv0mrrygnjs03zsrwrgqz4sa36evfw2a049l5p', '231fb18c889ca0f88a0370d001561d8eb2c4b95d')
])
def test_rune_decode(text: str, hex_value: str) -> None:
    assert decode_rune_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('thor1kljxxccrheghavaw97u78le6yy3sdj7h696nl4', 'b7e4636303be517eb3ae2fb9e3ff3a212306cbd7'),
        ('thor1yv0mrrygnjs03zsrwrgqz4sa36evfw2a049l5p', '231fb18c889ca0f88a0370d001561d8eb2c4b95d')
])
def test_rune_encode(expected_text: str, hex_value: str) -> None:
    assert encode_rune_address(bytes.fromhex(hex_value)) == expected_text

