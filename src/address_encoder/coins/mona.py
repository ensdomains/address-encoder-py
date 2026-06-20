from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.bitcoin import BitcoinCoderParameters, create_bitcoin_decoder, create_bitcoin_encoder

_params = BitcoinCoderParameters(
    hrp="mona",
    p2pkh_versions=(bytes([50]),),
    p2sh_versions=(bytes([55]), bytes([5]),),
)
encode_mona_address = create_bitcoin_encoder(_params)
decode_mona_address = create_bitcoin_decoder(_params)

mona = CoinCoder(
    name="mona",
    coin_type=22,
    encode=encode_mona_address,
    decode=decode_mona_address,
)
