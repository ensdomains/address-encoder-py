from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.hex_ import create_hex_checksummed_decoder, create_hex_checksummed_encoder

encode_tfuel_address = create_hex_checksummed_encoder()
decode_tfuel_address = create_hex_checksummed_decoder()

tfuel = CoinCoder(
    name="tfuel",
    coin_type=589,
    encode=encode_tfuel_address,
    decode=decode_tfuel_address,
)
