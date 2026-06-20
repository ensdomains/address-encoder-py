from __future__ import annotations

from address_encoder.types import CoinCoder
from address_encoder.utils.base58_ import base58_unchecked_decode, base58_unchecked_encode

encode_dcr_address = base58_unchecked_encode
decode_dcr_address = base58_unchecked_decode

dcr = CoinCoder(
    name="dcr",
    coin_type=42,
    encode=encode_dcr_address,
    decode=decode_dcr_address,
)

