import skycoin
import tests.utils

def test_TestFeInv():
    in_ = out_ = exp = skycoin.secp256k1go__Field()
    in_hex = b"813925AF112AAB8243F8CCBADE4CC7F63DF387263028DE6E679232A73A7F3C31"
    exp_hex = b"7F586430EA30F914965770F6098E492699C62EE1DF6CAFFA77681C179FDF3117"

    assert skycoin.SKY_secp256k1go_Field_SetHex(in_, in_hex) == skycoin.SKY_OK
    assert skycoin.SKY_secp256k1go_Field_SetHex(exp, exp_hex) == skycoin.SKY_OK
    assert skycoin.SKY_secp256k1go_Field_Inv(in_, out_) == skycoin.SKY_OK
    assert out_ == exp
    assert skycoin.SKY_secp256k1go_Field_Equals(out_,exp)[1] and True


