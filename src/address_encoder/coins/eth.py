from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.hex_ import create_hex_checksummed_decoder, create_hex_checksummed_encoder

encode_eth_address = create_hex_checksummed_encoder()
decode_eth_address = create_hex_checksummed_decoder()

eth = CoinCoder(
    name="eth",
    coin_type=60,
    encode=encode_eth_address,
    decode=decode_eth_address,
)
