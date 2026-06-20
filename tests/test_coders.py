from __future__ import annotations

import importlib

import pytest

from address_encoder.consts.coin_maps import NON_EVM_COIN_NAME_TO_TYPE


@pytest.mark.parametrize("coin_name", sorted(NON_EVM_COIN_NAME_TO_TYPE))
def test_coders_export(coin_name: str) -> None:
    coders = importlib.import_module("address_encoder.coders")
    encoder = getattr(coders, f"encode_{coin_name}_address")
    decoder = getattr(coders, f"decode_{coin_name}_address")
    assert callable(encoder)
    assert callable(decoder)

