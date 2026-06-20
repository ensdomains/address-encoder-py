from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.bech32_ import create_bech32_decoder, create_bech32_encoder

encode_ckb_address = create_bech32_encoder("ckb")
decode_ckb_address = create_bech32_decoder("ckb")

ckb = CoinCoder(
    name="ckb",
    coin_type=309,
    encode=encode_ckb_address,
    decode=decode_ckb_address,
)
