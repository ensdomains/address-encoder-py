from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.bech32_ import create_bech32_decoder, create_bech32_encoder

encode_iotx_address = create_bech32_encoder("io")
decode_iotx_address = create_bech32_decoder("io")

iotx = CoinCoder(
    name="iotx",
    coin_type=304,
    encode=encode_iotx_address,
    decode=decode_iotx_address,
)
