from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.base58_ import create_base58_versioned_decoder, create_base58_versioned_encoder

_p2pkh = (bytes([30]),)
_p2sh = (bytes([13]),)
encode_lrg_address = create_base58_versioned_encoder(_p2pkh[0], _p2sh[0])
decode_lrg_address = create_base58_versioned_decoder(_p2pkh, _p2sh)

lrg = CoinCoder(
    name="lrg",
    coin_type=568,
    encode=encode_lrg_address,
    decode=decode_lrg_address,
)
