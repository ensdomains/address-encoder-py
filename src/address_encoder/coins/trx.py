from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.base58_ import base58_check_decode, base58_check_encode

encode_trx_address = base58_check_encode
decode_trx_address = base58_check_decode

trx = CoinCoder(
    name="trx",
    coin_type=195,
    encode=encode_trx_address,
    decode=decode_trx_address,
)
