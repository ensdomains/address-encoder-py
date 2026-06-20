from __future__ import annotations

from address_encoder.types import CoinCoder
from address_encoder.utils.bech32_ import create_plain_bech32_decoder, create_plain_bech32_encoder
from address_encoder.utils.byron import byron_decode, byron_encode

_hrp = "addr"
_limit = 104
_cardano_bech32_encode = create_plain_bech32_encoder(_hrp, _limit)
_cardano_bech32_decode = create_plain_bech32_decoder(_hrp, _limit)


def encode_ada_address(source: bytes) -> str:
    try:
        return byron_encode(source)
    except Exception:
        return _cardano_bech32_encode(source)


def decode_ada_address(source: str) -> bytes:
    if source.lower().startswith(_hrp):
        return _cardano_bech32_decode(source)
    return byron_decode(source)


ada = CoinCoder(
    name="ada",
    coin_type=1815,
    encode=encode_ada_address,
    decode=decode_ada_address,
)

