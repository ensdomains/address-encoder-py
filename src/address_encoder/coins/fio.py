from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.eosio import create_eos_decoder, create_eos_encoder

encode_fio_address = create_eos_encoder("FIO")
decode_fio_address = create_eos_decoder("FIO")

fio = CoinCoder(
    name="fio",
    coin_type=235,
    encode=encode_fio_address,
    decode=decode_fio_address,
)
