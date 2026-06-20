from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.hex_ import create_hex_checksummed_decoder, create_hex_checksummed_encoder

encode_tomoLegacy_address = create_hex_checksummed_encoder()
decode_tomoLegacy_address = create_hex_checksummed_decoder()

tomoLegacy = CoinCoder(
    name="tomoLegacy",
    coin_type=889,
    encode=encode_tomoLegacy_address,
    decode=decode_tomoLegacy_address,
)
