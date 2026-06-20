from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.hex_ import create_hex_checksummed_decoder, create_hex_checksummed_encoder

encode_ttLegacy_address = create_hex_checksummed_encoder()
decode_ttLegacy_address = create_hex_checksummed_decoder()

ttLegacy = CoinCoder(
    name="ttLegacy",
    coin_type=1001,
    encode=encode_ttLegacy_address,
    decode=decode_ttLegacy_address,
)
