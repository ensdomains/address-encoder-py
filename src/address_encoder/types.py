from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import TypeAlias

Encoder = Callable[[bytes], str]
Decoder = Callable[[str], bytes]

ByteArray: TypeAlias = bytes


@dataclass(frozen=True, slots=True)
class CoinCoder:
    """Codec for a single cryptocurrency address format."""

    name: str
    coin_type: int
    encode: Encoder
    decode: Decoder
    evm_chain_id: int | None = None
    is_unknown_chain: bool = False
