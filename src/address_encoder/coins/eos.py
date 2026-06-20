from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.eosio import create_eos_decoder, create_eos_encoder

encode_eos_address = create_eos_encoder("EOS")
decode_eos_address = create_eos_decoder("EOS")

eos = CoinCoder(
    name="eos",
    coin_type=194,
    encode=encode_eos_address,
    decode=decode_eos_address,
)
