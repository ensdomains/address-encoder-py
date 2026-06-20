from __future__ import annotations

import re

from address_encoder.types import CoinCoder
from address_encoder.utils.bech32_ import _bech32_encode, _to_words

_hrp = "hs"
_version = 0x00


def encode_hns_address(source: bytes) -> str:
    if len(source) != 20:
        raise ValueError("Unrecognised address format")
    return _bech32_encode(_hrp, [_version, *_to_words(source)], "bech32")


def decode_hns_address(source: str) -> bytes:
    from address_encoder.utils.bech32_ import _bech32_decode, _from_words

    prefix, words = _bech32_decode(source, "bech32")
    if prefix != _hrp:
        raise ValueError("Unrecognised address format")
    version = words[0]
    payload = _from_words(words[1:])
    if version != _version:
        raise ValueError("Unrecognised address format")
    if len(payload) != 20:
        raise ValueError("Unrecognised address format")
    return payload


hns = CoinCoder(
    name="hns",
    coin_type=5353,
    encode=encode_hns_address,
    decode=decode_hns_address,
)

