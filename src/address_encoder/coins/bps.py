from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.base58_ import create_base58_versioned_decoder, create_base58_versioned_encoder

_p2pkh = (bytes([0]),)
_p2sh = (bytes([5]),)
encode_bps_address = create_base58_versioned_encoder(_p2pkh[0], _p2sh[0])
decode_bps_address = create_base58_versioned_decoder(_p2pkh, _p2sh)

bps = CoinCoder(
    name="bps",
    coin_type=576,
    encode=encode_bps_address,
    decode=decode_bps_address,
)
