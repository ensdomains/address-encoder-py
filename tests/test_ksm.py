from __future__ import annotations

import pytest

from address_encoder.coins.ksm import decode_ksm_address, encode_ksm_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('CpjsLDC1JFyrhm3ftC9Gs4QoyrkHKhZKtK7YqGTRFtTafgp', '0aff6865635ae11013a83835c019d44ec3f865145943f487ae82a8e7bed3a66b'),
        ('DDioZ6gLeKMc5xUCeSXRHZ5U43MH1Tsrmh8T3Gcg9Vxr6DY', '1c86776eda34405584e710a7363650afd1f2b38ef72836317b11ef1303a0ae72'),
        ('EDNfVHuNHrXsVTLMMNbp6Con5zESZJa3fkRc93AgahuMm99', '487ee7e677203b4209af2ffaec0f5068033c870c97fee18b31b4aee524089943')
])
def test_ksm_decode(text: str, hex_value: str) -> None:
    assert decode_ksm_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('CpjsLDC1JFyrhm3ftC9Gs4QoyrkHKhZKtK7YqGTRFtTafgp', '0aff6865635ae11013a83835c019d44ec3f865145943f487ae82a8e7bed3a66b'),
        ('DDioZ6gLeKMc5xUCeSXRHZ5U43MH1Tsrmh8T3Gcg9Vxr6DY', '1c86776eda34405584e710a7363650afd1f2b38ef72836317b11ef1303a0ae72'),
        ('EDNfVHuNHrXsVTLMMNbp6Con5zESZJa3fkRc93AgahuMm99', '487ee7e677203b4209af2ffaec0f5068033c870c97fee18b31b4aee524089943')
])
def test_ksm_encode(expected_text: str, hex_value: str) -> None:
    assert encode_ksm_address(bytes.fromhex(hex_value)) == expected_text

