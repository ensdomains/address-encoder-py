from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.bitcoin import BitcoinCoderParameters, create_bitcoin_decoder, create_bitcoin_encoder

_params = BitcoinCoderParameters(
    hrp="ltc",
    p2pkh_versions=(bytes([48]),),
    p2sh_versions=(bytes([50]), bytes([5]),),
)
encode_ltc_address = create_bitcoin_encoder(_params)
decode_ltc_address = create_bitcoin_decoder(_params)

ltc = CoinCoder(
    name="ltc",
    coin_type=2,
    encode=encode_ltc_address,
    decode=decode_ltc_address,
)
