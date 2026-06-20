from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.hex_ import create_hex_checksummed_decoder, create_hex_checksummed_encoder

encode_ftmLegacy_address = create_hex_checksummed_encoder()
decode_ftmLegacy_address = create_hex_checksummed_decoder()

ftmLegacy = CoinCoder(
    name="ftmLegacy",
    coin_type=1007,
    encode=encode_ftmLegacy_address,
    decode=decode_ftmLegacy_address,
)
