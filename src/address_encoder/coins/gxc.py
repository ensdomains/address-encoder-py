from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.eosio import create_eos_decoder, create_eos_encoder

encode_gxc_address = create_eos_encoder("GXC")
decode_gxc_address = create_eos_decoder("GXC")

gxc = CoinCoder(
    name="gxc",
    coin_type=2303,
    encode=encode_gxc_address,
    decode=decode_gxc_address,
)
