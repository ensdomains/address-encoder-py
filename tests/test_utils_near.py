from __future__ import annotations

import pytest

from address_encoder.utils.near import validate_near_address


def test_root_name() -> None:
    assert validate_near_address("near")


def test_2ld() -> None:
    assert validate_near_address("alice.near")


def test_3ld() -> None:
    assert validate_near_address("alice.bob.near")


def test_64_char_account_id() -> None:
    assert validate_near_address("a" * 64)


def test_larger_than_64_chars() -> None:
    assert not validate_near_address("a" * 65)


def test_smaller_than_2_chars() -> None:
    assert not validate_near_address("a")


def test_non_alphanumeric() -> None:
    assert not validate_near_address("ƒelicia.near")


@pytest.mark.parametrize("separator", [".", "-", "_"])
def test_starting_separator(separator: str) -> None:
    assert not validate_near_address(f"{separator}near")


@pytest.mark.parametrize("separator", [".", "-", "_"])
def test_ending_separator(separator: str) -> None:
    assert not validate_near_address(f"near{separator}")


@pytest.mark.parametrize("separator", [".", "-", "_"])
def test_consecutive_separators(separator: str) -> None:
    assert not validate_near_address(f"alice{separator}{separator}near")

