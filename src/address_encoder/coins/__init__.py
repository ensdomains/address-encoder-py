from __future__ import annotations

import importlib
from collections.abc import Iterator, Mapping
from pathlib import Path
from typing import Any

from address_encoder.types import CoinCoder

_COINS_DIR = Path(__file__).parent
_COIN_MODULE_NAMES: tuple[str, ...] | None = None


def _coin_module_names() -> tuple[str, ...]:
    global _COIN_MODULE_NAMES
    if _COIN_MODULE_NAMES is None:
        _COIN_MODULE_NAMES = tuple(
            sorted(
                path.stem
                for path in _COINS_DIR.glob("*.py")
                if path.stem != "__init__"
            )
        )
    return _COIN_MODULE_NAMES


class _LazyCoins(Mapping[str, CoinCoder]):
    def __getitem__(self, key: str) -> CoinCoder:
        if key not in _coin_module_names():
            raise KeyError(key)
        return _load_coin(key)

    def __iter__(self) -> Iterator[str]:
        return iter(_coin_module_names())

    def __len__(self) -> int:
        return len(_coin_module_names())


_COINS: _LazyCoins | None = None


def _load_coin(name: str) -> CoinCoder:
    existing = globals().get(name)
    if isinstance(existing, CoinCoder):
        return existing
    module = importlib.import_module(f"{__name__}.{name}")
    coin = getattr(module, name, None)
    if coin is None:
        raise AttributeError(name)
    globals()[name] = coin
    return coin


def __getattr__(name: str) -> Any:
    if name == "COINS":
        global _COINS
        if _COINS is None:
            _COINS = _LazyCoins()
        return _COINS
    if name in _coin_module_names():
        return _load_coin(name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    return sorted([*_coin_module_names(), "COINS"])
