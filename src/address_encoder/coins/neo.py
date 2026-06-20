from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.base58_ import base58_check_decode, base58_check_encode

encode_neo_address = base58_check_encode
decode_neo_address = base58_check_decode

neo = CoinCoder(
    name="neo",
    coin_type=888,
    encode=encode_neo_address,
    decode=decode_neo_address,
)
