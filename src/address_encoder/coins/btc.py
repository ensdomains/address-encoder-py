from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.bitcoin import BitcoinCoderParameters, create_bitcoin_decoder, create_bitcoin_encoder

_params = BitcoinCoderParameters(
    hrp="bc",
    p2pkh_versions=(bytes([0]),),
    p2sh_versions=(bytes([5]),),
)
encode_btc_address = create_bitcoin_encoder(_params)
decode_btc_address = create_bitcoin_decoder(_params)

btc = CoinCoder(
    name="btc",
    coin_type=0,
    encode=encode_btc_address,
    decode=decode_btc_address,
)
