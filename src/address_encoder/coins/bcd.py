from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.bitcoin import BitcoinCoderParameters, create_bitcoin_decoder, create_bitcoin_encoder

_params = BitcoinCoderParameters(
    hrp="bcd",
    p2pkh_versions=(bytes([0]),),
    p2sh_versions=(bytes([5]),),
)
encode_bcd_address = create_bitcoin_encoder(_params)
decode_bcd_address = create_bitcoin_decoder(_params)

bcd = CoinCoder(
    name="bcd",
    coin_type=999,
    encode=encode_bcd_address,
    decode=decode_bcd_address,
)
