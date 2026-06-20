from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.hex_ import create_hex_checksummed_decoder, create_hex_checksummed_encoder

encode_gnoLegacy_address = create_hex_checksummed_encoder()
decode_gnoLegacy_address = create_hex_checksummed_decoder()

gnoLegacy = CoinCoder(
    name="gnoLegacy",
    coin_type=700,
    encode=encode_gnoLegacy_address,
    decode=decode_gnoLegacy_address,
)
