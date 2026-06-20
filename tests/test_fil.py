from __future__ import annotations

import pytest

from address_encoder.coins.fil import decode_fil_address, encode_fil_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('f0150', '009601'),
        ('f15ihq5ibzwki2b4ep2f46avlkrqzhpqgtga7pdrq', '01ea0f0ea039b291a0f08fd179e0556a8c3277c0d3'),
        ('f24vg6ut43yw2h2jqydgbg2xq7x6f4kub3bg6as6i', '02e54dea4f9bc5b47d261819826d5e1fbf8bc5503b'),
        ('f3vvmn62lofvhjd2ugzca6sof2j2ubwok6cj4xxbfzz4yuxfkgobpihhd2thlanmsh3w2ptld2gqkn2jvlss4a', '03ad58df696e2d4e91ea86c881e938ba4ea81b395e12797b84b9cf314b9546705e839c7a99d606b247ddb4f9ac7a3414dd')
])
def test_fil_decode(text: str, hex_value: str) -> None:
    assert decode_fil_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('f0150', '009601'),
        ('f15ihq5ibzwki2b4ep2f46avlkrqzhpqgtga7pdrq', '01ea0f0ea039b291a0f08fd179e0556a8c3277c0d3'),
        ('f24vg6ut43yw2h2jqydgbg2xq7x6f4kub3bg6as6i', '02e54dea4f9bc5b47d261819826d5e1fbf8bc5503b'),
        ('f3vvmn62lofvhjd2ugzca6sof2j2ubwok6cj4xxbfzz4yuxfkgobpihhd2thlanmsh3w2ptld2gqkn2jvlss4a', '03ad58df696e2d4e91ea86c881e938ba4ea81b395e12797b84b9cf314b9546705e839c7a99d606b247ddb4f9ac7a3414dd')
])
def test_fil_encode(expected_text: str, hex_value: str) -> None:
    assert encode_fil_address(bytes.fromhex(hex_value)) == expected_text

