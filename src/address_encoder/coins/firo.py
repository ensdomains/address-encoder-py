from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.base58_ import create_base58_versioned_decoder, create_base58_versioned_encoder

_p2pkh = (bytes([82]),)
_p2sh = (bytes([7]),)
encode_firo_address = create_base58_versioned_encoder(_p2pkh[0], _p2sh[0])
decode_firo_address = create_base58_versioned_decoder(_p2pkh, _p2sh)

firo = CoinCoder(
    name="firo",
    coin_type=136,
    encode=encode_firo_address,
    decode=decode_firo_address,
)
