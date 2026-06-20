from __future__ import annotations

from address_encoder.types import CoinCoder

from address_encoder.utils.bech32_ import create_bech32_decoder, create_bech32_encoder

encode_nostr_address = create_bech32_encoder("npub")
decode_nostr_address = create_bech32_decoder("npub")

nostr = CoinCoder(
    name="nostr",
    coin_type=1237,
    encode=encode_nostr_address,
    decode=decode_nostr_address,
)
