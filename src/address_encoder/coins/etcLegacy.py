from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.hex_ import create_hex_checksummed_decoder, create_hex_checksummed_encoder

encode_etcLegacy_address = create_hex_checksummed_encoder()
decode_etcLegacy_address = create_hex_checksummed_decoder()

etcLegacy = CoinCoder(
    name="etcLegacy",
    coin_type=61,
    encode=encode_etcLegacy_address,
    decode=decode_etcLegacy_address,
)
