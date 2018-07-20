import skycoin
from tests.utils.skyerror import error


def test_TestGejDouble():
    a = skycoin.secp256k1go__XYZ()
    aExp = skycoin.secp256k1go__XYZ()
    r = skycoin.secp256k1go__XYZ()
    err = skycoin.SKY_secp256k1go_Field_SetHex(
        a.X, "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798")
    assert err == error["SKY_OK"]
    skycoin.SKY_secp256k1go_Field_SetHex(a.Y, "483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8")
