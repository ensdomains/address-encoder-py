from __future__ import annotations

import pytest

from address_encoder.utils.evm import coin_type_to_evm_chain_id, evm_chain_id_to_coin_type, is_evm_coin_type


def test_is_evm_coin_type_non_evm() -> None:
    assert is_evm_coin_type(1000) is False


def test_is_evm_coin_type_evm() -> None:
    assert is_evm_coin_type(2147483658) is True


def test_evm_chain_id_to_coin_type_normal() -> None:
    assert evm_chain_id_to_coin_type(10) == 2147483658


def test_evm_chain_id_to_coin_type_too_large() -> None:
    with pytest.raises(ValueError, match="Invalid chainId"):
        evm_chain_id_to_coin_type(2147483648)


def test_coin_type_to_evm_chain_id_non_evm() -> None:
    with pytest.raises(ValueError, match="Coin type is not an EVM chain"):
        coin_type_to_evm_chain_id(1000)


def test_coin_type_to_evm_chain_id_evm() -> None:
    assert coin_type_to_evm_chain_id(2147483658) == 10

