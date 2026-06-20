from __future__ import annotations


def hex_to_bytes(hex_value: str) -> bytes:
    hex_string = hex_value[2:] if hex_value.startswith("0x") else hex_value
    if len(hex_string) % 2:
        hex_string = f"0{hex_string}"
    try:
        return bytes.fromhex(hex_string)
    except ValueError as exc:
        raise ValueError(f'Invalid hex sequence in "{hex_string}".') from exc


def bytes_to_hex(data: bytes) -> str:
    return f"0x{data.hex()}"


def hex_to_string(hex_value: str) -> str:
    return hex_to_bytes(hex_value).decode()


def bytes_to_string(data: bytes) -> str:
    return data.decode()


def string_to_bytes(value: str) -> bytes:
    return value.encode()


def bytes_to_base10(data: bytes) -> str:
    return str(int.from_bytes(data, "big"))


def base10_to_bytes(value: str) -> bytes:
    number = int(value)
    if number == 0:
        return b""
    length = (number.bit_length() + 7) // 8
    return number.to_bytes(length, "big")


bytes_to_hex_without_prefix = lambda data: data.hex()
hex_without_prefix_to_bytes = hex_to_bytes
