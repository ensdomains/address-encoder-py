from __future__ import annotations

from dataclasses import dataclass

from address_encoder.utils.base58_ import (
    create_base58_versioned_decoder,
    create_base58_versioned_encoder,
)
from address_encoder.utils.bech32_ import (
    create_bech32_segwit_decoder,
    create_bech32_segwit_encoder,
)


@dataclass(frozen=True, slots=True)
class BitcoinCoderParameters:
    hrp: str
    p2pkh_versions: tuple[bytes, ...]
    p2sh_versions: tuple[bytes, ...]


def create_bitcoin_decoder(params: BitcoinCoderParameters):
    decode_bech32 = create_bech32_segwit_decoder(params.hrp)
    decode_base58 = create_base58_versioned_decoder(
        params.p2pkh_versions,
        params.p2sh_versions,
    )

    def decode(source: str) -> bytes:
        if source.lower().startswith(params.hrp + "1"):
            return decode_bech32(source)
        return decode_base58(source)

    return decode


def create_bitcoin_encoder(params: BitcoinCoderParameters):
    encode_bech32 = create_bech32_segwit_encoder(params.hrp)
    encode_base58 = create_base58_versioned_encoder(
        params.p2pkh_versions[0],
        params.p2sh_versions[0],
    )

    def encode(source: bytes) -> str:
        try:
            return encode_base58(source)
        except ValueError:
            return encode_bech32(source)

    return encode
