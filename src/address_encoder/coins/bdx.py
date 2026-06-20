from __future__ import annotations

from address_encoder.types import CoinCoder
from address_encoder.utils.base58_ import base58xmr_decode, base58xmr_encode

encode_bdx_address = base58xmr_encode
decode_bdx_address = base58xmr_decode

bdx = CoinCoder(
    name="bdx",
    coin_type=570,
    encode=encode_bdx_address,
    decode=decode_bdx_address,
)

