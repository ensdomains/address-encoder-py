from __future__ import annotations

from address_encoder.types import CoinCoder
from address_encoder.utils.bech32_ import create_bech32_decoder, create_bech32_encoder

_hrp = "avax"
_decode_bech32 = create_bech32_decoder(_hrp)
_encode_bech32 = create_bech32_encoder(_hrp)


def encode_avax_address(source: bytes) -> str:
    return _encode_bech32(source)


def decode_avax_address(source: str) -> bytes:
    address = source
    chain_id, _, possible_addr = source.partition("-")
    if possible_addr:
        address = possible_addr
    else:
        chain_id = ""
    return _decode_bech32(address)


avax = CoinCoder(
    name="avax",
    coin_type=9000,
    encode=encode_avax_address,
    decode=decode_avax_address,
)

