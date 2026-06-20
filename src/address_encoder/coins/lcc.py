from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.bitcoin import BitcoinCoderParameters, create_bitcoin_decoder, create_bitcoin_encoder

_params = BitcoinCoderParameters(
    hrp="lcc",
    p2pkh_versions=(bytes([28]),),
    p2sh_versions=(bytes([50]), bytes([5]),),
)
encode_lcc_address = create_bitcoin_encoder(_params)
decode_lcc_address = create_bitcoin_decoder(_params)

lcc = CoinCoder(
    name="lcc",
    coin_type=192,
    encode=encode_lcc_address,
    decode=decode_lcc_address,
)
