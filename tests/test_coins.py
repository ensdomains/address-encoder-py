from __future__ import annotations

import pytest

from address_encoder.coins import COINS
from address_encoder.consts.coin_maps import NON_EVM_COIN_NAME_TO_TYPE


@pytest.mark.parametrize("coin_name", sorted(NON_EVM_COIN_NAME_TO_TYPE))
def test_coins_export(coin_name: str) -> None:
    obj = COINS[coin_name]
    assert obj.name == coin_name
    assert obj.coin_type == NON_EVM_COIN_NAME_TO_TYPE[coin_name]
    assert callable(obj.encode)
    assert callable(obj.decode)

