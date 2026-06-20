from __future__ import annotations

import pytest

from address_encoder.coins.dgb import decode_dgb_address, encode_dgb_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('dgb1q6fdfum8w0052aqmqjhpcpjzuyg4jlwjy9jrwz9', '0014d25a9e6cee7be8ae836095c380c85c222b2fba44'),
        ('DPPWe2aK4aYj3rt3yvw9zstCDXrN6frS7a', '76a914c82c346ddb007e70fbb73edcbe104ecceea97bd188ac'),
        ('SRFLzWuizzCPQDc5qLM2L8pZkvFws6We3j', 'a9142b5feabcb3feb6c45f9b623a7f1bc16be7377db787')
])
def test_dgb_decode(text: str, hex_value: str) -> None:
    assert decode_dgb_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('dgb1q6fdfum8w0052aqmqjhpcpjzuyg4jlwjy9jrwz9', '0014d25a9e6cee7be8ae836095c380c85c222b2fba44'),
        ('DPPWe2aK4aYj3rt3yvw9zstCDXrN6frS7a', '76a914c82c346ddb007e70fbb73edcbe104ecceea97bd188ac'),
        ('SRFLzWuizzCPQDc5qLM2L8pZkvFws6We3j', 'a9142b5feabcb3feb6c45f9b623a7f1bc16be7377db787')
])
def test_dgb_encode(expected_text: str, hex_value: str) -> None:
    assert encode_dgb_address(bytes.fromhex(hex_value)) == expected_text

