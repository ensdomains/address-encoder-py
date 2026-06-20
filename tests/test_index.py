from __future__ import annotations

import pytest

from address_encoder import get_coder_by_coin_name, get_coder_by_coin_type
from address_encoder.consts.coin_maps import (
    EVM_COIN_NAME_TO_TYPE,
    EVM_COIN_TYPE_TO_NAME,
    NON_EVM_COIN_NAME_TO_TYPE,
    NON_EVM_COIN_TYPE_TO_NAME,
)
from address_encoder.utils.evm import coin_type_to_evm_chain_id


def test_coin_name() -> None:
    coder = get_coder_by_coin_name("btc")
    assert coder.coin_type == 0
    assert coder.name == "btc"
    assert callable(coder.encode)
    assert callable(coder.decode)


def test_coin_type() -> None:
    coder = get_coder_by_coin_type(0)
    assert coder.coin_type == 0
    assert coder.name == "btc"
    assert callable(coder.encode)
    assert callable(coder.decode)


def test_evm_coin_name() -> None:
    coder = get_coder_by_coin_name("op")
    assert coder.coin_type == 2147483658
    assert coder.name == "op"
    assert coder.evm_chain_id == 10
    assert not getattr(coder, "is_unknown_chain", False)
    assert callable(coder.encode)
    assert callable(coder.decode)


def test_evm_coin_type() -> None:
    coder = get_coder_by_coin_type(2147483658)
    assert coder.coin_type == 2147483658
    assert coder.name == "op"
    assert coder.evm_chain_id == 10
    assert coder.is_unknown_chain is False
    assert callable(coder.encode)
    assert callable(coder.decode)


def test_unknown_evm_coin_type() -> None:
    coder = get_coder_by_coin_type(2147483659)
    assert coder.coin_type == 2147483659
    assert coder.name == "Unknown Chain (11)"
    assert coder.evm_chain_id == 11
    assert coder.is_unknown_chain is True
    assert callable(coder.encode)
    assert callable(coder.decode)


@pytest.mark.parametrize("coin_name", sorted(NON_EVM_COIN_NAME_TO_TYPE))
def test_get_coder_by_coin_name_non_evm(coin_name: str) -> None:
    coder = get_coder_by_coin_name(coin_name)
    assert coder.name == coin_name
    assert coder.coin_type == NON_EVM_COIN_NAME_TO_TYPE[coin_name]
    assert callable(coder.encode)
    assert callable(coder.decode)


@pytest.mark.parametrize("coin_name", sorted(EVM_COIN_NAME_TO_TYPE))
def test_get_coder_by_coin_name_evm(coin_name: str) -> None:
    coder = get_coder_by_coin_name(coin_name)
    assert coder.name == coin_name
    assert coder.coin_type == EVM_COIN_NAME_TO_TYPE[coin_name]
    assert coder.evm_chain_id == coin_type_to_evm_chain_id(coder.coin_type)
    assert callable(coder.encode)
    assert callable(coder.decode)


@pytest.mark.parametrize("coin_type", sorted(NON_EVM_COIN_NAME_TO_TYPE.values()))
def test_get_coder_by_coin_type_non_evm(coin_type: int) -> None:
    coder = get_coder_by_coin_type(coin_type)
    assert coder.name == NON_EVM_COIN_TYPE_TO_NAME[coin_type][0]
    assert coder.coin_type == coin_type
    assert callable(coder.encode)
    assert callable(coder.decode)


@pytest.mark.parametrize("coin_type", sorted(EVM_COIN_NAME_TO_TYPE.values()))
def test_get_coder_by_coin_type_evm(coin_type: int) -> None:
    coder = get_coder_by_coin_type(coin_type)
    assert coder.name == EVM_COIN_TYPE_TO_NAME[coin_type][0]
    assert coder.coin_type == coin_type
    assert coder.evm_chain_id == coin_type_to_evm_chain_id(coin_type)
    assert callable(coder.encode)
    assert callable(coder.decode)

