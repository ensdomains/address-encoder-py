from __future__ import annotations

from io import BytesIO

import cbor2

from address_encoder.utils.base58_ import base58_unchecked_decode, base58_unchecked_encode
from address_encoder.utils.crc32 import crc32

# Byron addresses are CBOR `[#6.24(address bytes), crc32(address bytes)]`
_ADDRESS_TAG = 24


def byron_encode(source: bytes) -> str:
    checksum = crc32(source)
    cbor_encoded = cbor2.dumps([cbor2.CBORTag(_ADDRESS_TAG, source), checksum])
    address = base58_unchecked_encode(cbor_encoded)
    if not address.startswith(("Ae2", "Ddz")):
        raise ValueError("Unrecognised address format")
    return address


def byron_decode(source: str) -> bytes:
    data = base58_unchecked_decode(source)
    stream = BytesIO(data)
    try:
        decoded = cbor2.CBORDecoder(stream).decode()
    except Exception as exc:
        raise ValueError("Unrecognised address format") from exc
    # Reject trailing bytes after the CBOR item
    if stream.tell() != len(data):
        raise ValueError("Unrecognised address format")

    if not isinstance(decoded, list) or len(decoded) != 2:
        raise ValueError("Unrecognised address format")

    tagged_address, checksum = decoded
    if (
        not isinstance(tagged_address, cbor2.CBORTag)
        or tagged_address.tag != _ADDRESS_TAG
        or not isinstance(tagged_address.value, bytes)
    ):
        raise ValueError("Unrecognised address format")
    value: bytes = tagged_address.value

    if type(checksum) is not int or crc32(value) != checksum:
        raise ValueError("Unrecognised address format")
    return value
