import skycoin
import tests.utils as utils
from random import randint

_testSeckey = [
    b"08efb79385c9a8b0d1c6f5f6511be0c6f6c2902963d874a3a4bacc18802528d3",
    b"78298d9ecdc0640c9ae6883201a53f4518055442642024d23c45858f45d0c3e6",
    b"04e04fe65bfa6ded50a12769a3bd83d7351b2dbff08c9bac14662b23a3294b9e",
    b"2f5141f1b75747996c5de77c911dae062d16ae48799052c04ead20ccd5afa113",

]


def test_Test_Abnormal_Keys2():
    for tt in _testSeckey:
        err, s = skycoin.SKY_base58_String2Hex(tt)
        assert err == skycoin.SKY_OK
        err, p = skycoin.SKY_secp256k1_PubkeyFromSeckey(s)
        assert err == skycoin.SKY_OK
        err = skycoin.SKY_secp256k1_VerifyPubkey(p)


def test_Test_Abnormal_Keys3():
    for tt in _testSeckey:
        err, s = skycoin.SKY_base58_String2Hex(tt)
        assert err == skycoin.SKY_OK
        err, p = skycoin.SKY_secp256k1_PubkeyFromSeckey(s)
        assert err == skycoin.SKY_OK
        n = randint(0, len(_testSeckey) - 1)
        err, s2 = skycoin.SKY_base58_String2Hex(_testSeckey[n])
        assert err == skycoin.SKY_OK
        err, p2 = skycoin.SKY_secp256k1_PubkeyFromSeckey(s2)
        assert err == skycoin.SKY_OK
        err, puba = skycoin.SKY_secp256k1_ECDH(p, s2)
        assert err == skycoin.SKY_OK
        err, pubb = skycoin.SKY_secp256k1_ECDH(p2, s)
        assert err == skycoin.SKY_OK
        assert puba == pubb
