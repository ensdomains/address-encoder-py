from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.bech32_ import create_bech32_decoder, create_bech32_encoder

encode_luna_address = create_bech32_encoder("terra")
decode_luna_address = create_bech32_decoder("terra")

luna = CoinCoder(
    name="luna",
    coin_type=330,
    encode=encode_luna_address,
    decode=decode_luna_address,
)
