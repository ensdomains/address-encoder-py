from __future__ import annotations

import struct

from address_encoder.types import CoinCoder


def encode_hbar_address(source: bytes) -> str:
    if len(source) != 20:
        raise ValueError("Unrecognised address format")
    shard = struct.unpack(">I", source[0:4])[0]
    realm = struct.unpack(">Q", source[4:12])[0]
    account = struct.unpack(">Q", source[12:20])[0]
    return f"{shard}.{realm}.{account}"


def decode_hbar_address(source: str) -> bytes:
    components = source.split(".")
    if len(components) != 3:
        raise ValueError("Unrecognised address format")
    shard = int(components[0])
    realm = int(components[1])
    account = int(components[2])
    return struct.pack(">I", shard) + struct.pack(">Q", realm) + struct.pack(">Q", account)


hbar = CoinCoder(
    name="hbar",
    coin_type=3030,
    encode=encode_hbar_address,
    decode=decode_hbar_address,
)

