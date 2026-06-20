from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.eosio import create_eos_decoder, create_eos_encoder

encode_hive_address = create_eos_encoder("STM")
decode_hive_address = create_eos_decoder("STM")

hive = CoinCoder(
    name="hive",
    coin_type=825,
    encode=encode_hive_address,
    decode=decode_hive_address,
)
