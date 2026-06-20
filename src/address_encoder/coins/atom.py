from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.bech32_ import create_bech32_decoder, create_bech32_encoder

encode_atom_address = create_bech32_encoder("cosmos")
decode_atom_address = create_bech32_decoder("cosmos")

atom = CoinCoder(
    name="atom",
    coin_type=118,
    encode=encode_atom_address,
    decode=decode_atom_address,
)
