from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.eosio import create_eos_decoder, create_eos_encoder

encode_bts_address = create_eos_encoder("BTS")
decode_bts_address = create_eos_decoder("BTS")

bts = CoinCoder(
    name="bts",
    coin_type=308,
    encode=encode_bts_address,
    decode=decode_bts_address,
)
