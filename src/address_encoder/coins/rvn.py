from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.base58_ import create_base58_versioned_decoder, create_base58_versioned_encoder

_p2pkh = (bytes([60]),)
_p2sh = (bytes([122]),)
encode_rvn_address = create_base58_versioned_encoder(_p2pkh[0], _p2sh[0])
decode_rvn_address = create_base58_versioned_decoder(_p2pkh, _p2sh)

rvn = CoinCoder(
    name="rvn",
    coin_type=175,
    encode=encode_rvn_address,
    decode=decode_rvn_address,
)
