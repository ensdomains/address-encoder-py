from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.base58_ import create_base58_versioned_decoder, create_base58_versioned_encoder

_p2pkh = (bytes([76]),)
_p2sh = (bytes([16]),)
encode_dash_address = create_base58_versioned_encoder(_p2pkh[0], _p2sh[0])
decode_dash_address = create_base58_versioned_decoder(_p2pkh, _p2sh)

dash = CoinCoder(
    name="dash",
    coin_type=5,
    encode=encode_dash_address,
    decode=decode_dash_address,
)
