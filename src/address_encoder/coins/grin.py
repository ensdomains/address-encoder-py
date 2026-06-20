from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.bech32_ import create_bech32_decoder, create_bech32_encoder

encode_grin_address = create_bech32_encoder("grin")
decode_grin_address = create_bech32_decoder("grin")

grin = CoinCoder(
    name="grin",
    coin_type=592,
    encode=encode_grin_address,
    decode=decode_grin_address,
)
