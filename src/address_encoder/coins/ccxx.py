from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.bitcoin import BitcoinCoderParameters, create_bitcoin_decoder, create_bitcoin_encoder

_params = BitcoinCoderParameters(
    hrp="ccx",
    p2pkh_versions=(bytes([137]),),
    p2sh_versions=(bytes([75]), bytes([5]),),
)
encode_ccxx_address = create_bitcoin_encoder(_params)
decode_ccxx_address = create_bitcoin_decoder(_params)

ccxx = CoinCoder(
    name="ccxx",
    coin_type=571,
    encode=encode_ccxx_address,
    decode=decode_ccxx_address,
)
