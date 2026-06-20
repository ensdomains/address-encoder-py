from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.eosio import create_eos_decoder, create_eos_encoder

encode_abbc_address = create_eos_encoder("ABBC")
decode_abbc_address = create_eos_decoder("ABBC")

abbc = CoinCoder(
    name="abbc",
    coin_type=367,
    encode=encode_abbc_address,
    decode=decode_abbc_address,
)
