from __future__ import annotations

from address_encoder.types import CoinCoder
from address_encoder.utils.base58_ import base58_unchecked_decode, base58_unchecked_encode

encode_iost_address = base58_unchecked_encode
decode_iost_address = base58_unchecked_decode

iost = CoinCoder(
    name="iost",
    coin_type=291,
    encode=encode_iost_address,
    decode=decode_iost_address,
)

