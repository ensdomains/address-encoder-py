from __future__ import annotations

from Crypto.Hash import RIPEMD160

from address_encoder.utils.base58_ import base58_unchecked_decode, base58_unchecked_encode


def _ripemd160(data: bytes) -> bytes:
    return RIPEMD160.new(data=data).digest()


def create_eos_encoder(prefix: str):
    def encode(source: bytes) -> str:
        checksummed = source + _ripemd160(source)[:4]
        return f"{prefix}{base58_unchecked_encode(checksummed)}"

    return encode


def create_eos_decoder(prefix: str):
    def decode(source: str) -> bytes:
        if not source.startswith(prefix):
            raise ValueError("Unrecognised address format")
        decoded = base58_unchecked_decode(source[len(prefix) :])
        data, checksum = decoded[:-4], decoded[-4:]
        if _ripemd160(data)[:4] != checksum:
            raise ValueError("Unrecognised address format")
        return data

    return decode
