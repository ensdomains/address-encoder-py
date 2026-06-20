from __future__ import annotations

import base64

BASE64URL_ALPHABET = b"-_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def base64url_nopad_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode().rstrip("=")


def base64url_nopad_decode(source: str) -> bytes:
    padding = "=" * (-len(source) % 4)
    return base64.urlsafe_b64decode(source + padding)
