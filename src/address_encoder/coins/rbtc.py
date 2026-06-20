from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.hex_ import create_hex_checksummed_decoder, create_hex_checksummed_encoder

encode_rbtc_address = create_hex_checksummed_encoder(30)
decode_rbtc_address = create_hex_checksummed_decoder(30)

rbtc = CoinCoder(
    name="rbtc",
    coin_type=137,
    encode=encode_rbtc_address,
    decode=decode_rbtc_address,
)
