from __future__ import annotations

import pytest

from address_encoder.coins.bts import decode_bts_address, encode_bts_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('BTS8QykigLRi9ZUcNy1iXGY3KjRuCiLM8Ga49LHti1F8hgawKFc3K', '03d0519ddad62bd2a833bee5dc04011c08f77f66338c38d99c685dee1f454cd1b8')
])
def test_bts_decode(text: str, hex_value: str) -> None:
    assert decode_bts_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('BTS8QykigLRi9ZUcNy1iXGY3KjRuCiLM8Ga49LHti1F8hgawKFc3K', '03d0519ddad62bd2a833bee5dc04011c08f77f66338c38d99c685dee1f454cd1b8')
])
def test_bts_encode(expected_text: str, hex_value: str) -> None:
    assert encode_bts_address(bytes.fromhex(hex_value)) == expected_text

