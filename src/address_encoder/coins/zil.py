from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.bech32_ import create_bech32_decoder, create_bech32_encoder

encode_zil_address = create_bech32_encoder("zil")
decode_zil_address = create_bech32_decoder("zil")

zil = CoinCoder(
    name="zil",
    coin_type=313,
    encode=encode_zil_address,
    decode=decode_zil_address,
)
