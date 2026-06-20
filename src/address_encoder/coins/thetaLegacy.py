from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.hex_ import create_hex_checksummed_decoder, create_hex_checksummed_encoder

encode_thetaLegacy_address = create_hex_checksummed_encoder()
decode_thetaLegacy_address = create_hex_checksummed_decoder()

thetaLegacy = CoinCoder(
    name="thetaLegacy",
    coin_type=500,
    encode=encode_thetaLegacy_address,
    decode=decode_thetaLegacy_address,
)
