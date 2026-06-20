from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.bech32_ import create_bech32_decoder, create_bech32_encoder

encode_bnb_address = create_bech32_encoder("bnb")
decode_bnb_address = create_bech32_decoder("bnb")

bnb = CoinCoder(
    name="bnb",
    coin_type=714,
    encode=encode_bnb_address,
    decode=decode_bnb_address,
)
