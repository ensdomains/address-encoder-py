from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.eosio import create_eos_decoder, create_eos_encoder

encode_steem_address = create_eos_encoder("STM")
decode_steem_address = create_eos_decoder("STM")

steem = CoinCoder(
    name="steem",
    coin_type=135,
    encode=encode_steem_address,
    decode=decode_steem_address,
)
