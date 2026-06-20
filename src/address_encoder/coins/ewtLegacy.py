from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.hex_ import create_hex_checksummed_decoder, create_hex_checksummed_encoder

encode_ewtLegacy_address = create_hex_checksummed_encoder()
decode_ewtLegacy_address = create_hex_checksummed_decoder()

ewtLegacy = CoinCoder(
    name="ewtLegacy",
    coin_type=246,
    encode=encode_ewtLegacy_address,
    decode=decode_ewtLegacy_address,
)
