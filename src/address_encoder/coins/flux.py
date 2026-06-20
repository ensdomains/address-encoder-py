from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.bitcoin import BitcoinCoderParameters
from address_encoder.utils.zcash import create_zcash_decoder, create_zcash_encoder

_params = BitcoinCoderParameters(
    hrp="za",
    p2pkh_versions=(bytes([28, 184]),),
    p2sh_versions=(bytes([28, 189]),),
)
encode_flux_address = create_zcash_encoder(_params)
decode_flux_address = create_zcash_decoder(_params)

flux = CoinCoder(
    name="flux",
    coin_type=19167,
    encode=encode_flux_address,
    decode=decode_flux_address,
)
