from __future__ import annotations

import hashlib
from collections.abc import Callable, Sequence

import base58

XRP_ALPHABET = b"rpshnaf39wBUDNEGHJKLM4PQRST7VWXYZ2bcdeCg65jkm8oFqi1tuvAxyz"
XMR_BLOCK_LEN = [0, 2, 3, 5, 6, 7, 9, 10, 11]

Encoder = Callable[[bytes], str]
Decoder = Callable[[str], bytes]


def _double_sha256(data: bytes) -> bytes:
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()


def base58_unchecked_encode(data: bytes) -> str:
    return base58.b58encode(data).decode()


def base58_unchecked_decode(source: str) -> bytes:
    return base58.b58decode(source)


def base58_check_encode(data: bytes) -> str:
    return base58.b58encode_check(data).decode()


def base58_check_decode(source: str) -> bytes:
    return base58.b58decode_check(source)


def _base58_with_alphabet(data: bytes, alphabet: bytes) -> str:
    return base58.b58encode(data, alphabet=alphabet).decode()


def _base58_decode_with_alphabet(source: str, alphabet: bytes) -> bytes:
    return base58.b58decode(source, alphabet=alphabet)


def _checksum_encode(data: bytes, checksum_fn: Callable[[bytes], bytes], alphabet: bytes | None = None) -> str:
    payload = data + checksum_fn(data)
    if alphabet is None:
        return base58.b58encode(payload).decode()
    return base58.b58encode(payload, alphabet=alphabet).decode()


def _checksum_decode(source: str, checksum_fn: Callable[[bytes], bytes], alphabet: bytes | None = None) -> bytes:
    decoded = base58.b58decode(source, alphabet=alphabet) if alphabet else base58.b58decode(source)
    data, checksum = decoded[:-4], decoded[-4:]
    if checksum_fn(data)[:4] != checksum:
        raise ValueError("Invalid checksum")
    return data


def create_base58xrp_codec() -> tuple[Encoder, Decoder]:
    def checksum(data: bytes) -> bytes:
        return _double_sha256(data)[:4]

    def encode(data: bytes) -> str:
        return _checksum_encode(data, checksum, XRP_ALPHABET)

    def decode(source: str) -> bytes:
        return _checksum_decode(source, checksum, XRP_ALPHABET)

    return encode, decode


def base58xmr_encode(data: bytes) -> str:
    result = ""
    for index in range(0, len(data), 8):
        block = data[index : index + 8]
        encoded = base58.b58encode(block).decode()
        result += encoded.rjust(XMR_BLOCK_LEN[len(block)], "1")
    return result


def base58xmr_decode(source: str) -> bytes:
    result = bytearray()
    for index in range(0, len(source), 11):
        block = source[index : index + 11]
        block_len = XMR_BLOCK_LEN.index(len(block))
        decoded = base58.b58decode(block)
        padding = len(decoded) - block_len
        if any(byte != 0 for byte in decoded[:padding]):
            raise ValueError("base58xmr: wrong padding")
        result.extend(decoded[-block_len:])
    return bytes(result)


def create_base58_versioned_encoder(p2pkh_version: bytes, p2sh_version: bytes) -> Encoder:
    def encode(source: bytes) -> str:
        if source[0] == 0x76:
            if (
                source[1] != 0xA9
                or source[-2] != 0x88
                or source[-1] != 0xAC
            ):
                raise ValueError("Unrecognised address format")
            return base58_check_encode(p2pkh_version + source[3 : 3 + source[2]])
        if source[0] == 0xA9:
            if source[-1] != 0x87:
                raise ValueError("Unrecognised address format")
            return base58_check_encode(p2sh_version + source[2 : 2 + source[1]])
        raise ValueError("Unrecognised address format")

    return encode


def create_base58_versioned_decoder(
    p2pkh_versions: Sequence[bytes],
    p2sh_versions: Sequence[bytes],
) -> Decoder:
    def check_version(version: bytes, address: bytes) -> bool:
        return len(address) >= len(version) and address[: len(version)] == version

    def decode(source: str) -> bytes:
        address = base58_check_decode(source)
        if any(check_version(version, address) for version in p2pkh_versions):
            version_len = len(p2pkh_versions[0])
            return b"\x76\xa9\x14" + address[version_len:] + b"\x88\xac"
        if any(check_version(version, address) for version in p2sh_versions):
            version_len = len(p2sh_versions[0])
            return b"\xa9\x14" + address[version_len:] + b"\x87"
        raise ValueError("Unrecognised address format")

    return decode
