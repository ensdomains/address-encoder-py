from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.bech32_ import create_bech32m_decoder, create_bech32m_encoder

encode_xch_address = create_bech32m_encoder("xch")
decode_xch_address = create_bech32m_decoder("xch")

xch = CoinCoder(
    name="xch",
    coin_type=8444,
    encode=encode_xch_address,
    decode=decode_xch_address,
)
