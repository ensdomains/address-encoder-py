from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.bitcoin import BitcoinCoderParameters, create_bitcoin_decoder, create_bitcoin_encoder

_params = BitcoinCoderParameters(
    hrp="sys",
    p2pkh_versions=(bytes([63]),),
    p2sh_versions=(bytes([5]),),
)
encode_sys_address = create_bitcoin_encoder(_params)
decode_sys_address = create_bitcoin_decoder(_params)

sys = CoinCoder(
    name="sys",
    coin_type=57,
    encode=encode_sys_address,
    decode=decode_sys_address,
)
