import skycoin
import tests.utils


def test_TestGejDouble():
    a = skycoin.secp256k1go__XYZ()
    aExp = skycoin.secp256k1go__XYZ()
    r = skycoin.secp256k1go__XYZ()
    assert skycoin.SKY_secp256k1go_Field_SetHex(
        a.X, b"79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798") == skycoin.SKY_OK
    assert skycoin.SKY_secp256k1go_Field_SetHex(
        a.Y, b"483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8") == skycoin.SKY_OK
    assert skycoin.SKY_secp256k1go_Field_SetHex(a.X, b"01") == skycoin.SKY_OK
    assert skycoin.SKY_secp256k1go_Field_SetHex(
        aExp.X, b"7D152C041EA8E1DC2191843D1FA9DB55B68F88FEF695E2C791D40444B365AFC2") == skycoin.SKY_OK
    assert skycoin.SKY_secp256k1go_Field_SetHex(
        aExp.Y, b"56915849F52CC8F76F5FD7E4BF60DB4A43BF633E1B1383F85FE89164BFADCBDB") == skycoin.SKY_OK
    assert skycoin.SKY_secp256k1go_Field_SetHex(
        aExp.Z, b"9075B4EE4D4788CABB49F7F81C221151FA2F68914D0AA833388FA11FF621A970") == skycoin.SKY_OK
    assert skycoin.SKY_secp256k1go_XYZ_Double(a, r) == skycoin.SKY_OK
    assert skycoin.SKY_secp256k1go_XYZ_Equals(aExp, a)
