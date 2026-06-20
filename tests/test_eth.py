from __future__ import annotations

import pytest

from address_encoder.coins.eth import decode_eth_address, encode_eth_address

PREFIXLESS_ADDRESS = "314159265dD8dbb310642f98f50C066173C1259b"
HEX_VALUE = "314159265dd8dbb310642f98f50c066173c1259b"


def test_eth_encode() -> None:
    assert encode_eth_address(bytes.fromhex(HEX_VALUE)) == f"0x{PREFIXLESS_ADDRESS}"


def test_eth_invalid_checksum() -> None:
    with pytest.raises(ValueError):
        decode_eth_address("0x314159265Dd8Dbb310642f98F50C066173C1259b")


@pytest.mark.parametrize(
    "text",
    [
        f"0x{PREFIXLESS_ADDRESS}",
        f"0x{PREFIXLESS_ADDRESS.lower()}",
        f"0x{PREFIXLESS_ADDRESS.upper()}",
    ],
)
def test_eth_decode(text: str) -> None:
    assert decode_eth_address(text) == bytes.fromhex(HEX_VALUE)

