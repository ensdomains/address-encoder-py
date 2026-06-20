from __future__ import annotations

import re

NEAR_ADDRESS_REGEX = re.compile(r"^(([a-z\d]+[\-_])*[a-z\d]+\.)*([a-z\d]+[\-_])*[a-z\d]+$")


def validate_near_address(address: str) -> bool:
    if len(address) < 2 or len(address) > 64:
        return False
    return bool(NEAR_ADDRESS_REGEX.fullmatch(address))
