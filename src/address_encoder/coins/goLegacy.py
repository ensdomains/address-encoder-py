from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.hex_ import create_hex_checksummed_decoder, create_hex_checksummed_encoder

encode_goLegacy_address = create_hex_checksummed_encoder()
decode_goLegacy_address = create_hex_checksummed_decoder()

goLegacy = CoinCoder(
    name="goLegacy",
    coin_type=6060,
    encode=encode_goLegacy_address,
    decode=decode_goLegacy_address,
)
