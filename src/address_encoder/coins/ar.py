from __future__ import annotations

from address_encoder.types import CoinCoder
from address_encoder.utils.base64url import base64url_nopad_decode, base64url_nopad_encode

encode_ar_address = base64url_nopad_encode
decode_ar_address = base64url_nopad_decode

ar = CoinCoder(
    name="ar",
    coin_type=472,
    encode=encode_ar_address,
    decode=decode_ar_address,
)

