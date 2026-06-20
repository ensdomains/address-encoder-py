from __future__ import annotations

from address_encoder.types import CoinCoder
from address_encoder.utils.base58_ import base58_unchecked_decode, base58_unchecked_encode

encode_ela_address = base58_unchecked_encode
decode_ela_address = base58_unchecked_decode

ela = CoinCoder(
    name="ela",
    coin_type=2305,
    encode=encode_ela_address,
    decode=decode_ela_address,
)

