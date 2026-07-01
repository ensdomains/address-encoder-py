# address-encoder

[![CI](https://github.com/ensdomains/address-encoder-py/actions/workflows/test.yml/badge.svg)](https://github.com/ensdomains/address-encoder-py/actions/workflows/test.yml)

Encodes and decodes address formats for various cryptocurrencies.

Converts addresses between human-readable text and their native binary representations for use with [EIP-2304](https://eips.ethereum.org/EIPS/eip-2304) and ENS multichain resolution.

EVM compatible chains are either specified using SLIP-44 coin type or `0x80000000 | chainId` where `0x80000000` is the MSB (most significant bit) reserved at SLIP-44 and no coin types exist in that range. This is to avoid number collision with the existing coin types.

See [ENSIP-11](https://docs.ens.domains/ens-improvement-proposals/ensip-11-evmchain-address-resolution#specification) for more detail.

## Installation

```bash
pip install address-encoder
```

Available on [PyPI](https://pypi.org/project/address-encoder/).

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

### Direct coin imports

```python
from address_encoder.coins.btc import btc

decoded = btc.decode("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
```

### EVM chains

Many EVM chains are supported, but none of them (except ETH) are exported from `address_encoder.coins`. To encode or decode addresses for an EVM chain, use the ETH codec via `get_coder_by_coin_name`:

```python
from address_encoder import get_coder_by_coin_name

op = get_coder_by_coin_name("op")  # Optimism
decoded = op.decode("0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb")
```

You can also look up a codec by coin type:

```python
from address_encoder import get_coder_by_coin_type

op = get_coder_by_coin_type(2147483658)  # 0x80000000 | 10
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

#### Coin types

When adding a new coin, the **coin type** is a numeric identifier from [SLIP-44](https://github.com/satoshilabs/slips/blob/master/slip-0044.md). It must be an integer, not a coin name or symbol.

| Chain type | Coin type | Script |
| --- | --- | --- |
| Non-EVM (e.g. BTC, SOL) | SLIP-44 index (e.g. `0` for Bitcoin, `501` for Solana) | `scripts/generate_coin.py` |
| EVM (e.g. Optimism, Base) | Computed as `0x80000000 \| chainId` — enter the chain ID only | `scripts/add_evm_coin.py` |

If the coin is not listed in SLIP-44, open a PR to [add it there](https://github.com/satoshilabs/slips/blob/master/slip-0044.md) first.

## Package layout

- `address_encoder` — main API (`get_coder_by_coin_name`, `get_coder_by_coin_type`)
- `address_encoder.coins` — per-coin codecs
- `address_encoder.coders` — per-coin encode/decode function exports
- `address_encoder.consts` — SLIP-44 and EVM chain mappings
- `address_encoder.utils` — shared encoding primitives
