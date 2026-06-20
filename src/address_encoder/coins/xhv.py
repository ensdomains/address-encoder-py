from __future__ import annotations

from address_encoder.types import CoinCoder
from address_encoder.utils.base58_ import base58xmr_decode, base58xmr_encode

encode_xhv_address = base58xmr_encode
decode_xhv_address = base58xmr_decode

xhv = CoinCoder(
    name="xhv",
    coin_type=535,
    encode=encode_xhv_address,
    decode=decode_xhv_address,
)

