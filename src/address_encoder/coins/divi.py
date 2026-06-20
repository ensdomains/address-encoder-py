from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.base58_ import create_base58_versioned_decoder, create_base58_versioned_encoder

_p2pkh = (bytes([30]),)
_p2sh = (bytes([13]),)
encode_divi_address = create_base58_versioned_encoder(_p2pkh[0], _p2sh[0])
decode_divi_address = create_base58_versioned_decoder(_p2pkh, _p2sh)

divi = CoinCoder(
    name="divi",
    coin_type=301,
    encode=encode_divi_address,
    decode=decode_divi_address,
)
