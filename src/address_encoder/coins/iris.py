from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.bech32_ import create_bech32_decoder, create_bech32_encoder

encode_iris_address = create_bech32_encoder("iaa")
decode_iris_address = create_bech32_decoder("iaa")

iris = CoinCoder(
    name="iris",
    coin_type=566,
    encode=encode_iris_address,
    decode=decode_iris_address,
)
