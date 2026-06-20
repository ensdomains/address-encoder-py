from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.bech32_ import create_bech32_decoder, create_bech32_encoder

encode_one_address = create_bech32_encoder("one")
decode_one_address = create_bech32_decoder("one")

one = CoinCoder(
    name="one",
    coin_type=1023,
    encode=encode_one_address,
    decode=decode_one_address,
)
