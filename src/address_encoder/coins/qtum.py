from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.base58_ import base58_check_decode, base58_check_encode

encode_qtum_address = base58_check_encode
decode_qtum_address = base58_check_decode

qtum = CoinCoder(
    name="qtum",
    coin_type=2301,
    encode=encode_qtum_address,
    decode=decode_qtum_address,
)
