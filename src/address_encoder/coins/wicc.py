from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.base58_ import create_base58_versioned_decoder, create_base58_versioned_encoder

_p2pkh = (bytes([73]),)
_p2sh = (bytes([51]),)
encode_wicc_address = create_base58_versioned_encoder(_p2pkh[0], _p2sh[0])
decode_wicc_address = create_base58_versioned_decoder(_p2pkh, _p2sh)

wicc = CoinCoder(
    name="wicc",
    coin_type=99999,
    encode=encode_wicc_address,
    decode=decode_wicc_address,
)
