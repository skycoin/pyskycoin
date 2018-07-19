import skycoin
from tests.utils.skyerror import error


def freshSumRipemd160(b):
    rp160 = skycoin.cipher_Ripemd160()
    skycoin.SKY_cipher_HashRipemd160(b, rp160)
    return rp160


def freshSumSHA256(b):
    sha256 = skycoin.cipher_SHA256()
    skycoin.SKY_cipher_SumSHA256(b, sha256)
    return sha256


def test_TestHashRipemd160():
    r160 = skycoin.cipher_Ripemd160()
    _, b = skycoin.SKY_cipher_RandByte(128)
    assert skycoin.SKY_cipher_HashRipemd160(b, r160) == error["SKY_OK"]
    _, b = skycoin.SKY_cipher_RandByte(160)
    r = skycoin.cipher_Ripemd160()
    skycoin.SKY_cipher_HashRipemd160(b, r)
    assert r != skycoin.cipher_Ripemd160()

    _, b = skycoin.SKY_cipher_RandByte(256)
    r2 = skycoin.cipher_Ripemd160()
    skycoin.SKY_cipher_HashRipemd160(b, r2)
    assert r2 != skycoin.cipher_Ripemd160()
    assert r2 == freshSumRipemd160(b)


def test_TestRipemd160Set():
    h = skycoin.cipher_Ripemd160()
    _, b = skycoin.SKY_cipher_RandByte(21)
    assert skycoin.SKY_cipher_Ripemd160_Set(h, b) == error["SKY_ERROR"]
    _, b = skycoin.SKY_cipher_RandByte(100)
    assert skycoin.SKY_cipher_Ripemd160_Set(h, b) == error["SKY_ERROR"]
    _, b = skycoin.SKY_cipher_RandByte(19)
    assert skycoin.SKY_cipher_Ripemd160_Set(h, b) == error["SKY_ERROR"]
    _, b = skycoin.SKY_cipher_RandByte(0)
    assert skycoin.SKY_cipher_Ripemd160_Set(h, b) == error["SKY_ERROR"]
    _, b = skycoin.SKY_cipher_RandByte(20)
    assert skycoin.SKY_cipher_Ripemd160_Set(h, b) == error["SKY_OK"]
    _, b1 = skycoin.SKY_cipher_RandByte(20)
    skycoin.SKY_cipher_Ripemd160_Set(h, b1)
    assert h.compareToString(str(b))


def test_TestSHA256Set():
    h = skycoin.cipher_SHA256()
    _, b = skycoin.SKY_cipher_RandByte(33)
    assert skycoin.SKY_cipher_SHA256_Set(h, b) == error["SKY_ERROR"]
    _, b = skycoin.SKY_cipher_RandByte(100)
    assert skycoin.SKY_cipher_SHA256_Set(h, b) == error["SKY_ERROR"]
    _, b = skycoin.SKY_cipher_RandByte(31)
    assert skycoin.SKY_cipher_SHA256_Set(h, b) == error["SKY_ERROR"]
    _, b = skycoin.SKY_cipher_RandByte(0)
    assert skycoin.SKY_cipher_SHA256_Set(h, b) == error["SKY_ERROR"]
    _, b = skycoin.SKY_cipher_RandByte(32)
    assert skycoin.SKY_cipher_SHA256_Set(h, b) == error["SKY_OK"]


def test_TestSHA256Hex():
    h = skycoin.cipher_SHA256()
    _, b = skycoin.SKY_cipher_RandByte(32)
    skycoin.SKY_cipher_SHA256_Set(h, b)
    _, s = skycoin.SKY_cipher_SHA256_Hex(h)
    h2 = skycoin.cipher_SHA256()
    err = skycoin.SKY_cipher_SHA256FromHex(s, h2)
    assert err == error["SKY_OK"]
    assert h == h2
    _, s2 = skycoin.SKY_cipher_SHA256_Hex(h2)
    assert s2 == s


class struct_test:
    inputs = bytes
    outputs = bytes


def test_TestSHA256KnownValue():
    vals = []
    values = struct_test()
    values.inputs = b"skycoin"
    values.outputs = b"5a42c0643bdb465d90bf673b99c14f5fa02db71513249d904573d2b8b63d353d"
    vals.append(values)
    values.inputs = b"hello world"
    values.outputs = b"b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"
    vals.append(values)
    values.inputs = b"hello world asd awd awd awdapodawpokawpod "
    values.outputs = b"99d71f95cafe05ea2dddebc35b6083bd5af0e44850c9dc5139b4476c99950be4"

    for v in vals:
        b = v.inputs
        h = skycoin.cipher_SHA256()
        err = skycoin.SKY_cipher_SumSHA256(b, h)
        assert err == error["SKY_OK"]
        _, h = skycoin.SKY_cipher_SHA256_Hex(h)
        assert h == v.outputs


def test_TestSumSHA256():
    _, b = skycoin.SKY_cipher_RandByte(256)
    h1 = skycoin.cipher_SHA256()
    skycoin.SKY_cipher_SumSHA256(b, h1)
    assert h1 != skycoin.cipher_SHA256()

    _, c = skycoin.SKY_cipher_RandByte(256)
    h2 = skycoin.cipher_SHA256()
    skycoin.SKY_cipher_SumSHA256(c, h2)
    assert h2 != skycoin.cipher_SHA256()
    assert h2 == freshSumSHA256(c)


# Not implement
def test_TestSHA256FromHex():
    # Invalid hex hash
    h = skycoin.cipher_SHA256()
    err = skycoin.SKY_cipher_SHA256FromHex(b"cawcad", h)
    assert err == error["SKY_ERROR"]

    # Truncated hex hash
    _, b = skycoin.SKY_cipher_RandByte(128)
    h = skycoin.cipher_SHA256()
    skycoin.SKY_cipher_SumSHA256(b, h)


# Not implement
def test_TestMustSHA256FromHex():
    pass


def test_TestMustSumSHA256():
    _, b = skycoin.SKY_cipher_RandByte(128)
    h = skycoin.cipher_SHA256()
    err = skycoin.SKY_cipher_MustSumSHA256(b, 127, h)
    assert err == error["SKY_ERROR"]
    err = skycoin.SKY_cipher_MustSumSHA256(b, 129, h)
    assert err == error["SKY_ERROR"]
    err = skycoin.SKY_cipher_MustSumSHA256(b, 128, h)
    assert err == error["SKY_OK"]

    err = skycoin.SKY_cipher_MustSumSHA256(b, 128, h)
    assert h != skycoin.cipher_SHA256()
    assert h == freshSumSHA256(b)


def test_TestDoubleSHA256():
    _, b = skycoin.SKY_cipher_RandByte(128)
    h = skycoin.cipher_SHA256()
    skycoin.SKY_cipher_DoubleSHA256(b, h)
    assert h != skycoin.cipher_SHA256()
    assert h != freshSumSHA256(b)

def test_TestAddSHA256():
    pass