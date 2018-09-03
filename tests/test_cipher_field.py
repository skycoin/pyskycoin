import skycoin

def test_TestFeInv():
    in_ = out_ = exp = skycoin.secp256k1go.Field()
    in_hex = b"813925AF112AAB8243F8CCBADE4CC7F63DF387263028DE6E679232A73A7F3C31"
    exp_hex = b"7F586430EA30F914965770F6098E492699C62EE1DF6CAFFA77681C179FDF3117"

    err = skycoin.secp256k1go.FieldSetHex(in_, in_hex) 
    assert err == skycoin.SKY_OK
    err = skycoin.secp256k1go.FieldSetHex(exp, exp_hex)
    assert err == skycoin.SKY_OK
    err = skycoin.secp256k1go.FieldInv(in_, out_)
    assert err == skycoin.SKY_OK
    assert out_ == exp
    err = skycoin.secp256k1go.FieldEquals(out_,exp)[1]
    assert err and True


