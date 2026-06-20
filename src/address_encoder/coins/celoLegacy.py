from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.hex_ import create_hex_checksummed_decoder, create_hex_checksummed_encoder

encode_celoLegacy_address = create_hex_checksummed_encoder()
decode_celoLegacy_address = create_hex_checksummed_decoder()

celoLegacy = CoinCoder(
    name="celoLegacy",
    coin_type=52752,
    encode=encode_celoLegacy_address,
    decode=decode_celoLegacy_address,
)
