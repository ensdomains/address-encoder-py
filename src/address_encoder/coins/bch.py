from __future__ import annotations

from address_encoder.types import CoinCoder
from address_encoder.utils.base58_ import create_base58_versioned_decoder
from address_encoder.utils.bch import decode_bch_address_to_type_and_hash, encode_bch_address_with_version

_p2pkh_versions = (bytes([0x00]),)
_p2sh_versions = (bytes([0x05]),)
_bch_base58_decode = create_base58_versioned_decoder(_p2pkh_versions, _p2sh_versions)


def encode_bch_address(source: bytes) -> str:
    if source[0] == 0x76:
        if source[1] != 0xA9 or source[-2] != 0x88 or source[-1] != 0xAC:
            raise ValueError("Unrecognised address format")
        return encode_bch_address_with_version(0, source[3 : 3 + source[2]])
    if source[0] == 0xA9:
        if source[-1] != 0x87:
            raise ValueError("Unrecognised address format")
        return encode_bch_address_with_version(8, source[2 : 2 + source[1]])
    raise ValueError("Unrecognised address format")


def decode_bch_address(source: str) -> bytes:
    try:
        return _bch_base58_decode(source)
    except ValueError:
        address_type, hash_bytes = decode_bch_address_to_type_and_hash(source)
        if address_type == 0:
            return b"\x76\xa9\x14" + hash_bytes + b"\x88\xac"
        if address_type == 8:
            return b"\xa9\x14" + hash_bytes + b"\x87"
        raise ValueError("Unrecognised address format") from None


bch = CoinCoder(
    name="bch",
    coin_type=145,
    encode=encode_bch_address,
    decode=decode_bch_address,
)

