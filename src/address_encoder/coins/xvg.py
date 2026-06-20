from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.base58_ import create_base58_versioned_decoder, create_base58_versioned_encoder

_p2pkh = (bytes([30]),)
_p2sh = (bytes([33]),)
encode_xvg_address = create_base58_versioned_encoder(_p2pkh[0], _p2sh[0])
decode_xvg_address = create_base58_versioned_decoder(_p2pkh, _p2sh)

xvg = CoinCoder(
    name="xvg",
    coin_type=77,
    encode=encode_xvg_address,
    decode=decode_xvg_address,
)
