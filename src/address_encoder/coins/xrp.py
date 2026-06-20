from __future__ import annotations

from address_encoder.types import CoinCoder
from address_encoder.utils.base58_ import create_base58xrp_codec

encode_xrp_address, decode_xrp_address = create_base58xrp_codec()

xrp = CoinCoder(
    name="xrp",
    coin_type=144,
    encode=encode_xrp_address,
    decode=decode_xrp_address,
)

