from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.bitcoin import BitcoinCoderParameters, create_bitcoin_decoder, create_bitcoin_encoder

_params = BitcoinCoderParameters(
    hrp="btg",
    p2pkh_versions=(bytes([38]),),
    p2sh_versions=(bytes([23]),),
)
encode_btg_address = create_bitcoin_encoder(_params)
decode_btg_address = create_bitcoin_decoder(_params)

btg = CoinCoder(
    name="btg",
    coin_type=156,
    encode=encode_btg_address,
    decode=decode_btg_address,
)
