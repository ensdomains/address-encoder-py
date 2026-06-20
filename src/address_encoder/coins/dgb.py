from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.bitcoin import BitcoinCoderParameters, create_bitcoin_decoder, create_bitcoin_encoder

_params = BitcoinCoderParameters(
    hrp="dgb",
    p2pkh_versions=(bytes([30]),),
    p2sh_versions=(bytes([63]),),
)
encode_dgb_address = create_bitcoin_encoder(_params)
decode_dgb_address = create_bitcoin_decoder(_params)

dgb = CoinCoder(
    name="dgb",
    coin_type=20,
    encode=encode_dgb_address,
    decode=decode_dgb_address,
)
