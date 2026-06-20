from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.hex_ import create_hex_checksummed_decoder, create_hex_checksummed_encoder

encode_cloLegacy_address = create_hex_checksummed_encoder()
decode_cloLegacy_address = create_hex_checksummed_decoder()

cloLegacy = CoinCoder(
    name="cloLegacy",
    coin_type=820,
    encode=encode_cloLegacy_address,
    decode=decode_cloLegacy_address,
)
