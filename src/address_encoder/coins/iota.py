from __future__ import annotations

from address_encoder.types import CoinCoder
from address_encoder.utils.bech32_ import create_bech32_decoder, create_bech32_encoder

_hrp = "iota"
_version = bytes([0x00])
_iota_bech32_encode = create_bech32_encoder(_hrp)
_iota_bech32_decode = create_bech32_decoder(_hrp)


def encode_iota_address(source: bytes) -> str:
    return _iota_bech32_encode(_version + source)


def decode_iota_address(source: str) -> bytes:
    return _iota_bech32_decode(source)[1:]


iota = CoinCoder(
    name="iota",
    coin_type=4218,
    encode=encode_iota_address,
    decode=decode_iota_address,
)

