from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.bech32_ import create_bech32_segwit_decoder, create_bech32_segwit_encoder

encode_btm_address = create_bech32_segwit_encoder("bm")
decode_btm_address = create_bech32_segwit_decoder("bm")

btm = CoinCoder(
    name="btm",
    coin_type=153,
    encode=encode_btm_address,
    decode=decode_btm_address,
)
