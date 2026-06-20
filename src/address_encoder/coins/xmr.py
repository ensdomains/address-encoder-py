from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.base58_ import base58xmr_decode, base58xmr_encode

encode_xmr_address = base58xmr_encode
decode_xmr_address = base58xmr_decode

xmr = CoinCoder(
    name="xmr",
    coin_type=128,
    encode=encode_xmr_address,
    decode=decode_xmr_address,
)
