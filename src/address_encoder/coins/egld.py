from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.bech32_ import create_bech32_decoder, create_bech32_encoder

encode_egld_address = create_bech32_encoder("erd")
decode_egld_address = create_bech32_decoder("erd")

egld = CoinCoder(
    name="egld",
    coin_type=508,
    encode=encode_egld_address,
    decode=decode_egld_address,
)
