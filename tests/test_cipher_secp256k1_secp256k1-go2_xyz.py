import skycoin

def test_TestGejDouble():
    a = skycoin.secp256k1go.XYZ()
    aExp = skycoin.secp256k1go.XYZ()
    r = skycoin.secp256k1go.XYZ()
    err = skycoin.secp256k1go.FieldSetHex(a.X, b"79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798")
    assert err == skycoin.SKY_OK
    err = skycoin.secp256k1go.FieldSetHex(a.Y, b"483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8") 
    assert err == skycoin.SKY_OK
    err = skycoin.secp256k1go.FieldSetHex(a.X, b"01") 
    assert err == skycoin.SKY_OK
    err = skycoin.secp256k1go.FieldSetHex(aExp.X, b"7D152C041EA8E1DC2191843D1FA9DB55B68F88FEF695E2C791D40444B365AFC2") 
    assert err == skycoin.SKY_OK
    err = skycoin.secp256k1go.FieldSetHex(aExp.Y, b"56915849F52CC8F76F5FD7E4BF60DB4A43BF633E1B1383F85FE89164BFADCBDB") 
    assert err == skycoin.SKY_OK
    err = skycoin.secp256k1go.FieldSetHex(aExp.Z, b"9075B4EE4D4788CABB49F7F81C221151FA2F68914D0AA833388FA11FF621A970") 
    assert err == skycoin.SKY_OK
    err = skycoin.secp256k1go.XYZDouble(a, r)
    assert err == skycoin.SKY_OK
    err = skycoin.secp256k1go.XYZEquals(aExp, a)[0]
    assert err == skycoin.SKY_OK
