from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.base58_ import create_base58_versioned_decoder, create_base58_versioned_encoder

_p2pkh = (bytes([55]),)
_p2sh = (bytes([117]),)
encode_ppc_address = create_base58_versioned_encoder(_p2pkh[0], _p2sh[0])
decode_ppc_address = create_base58_versioned_decoder(_p2pkh, _p2sh)

ppc = CoinCoder(
    name="ppc",
    coin_type=6,
    encode=encode_ppc_address,
    decode=decode_ppc_address,
)
