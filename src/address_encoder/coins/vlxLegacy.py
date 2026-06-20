from __future__ import annotations

from address_encoder.types import CoinCoder
from address_encoder.utils.base58_ import base58_unchecked_decode, base58_unchecked_encode

encode_vlxLegacy_address = base58_unchecked_encode
decode_vlxLegacy_address = base58_unchecked_decode

vlxLegacy = CoinCoder(
    name="vlxLegacy",
    coin_type=574,
    encode=encode_vlxLegacy_address,
    decode=decode_vlxLegacy_address,
)

