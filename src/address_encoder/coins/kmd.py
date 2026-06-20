from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.base58_ import create_base58_versioned_decoder, create_base58_versioned_encoder

_p2pkh = (bytes([60]),)
_p2sh = (bytes([85]),)
encode_kmd_address = create_base58_versioned_encoder(_p2pkh[0], _p2sh[0])
decode_kmd_address = create_base58_versioned_decoder(_p2pkh, _p2sh)

kmd = CoinCoder(
    name="kmd",
    coin_type=141,
    encode=encode_kmd_address,
    decode=decode_kmd_address,
)
