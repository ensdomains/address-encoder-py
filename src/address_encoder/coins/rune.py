from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.bech32_ import create_bech32_decoder, create_bech32_encoder

encode_rune_address = create_bech32_encoder("thor")
decode_rune_address = create_bech32_decoder("thor")

rune = CoinCoder(
    name="rune",
    coin_type=931,
    encode=encode_rune_address,
    decode=decode_rune_address,
)
