from __future__ import annotations

from address_encoder.types import CoinCoder
from address_encoder.utils.bytes_ import bytes_to_hex, hex_without_prefix_to_bytes
from address_encoder.utils.flow import validate_flow_address


_ADDRESS_LENGTH = 8


def encode_flow_address(source: bytes) -> str:
    if len(source) > _ADDRESS_LENGTH:
        bytes_value = source[-_ADDRESS_LENGTH:]
    else:
        bytes_value = bytes(_ADDRESS_LENGTH - len(source)) + source
    return bytes_to_hex(bytes_value).lower()


def decode_flow_address(source: str) -> bytes:
    if not validate_flow_address(int(source, 0)):
        raise ValueError("Unrecognised address format")
    stripped = source[2:] if source.startswith("0x") else source
    return hex_without_prefix_to_bytes(stripped)


flow = CoinCoder(
    name="flow",
    coin_type=539,
    encode=encode_flow_address,
    decode=decode_flow_address,
)

