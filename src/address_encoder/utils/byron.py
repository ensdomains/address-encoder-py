from __future__ import annotations

import cbor2

from address_encoder.utils.base58_ import base58_unchecked_decode, base58_unchecked_encode
from address_encoder.utils.crc32 import crc32


def byron_encode(source: bytes) -> str:
    checksum = crc32(source)
    cbor_encoded = cbor2.dumps([cbor2.CBORTag(24, source), checksum])
    address = base58_unchecked_encode(cbor_encoded)
    if not address.startswith(("Ae2", "Ddz")):
        raise ValueError("Unrecognised address format")
    return address


def byron_decode(source: str) -> bytes:
    decoded = cbor2.loads(base58_unchecked_decode(source))
    tagged_address, checksum = decoded[0], decoded[1]
    value = tagged_address.value if isinstance(tagged_address, cbor2.CBORTag) else tagged_address
    if crc32(value) != checksum:
        raise ValueError("Unrecognised address format")
    return value
