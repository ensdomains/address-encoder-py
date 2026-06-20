from __future__ import annotations

from address_encoder.utils.hex_ import is_valid_checksum_address

PREFIXLESS_ADDRESS = "314159265dD8dbb310642f98f50C066173C1259b"


def test_valid_checksum_address() -> None:
    assert is_valid_checksum_address(f"0x{PREFIXLESS_ADDRESS}")


def test_all_lowercased_address() -> None:
    assert is_valid_checksum_address(f"0x{PREFIXLESS_ADDRESS.lower()}")


def test_all_uppercased_address() -> None:
    assert is_valid_checksum_address(f"0x{PREFIXLESS_ADDRESS.upper()}")


def test_invalid_checksum_address() -> None:
    assert not is_valid_checksum_address("0x314159265Dd8Dbb310642f98F50C066173C1259b")


def test_non_hex() -> None:
    assert not is_valid_checksum_address("0x1234567890abcdefghijklmnopqrstuvwxyz0123")

