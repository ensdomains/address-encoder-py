from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.dot import create_dot_address_decoder, create_dot_address_encoder

encode_ksm_address = create_dot_address_encoder(2)
decode_ksm_address = create_dot_address_decoder(2)

ksm = CoinCoder(
    name="ksm",
    coin_type=434,
    encode=encode_ksm_address,
    decode=decode_ksm_address,
)
