from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.base58_ import create_base58_versioned_decoder, create_base58_versioned_encoder

_p2pkh = (bytes([63]),)
_p2sh = (bytes([125]),)
encode_strat_address = create_base58_versioned_encoder(_p2pkh[0], _p2sh[0])
decode_strat_address = create_base58_versioned_decoder(_p2pkh, _p2sh)

strat = CoinCoder(
    name="strat",
    coin_type=105,
    encode=encode_strat_address,
    decode=decode_strat_address,
)
