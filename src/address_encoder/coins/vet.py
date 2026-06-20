from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.hex_ import create_hex_checksummed_decoder, create_hex_checksummed_encoder

encode_vet_address = create_hex_checksummed_encoder()
decode_vet_address = create_hex_checksummed_decoder()

vet = CoinCoder(
    name="vet",
    coin_type=818,
    encode=encode_vet_address,
    decode=decode_vet_address,
)
