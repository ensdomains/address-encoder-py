from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.bitcoin import BitcoinCoderParameters
from address_encoder.utils.zcash import create_zcash_decoder, create_zcash_encoder

_params = BitcoinCoderParameters(
    hrp="zs",
    p2pkh_versions=(bytes([28, 184]),),
    p2sh_versions=(bytes([28, 189]),),
)
encode_zec_address = create_zcash_encoder(_params)
decode_zec_address = create_zcash_decoder(_params)

zec = CoinCoder(
    name="zec",
    coin_type=133,
    encode=encode_zec_address,
    decode=decode_zec_address,
)
