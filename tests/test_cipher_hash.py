import skycoin


def freshSumRipemd160(b, rp160):
    skycoin.SKY_cipher_HashRipemd160(b, rp160)


def freshSumSHA256(b, sha256):
    skycoin.SKY_cipher_SumSHA256(b, sha256)


def test_TestHashRipemd160():
    r160 = skycoin.cipher_Ripemd160()
    _, b = skycoin.SKY_cipher_RandByte(128)
    assert skycoin.SKY_cipher_HashRipemd160(b, r160) == 0
    _, b = skycoin.SKY_cipher_RandByte(160)
    r = skycoin.cipher_Ripemd160()
    skycoin.SKY_cipher_HashRipemd160(b, r)
    assert r != skycoin.cipher_Ripemd160()

    _, b = skycoin.SKY_cipher_RandByte(256)
    r2 = skycoin.cipher_Ripemd160()
    skycoin.SKY_cipher_HashRipemd160(b, r2)
    assert r2 != skycoin.cipher_Ripemd160()
    r3 = skycoin.cipher_Ripemd160()
    freshSumRipemd160(b, r3)
    assert r2 == r3


def test_TestRipemd160Set():
    h = skycoin.cipher_Ripemd160()
    _, b = skycoin.SKY_cipher_RandByte(21)
    assert skycoin.SKY_cipher_Ripemd160_Set(h, b) != 0
    _, b = skycoin.SKY_cipher_RandByte(100)
    assert skycoin.SKY_cipher_Ripemd160_Set(h, b) != 0
    _, b = skycoin.SKY_cipher_RandByte(19)
    assert skycoin.SKY_cipher_Ripemd160_Set(h, b) != 0
    _, b = skycoin.SKY_cipher_RandByte(0)
    assert skycoin.SKY_cipher_Ripemd160_Set(h, b) != 0
    _, b = skycoin.SKY_cipher_RandByte(20)
    assert skycoin.SKY_cipher_Ripemd160_Set(h, b) == 0
    _, b1 = skycoin.SKY_cipher_RandByte(20)
    skycoin.SKY_cipher_Ripemd160_Set(h, b1)
    #not finish

def test_TestSHA256Set():
    h = skycoin.cipher_SHA256()