from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.hex_ import create_hex_checksummed_decoder, create_hex_checksummed_encoder

encode_poaLegacy_address = create_hex_checksummed_encoder()
decode_poaLegacy_address = create_hex_checksummed_decoder()

poaLegacy = CoinCoder(
    name="poaLegacy",
    coin_type=178,
    encode=encode_poaLegacy_address,
    decode=decode_poaLegacy_address,
)
