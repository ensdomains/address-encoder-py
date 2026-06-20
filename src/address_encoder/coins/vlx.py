from __future__ import annotations

from address_encoder.types import CoinCoder
from address_encoder.utils.base58_ import base58_unchecked_decode, base58_unchecked_encode

encode_vlx_address = base58_unchecked_encode
decode_vlx_address = base58_unchecked_decode

vlx = CoinCoder(
    name="vlx",
    coin_type=5655640,
    encode=encode_vlx_address,
    decode=decode_vlx_address,
)

