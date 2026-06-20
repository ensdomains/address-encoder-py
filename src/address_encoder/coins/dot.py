from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.dot import create_dot_address_decoder, create_dot_address_encoder

encode_dot_address = create_dot_address_encoder(0)
decode_dot_address = create_dot_address_decoder(0)

dot = CoinCoder(
    name="dot",
    coin_type=354,
    encode=encode_dot_address,
    decode=decode_dot_address,
)
