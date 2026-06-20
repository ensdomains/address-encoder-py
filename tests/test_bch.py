from __future__ import annotations

import pytest

from address_encoder.coins.bch import decode_bch_address, encode_bch_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('1BpEi6DfDAUFd7GtittLSdBeYJvcoaVggu', '76a91476a04053bda0a88bda5177b86a15c3b29f55987388ac'),
        ('1KXrWXciRDZUpQwQmuM1DbwsKDLYAYsVLR', '76a914cb481232299cd5743151ac4b2d63ae198e7bb0a988ac'),
        ('16w1D5WRVKJuZUsSRzdLp9w3YGcgoxDXb', '76a914011f28e473c95f4013d7d53ec5fbc3b42df8ed1088ac'),
        ('3CWFddi6m4ndiGyKqzYvsFYagqDLPVMTzC', 'a91476a04053bda0a88bda5177b86a15c3b29f55987387'),
        ('3LDsS579y7sruadqu11beEJoTjdFiFCdX4', 'a914cb481232299cd5743151ac4b2d63ae198e7bb0a987'),
        ('31nwvkZwyPdgzjBJZXfDmSWsC4ZLKpYyUw', 'a914011f28e473c95f4013d7d53ec5fbc3b42df8ed1087')
])
def test_bch_decode(text: str, hex_value: str) -> None:
    assert decode_bch_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('bitcoincash:qpm2qsznhks23z7629mms6s4cwef74vcwvy22gdx6a', '76a91476a04053bda0a88bda5177b86a15c3b29f55987388ac'),
        ('bitcoincash:qr95sy3j9xwd2ap32xkykttr4cvcu7as4y0qverfuy', '76a914cb481232299cd5743151ac4b2d63ae198e7bb0a988ac'),
        ('bitcoincash:qqq3728yw0y47sqn6l2na30mcw6zm78dzqre909m2r', '76a914011f28e473c95f4013d7d53ec5fbc3b42df8ed1088ac'),
        ('bitcoincash:ppm2qsznhks23z7629mms6s4cwef74vcwvn0h829pq', 'a91476a04053bda0a88bda5177b86a15c3b29f55987387'),
        ('bitcoincash:pr95sy3j9xwd2ap32xkykttr4cvcu7as4yc93ky28e', 'a914cb481232299cd5743151ac4b2d63ae198e7bb0a987'),
        ('bitcoincash:pqq3728yw0y47sqn6l2na30mcw6zm78dzq5ucqzc37', 'a914011f28e473c95f4013d7d53ec5fbc3b42df8ed1087')
])
def test_bch_decode_canonical(text: str, hex_value: str) -> None:
    assert decode_bch_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('bitcoincash:qpm2qsznhks23z7629mms6s4cwef74vcwvy22gdx6a', '76a91476a04053bda0a88bda5177b86a15c3b29f55987388ac'),
        ('bitcoincash:qr95sy3j9xwd2ap32xkykttr4cvcu7as4y0qverfuy', '76a914cb481232299cd5743151ac4b2d63ae198e7bb0a988ac'),
        ('bitcoincash:qqq3728yw0y47sqn6l2na30mcw6zm78dzqre909m2r', '76a914011f28e473c95f4013d7d53ec5fbc3b42df8ed1088ac'),
        ('bitcoincash:ppm2qsznhks23z7629mms6s4cwef74vcwvn0h829pq', 'a91476a04053bda0a88bda5177b86a15c3b29f55987387'),
        ('bitcoincash:pr95sy3j9xwd2ap32xkykttr4cvcu7as4yc93ky28e', 'a914cb481232299cd5743151ac4b2d63ae198e7bb0a987'),
        ('bitcoincash:pqq3728yw0y47sqn6l2na30mcw6zm78dzq5ucqzc37', 'a914011f28e473c95f4013d7d53ec5fbc3b42df8ed1087')
])
def test_bch_encode(expected_text: str, hex_value: str) -> None:
    assert encode_bch_address(bytes.fromhex(hex_value)) == expected_text

