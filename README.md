# address-encoder

Encodes and decodes address formats for various cryptocurrencies. Converts addresses between human-readable text and their native binary representations for use with [EIP-2304](https://eips.ethereum.org/EIPS/eip-2304) and ENS multichain resolution.

## Installation

Coming soon to PyPI. In the meantime, install from source.

For local development:

```bash
pip install -e ".[dev]"
```

## Usage

```python
from address_encoder import get_coder_by_coin_name

btc = get_coder_by_coin_name("btc")
decoded = btc.decode("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
encoded = btc.encode(decoded)
```

### Hex input

Encoders expect `bytes`. Convert hex strings with the utility helpers:

```python
from address_encoder import get_coder_by_coin_name
from address_encoder.utils import hex_to_bytes

btc = get_coder_by_coin_name("btc")
address = btc.encode(hex_to_bytes("0x76a91462e907b15cbf27d5425399ebf6f0fb50ebb88f1888ac"))
```

### Lazy loading

```python
from address_encoder.async_ import get_coder_by_coin_name_async

btc = await get_coder_by_coin_name_async("btc")
```

### Direct coin imports

```python
from address_encoder.coins.btc import btc

decoded = btc.decode("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
```

## Development

```bash
pytest
```

### Maintainer scripts

Interactive helpers for adding coins and keeping docs in sync:

```bash
python3 scripts/generate_coin.py          # scaffold a new non-EVM coin module and test
python3 scripts/add_evm_coin.py           # add EVM chain entries to coin maps
python3 scripts/format_supported_coins.py # regenerate docs/supported-cryptocurrencies.md
python3 scripts/prepublish_only.py        # run tests and verify the wheel builds
```

## Package layout

- `address_encoder` — main API (`get_coder_by_coin_name`, `get_coder_by_coin_type`)
- `address_encoder.coins` — per-coin codecs
- `address_encoder.coders` — per-coin encode/decode function exports
- `address_encoder.consts` — SLIP-44 and EVM chain mappings
- `address_encoder.utils` — shared encoding primitives
- `address_encoder.async_` — lazy-loading getters
