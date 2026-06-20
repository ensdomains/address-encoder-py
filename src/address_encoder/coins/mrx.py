from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.base58_ import base58_check_decode, base58_check_encode

encode_mrx_address = base58_check_encode
decode_mrx_address = base58_check_decode

mrx = CoinCoder(
    name="mrx",
    coin_type=326,
    encode=encode_mrx_address,
    decode=decode_mrx_address,
)
