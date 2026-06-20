from __future__ import annotations

import pytest

from address_encoder.coins.ada import decode_ada_address, encode_ada_address

@pytest.mark.parametrize(('text', 'hex_value'), [
        ('Ae2tdPwUPEZFRbyhz3cpfC2CumGzNkFBN2L42rcUc2yjQpEkxDbkPodpMAi', '83581cba970ad36654d8dd8f74274b733452ddeab9a62a397746be3c42ccdda000'),
        ('DdzFFzCqrhsiMfvZtvTgqbR5jT4UAMEwJCT2bBvWSTiN736tSSxhnhHbmJYUhTiuZGgojfi3jizinGRVUdBF9QHgWHi11nEVpwK36gC9', '83581c22fb739e75d1f34748c2f03365ac909aff4d5a47bad7b4231c62a949a101581e581c2374b70ae27c8cc324be7b97285bdde6eeb78354cf6d1110baa37da000'),
        ('addr1qx2fxv2umyhttkxyxp8x0dlpdt3k6cwng5pxj3jhsydzer3n0d3vllmyqwsx5wktcd8cc3sq835lu7drv2xwl2wywfgse35a3x', '019493315cd92eb5d8c4304e67b7e16ae36d61d34502694657811a2c8e337b62cfff6403a06a3acbc34f8c46003c69fe79a3628cefa9c47251'),
        ('addr1z8phkx6acpnf78fuvxn0mkew3l0fd058hzquvz7w36x4gten0d3vllmyqwsx5wktcd8cc3sq835lu7drv2xwl2wywfgs9yc0hh', '11c37b1b5dc0669f1d3c61a6fddb2e8fde96be87b881c60bce8e8d542f337b62cfff6403a06a3acbc34f8c46003c69fe79a3628cefa9c47251'),
        ('addr1yx2fxv2umyhttkxyxp8x0dlpdt3k6cwng5pxj3jhsydzerkr0vd4msrxnuwnccdxlhdjar77j6lg0wypcc9uar5d2shs2z78ve', '219493315cd92eb5d8c4304e67b7e16ae36d61d34502694657811a2c8ec37b1b5dc0669f1d3c61a6fddb2e8fde96be87b881c60bce8e8d542f'),
        ('addr1x8phkx6acpnf78fuvxn0mkew3l0fd058hzquvz7w36x4gt7r0vd4msrxnuwnccdxlhdjar77j6lg0wypcc9uar5d2shskhj42g', '31c37b1b5dc0669f1d3c61a6fddb2e8fde96be87b881c60bce8e8d542fc37b1b5dc0669f1d3c61a6fddb2e8fde96be87b881c60bce8e8d542f'),
        ('addr1gx2fxv2umyhttkxyxp8x0dlpdt3k6cwng5pxj3jhsydzer5pnz75xxcrzqf96k', '419493315cd92eb5d8c4304e67b7e16ae36d61d34502694657811a2c8e8198bd431b03'),
        ('addr128phkx6acpnf78fuvxn0mkew3l0fd058hzquvz7w36x4gtupnz75xxcrtw79hu', '51c37b1b5dc0669f1d3c61a6fddb2e8fde96be87b881c60bce8e8d542f8198bd431b03'),
        ('addr1vx2fxv2umyhttkxyxp8x0dlpdt3k6cwng5pxj3jhsydzers66hrl8', '619493315cd92eb5d8c4304e67b7e16ae36d61d34502694657811a2c8e'),
        ('addr1w8phkx6acpnf78fuvxn0mkew3l0fd058hzquvz7w36x4gtcyjy7wx', '71c37b1b5dc0669f1d3c61a6fddb2e8fde96be87b881c60bce8e8d542f')
])
def test_ada_decode(text: str, hex_value: str) -> None:
    assert decode_ada_address(text).hex() == hex_value.lower()

@pytest.mark.parametrize(('expected_text', 'hex_value'), [
        ('Ae2tdPwUPEZFRbyhz3cpfC2CumGzNkFBN2L42rcUc2yjQpEkxDbkPodpMAi', '83581cba970ad36654d8dd8f74274b733452ddeab9a62a397746be3c42ccdda000'),
        ('DdzFFzCqrhsiMfvZtvTgqbR5jT4UAMEwJCT2bBvWSTiN736tSSxhnhHbmJYUhTiuZGgojfi3jizinGRVUdBF9QHgWHi11nEVpwK36gC9', '83581c22fb739e75d1f34748c2f03365ac909aff4d5a47bad7b4231c62a949a101581e581c2374b70ae27c8cc324be7b97285bdde6eeb78354cf6d1110baa37da000'),
        ('addr1qx2fxv2umyhttkxyxp8x0dlpdt3k6cwng5pxj3jhsydzer3n0d3vllmyqwsx5wktcd8cc3sq835lu7drv2xwl2wywfgse35a3x', '019493315cd92eb5d8c4304e67b7e16ae36d61d34502694657811a2c8e337b62cfff6403a06a3acbc34f8c46003c69fe79a3628cefa9c47251'),
        ('addr1z8phkx6acpnf78fuvxn0mkew3l0fd058hzquvz7w36x4gten0d3vllmyqwsx5wktcd8cc3sq835lu7drv2xwl2wywfgs9yc0hh', '11c37b1b5dc0669f1d3c61a6fddb2e8fde96be87b881c60bce8e8d542f337b62cfff6403a06a3acbc34f8c46003c69fe79a3628cefa9c47251'),
        ('addr1yx2fxv2umyhttkxyxp8x0dlpdt3k6cwng5pxj3jhsydzerkr0vd4msrxnuwnccdxlhdjar77j6lg0wypcc9uar5d2shs2z78ve', '219493315cd92eb5d8c4304e67b7e16ae36d61d34502694657811a2c8ec37b1b5dc0669f1d3c61a6fddb2e8fde96be87b881c60bce8e8d542f'),
        ('addr1x8phkx6acpnf78fuvxn0mkew3l0fd058hzquvz7w36x4gt7r0vd4msrxnuwnccdxlhdjar77j6lg0wypcc9uar5d2shskhj42g', '31c37b1b5dc0669f1d3c61a6fddb2e8fde96be87b881c60bce8e8d542fc37b1b5dc0669f1d3c61a6fddb2e8fde96be87b881c60bce8e8d542f'),
        ('addr1gx2fxv2umyhttkxyxp8x0dlpdt3k6cwng5pxj3jhsydzer5pnz75xxcrzqf96k', '419493315cd92eb5d8c4304e67b7e16ae36d61d34502694657811a2c8e8198bd431b03'),
        ('addr128phkx6acpnf78fuvxn0mkew3l0fd058hzquvz7w36x4gtupnz75xxcrtw79hu', '51c37b1b5dc0669f1d3c61a6fddb2e8fde96be87b881c60bce8e8d542f8198bd431b03'),
        ('addr1vx2fxv2umyhttkxyxp8x0dlpdt3k6cwng5pxj3jhsydzers66hrl8', '619493315cd92eb5d8c4304e67b7e16ae36d61d34502694657811a2c8e'),
        ('addr1w8phkx6acpnf78fuvxn0mkew3l0fd058hzquvz7w36x4gtcyjy7wx', '71c37b1b5dc0669f1d3c61a6fddb2e8fde96be87b881c60bce8e8d542f')
])
def test_ada_encode(expected_text: str, hex_value: str) -> None:
    assert encode_ada_address(bytes.fromhex(hex_value)) == expected_text

