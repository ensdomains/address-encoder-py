from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.bech32_ import create_bech32_decoder, create_bech32_encoder

encode_kava_address = create_bech32_encoder("kava")
decode_kava_address = create_bech32_decoder("kava")

kava = CoinCoder(
    name="kava",
    coin_type=459,
    encode=encode_kava_address,
    decode=decode_kava_address,
)
