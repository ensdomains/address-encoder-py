from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.base58_ import create_base58_versioned_decoder, create_base58_versioned_encoder

_p2pkh = (bytes([11]),)
_p2sh = (bytes([5]),)
encode_cca_address = create_base58_versioned_encoder(_p2pkh[0], _p2sh[0])
decode_cca_address = create_base58_versioned_decoder(_p2pkh, _p2sh)

cca = CoinCoder(
    name="cca",
    coin_type=489,
    encode=encode_cca_address,
    decode=decode_cca_address,
)
