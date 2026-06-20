from __future__ import annotations

import pytest

from address_encoder.coins.hive import decode_hive_address, encode_hive_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('STM8QykigLRi9ZUcNy1iXGY3KjRuCiLM8Ga49LHti1F8hgawKFc3K', '03d0519ddad62bd2a833bee5dc04011c08f77f66338c38d99c685dee1f454cd1b8')
])
def test_hive_decode(text: str, hex_value: str) -> None:
    assert decode_hive_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('STM8QykigLRi9ZUcNy1iXGY3KjRuCiLM8Ga49LHti1F8hgawKFc3K', '03d0519ddad62bd2a833bee5dc04011c08f77f66338c38d99c685dee1f454cd1b8')
])
def test_hive_encode(expected_text: str, hex_value: str) -> None:
    assert encode_hive_address(bytes.fromhex(hex_value)) == expected_text

