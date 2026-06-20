from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.hex_ import create_hex_checksummed_decoder, create_hex_checksummed_encoder

encode_nrgLegacy_address = create_hex_checksummed_encoder()
decode_nrgLegacy_address = create_hex_checksummed_decoder()

nrgLegacy = CoinCoder(
    name="nrgLegacy",
    coin_type=9797,
    encode=encode_nrgLegacy_address,
    decode=decode_nrgLegacy_address,
)
