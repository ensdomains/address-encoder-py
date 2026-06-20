from __future__ import annotations

from address_encoder.types import CoinCoder
from address_encoder.utils.base58_ import base58_unchecked_decode, base58_unchecked_encode

encode_srm_address = base58_unchecked_encode
decode_srm_address = base58_unchecked_decode

srm = CoinCoder(
    name="srm",
    coin_type=573,
    encode=encode_srm_address,
    decode=decode_srm_address,
)

