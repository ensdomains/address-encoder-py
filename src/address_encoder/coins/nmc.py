from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.base58_ import base58_check_decode, base58_check_encode

encode_nmc_address = base58_check_encode
decode_nmc_address = base58_check_decode

nmc = CoinCoder(
    name="nmc",
    coin_type=7,
    encode=encode_nmc_address,
    decode=decode_nmc_address,
)
