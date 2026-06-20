from __future__ import annotations

from collections.abc import Callable

from Crypto.Hash import keccak

from address_encoder.utils.bytes_ import bytes_to_hex, hex_to_bytes

Encoder = Callable[[bytes], str]
Decoder = Callable[[str], bytes]


def strip_hex_prefix(value: str) -> str:
    return value[2:] if value.startswith("0x") else value


def _raw_checksum_address(address: list[str], digest: bytes, length: int) -> str:
    for index in range(0, length, 2):
        if digest[index >> 1] >> 4 >= 8 and address[index]:
            address[index] = address[index].upper()
        if (digest[index >> 1] & 0x0F) >= 8 and address[index + 1]:
            address[index + 1] = address[index + 1].upper()
    return f"0x{''.join(address)}"


def checksum_address(address: str, chain_id: int | None = None) -> str:
    if chain_id is not None:
        hex_address = f"{chain_id}{address.lower()}"
        chars = list(hex_address[len(f"{chain_id}0x") :])
    else:
        hex_address = address[2:].lower()
        chars = list(hex_address)
    digest = keccak.new(digest_bits=256, data=hex_address.encode()).digest()
    return _raw_checksum_address(chars, digest, 40)


def is_address(address: str) -> bool:
    import re

    return bool(re.fullmatch(r"0x[a-fA-F0-9]{40}", address))


def is_valid_checksum_address(address: str, chain_id: int | None = None) -> bool:
    if not is_address(address):
        return False
    if address == checksum_address(address, chain_id):
        return True
    prefixless = strip_hex_prefix(address)
    if prefixless.lower() == prefixless:
        return True
    if prefixless.upper() == prefixless:
        return True
    return False


def create_hex_checksummed_encoder(chain_id: int | None = None) -> Encoder:
    def encode(source: bytes) -> str:
        return checksum_address(bytes_to_hex(source), chain_id)

    return encode


def create_hex_checksummed_decoder(chain_id: int | None = None) -> Decoder:
    def decode(source: str) -> bytes:
        if not is_valid_checksum_address(source, chain_id):
            raise ValueError("Unrecognised address format")
        return hex_to_bytes(source)

    return decode
