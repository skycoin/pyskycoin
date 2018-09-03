import skycoin

def freshSumRipemd160(b):
    rp160 = skycoin.cipher.Ripemd160()
    skycoin.cipher.HashRipemd160(b, rp160)
    return rp160


def freshSumSHA256(b):
    sha256 = skycoin.cipher.SHA256()
    skycoin.cipher.SumSHA256(b, sha256)
    return sha256


def test_TestHashRipemd160():
    r160 = skycoin.cipher.Ripemd160()
    _, b = skycoin.cipher.RandByte(128)
    assert skycoin.cipher.HashRipemd160(b, r160) == skycoin.SKY_OK
    _, b = skycoin.cipher.RandByte(160)
    r = skycoin.cipher.Ripemd160()
    skycoin.cipher.HashRipemd160(b, r)
    assert r != skycoin.cipher.Ripemd160()

    _, b = skycoin.cipher.RandByte(256)
    r2 = skycoin.cipher.Ripemd160()
    skycoin.cipher.HashRipemd160(b, r2)
    assert r2 != skycoin.cipher.Ripemd160()
    assert r2 == freshSumRipemd160(b)


def test_TestRipemd160Set():
    h = skycoin.cipher.Ripemd160()
    _, b = skycoin.cipher.RandByte(21)
    err = skycoin.cipher.Ripemd160Set(h, b)
    assert err == skycoin.SKY_ErrInvalidLengthRipemd160
    _, b = skycoin.cipher.RandByte(100)
    err = skycoin.cipher.Ripemd160Set(h, b)
    assert err == skycoin.SKY_ErrInvalidLengthRipemd160
    _, b = skycoin.cipher.RandByte(19)
    err = skycoin.cipher.Ripemd160Set(h, b)
    assert err == skycoin.SKY_ErrInvalidLengthRipemd160
    _, b = skycoin.cipher.RandByte(0)
    err = skycoin.cipher.Ripemd160Set(h, b)
    assert err  == skycoin.SKY_ErrInvalidLengthRipemd160
    _, b = skycoin.cipher.RandByte(20)
    err = skycoin.cipher.Ripemd160Set(h, b)
    assert err == skycoin.SKY_OK
    _, b1 = skycoin.cipher.RandByte(20)
    skycoin.cipher.Ripemd160Set(h, b1)
    assert h.compareToString(str(b))


def test_TestSHA256Set():
    h = skycoin.cipher.SHA256()
    _, b = skycoin.cipher.RandByte(33)
    err = skycoin.cipher.SHA256Set(h, b)
    assert err == skycoin.SKY_ErrInvalidLengthSHA256
    _, b = skycoin.cipher.RandByte(100)
    err = skycoin.cipher.SHA256Set(h, b)
    assert err == skycoin.SKY_ErrInvalidLengthSHA256
    _, b = skycoin.cipher.RandByte(31)
    err = skycoin.cipher.SHA256Set(h, b) 
    assert err == skycoin.SKY_ErrInvalidLengthSHA256
    _, b = skycoin.cipher.RandByte(0)
    err = skycoin.cipher.SHA256Set(h, b)
    assert err == skycoin.SKY_ErrInvalidLengthSHA256
    _, b = skycoin.cipher.RandByte(32)
    err = skycoin.cipher.SHA256Set(h, b)
    assert err == skycoin.SKY_OK
    _, b = skycoin.cipher.RandByte(32)
    skycoin.cipher.SHA256Set(h, b)
    assert h.toStr()[:] == b


def test_TestSHA256Hex():
    h = skycoin.cipher.SHA256()
    _, b = skycoin.cipher.RandByte(32)
    skycoin.cipher.SHA256Set(h, b)
    _, s = skycoin.cipher.SHA256Hex(h)
    h2 = skycoin.cipher.SHA256()
    err = skycoin.cipher.SHA256FromHex(s, h2)
    assert err == skycoin.SKY_OK
    assert h == h2
    _, s2 = skycoin.cipher.SHA256Hex(h2)
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
        h = skycoin.cipher.SHA256()
        err = skycoin.cipher.SumSHA256(b, h)
        assert err == skycoin.SKY_OK
        _, h = skycoin.cipher.SHA256Hex(h)
        assert h == v.outputs


def test_TestSumSHA256():
    _, b = skycoin.cipher.RandByte(256)
    h1 = skycoin.cipher.SHA256()
    skycoin.cipher.SumSHA256(b, h1)
    assert h1 != skycoin.cipher.SHA256()

    _, c = skycoin.cipher.RandByte(256)
    h2 = skycoin.cipher.SHA256()
    skycoin.cipher.SumSHA256(c, h2)
    assert h2 != skycoin.cipher.SHA256()
    assert h2 == freshSumSHA256(c)


def test_TestSHA256FromHex():
    # Invalid hex hash
    h = skycoin.cipher.SHA256()
    err = skycoin.cipher.SHA256FromHex(b"cawcad", h)
    assert err == skycoin.SKY_ERROR

    # Truncated hex hash
    _, b = skycoin.cipher.RandByte(128)
    h = skycoin.cipher.SHA256()
    skycoin.cipher.SumSHA256(b, h)
    h_bytes = h.toStr()
    h1 = skycoin.cipher.SHA256()
    err = skycoin.cipher.SHA256FromHex(h_bytes[:int(len(h_bytes) / 2)], h1)
    assert err == skycoin.SKY_ERROR

    # Valid hex hash
    h2 = skycoin.cipher.SHA256()
    err, b = skycoin.cipher.SHA256Hex(h)
    err = skycoin.cipher.SHA256FromHex(b, h2)
    assert h == h2
    assert err == skycoin.SKY_OK


def test_TestDoubleSHA256():
    _, b = skycoin.cipher.RandByte(128)
    h = skycoin.cipher.SHA256()
    skycoin.cipher.DoubleSHA256(b, h)
    assert h != skycoin.cipher.SHA256()
    assert h != freshSumSHA256(b)


def test_TestAddSHA256():
    _, b = skycoin.cipher.RandByte(128)
    h = skycoin.cipher.SHA256()
    skycoin.cipher.SumSHA256(b, h)
    _, c = skycoin.cipher.RandByte(64)
    i = skycoin.cipher.SHA256()
    skycoin.cipher.SumSHA256(c, i)
    add = skycoin.cipher.SHA256()
    err = skycoin.cipher.AddSHA256(h, i, add)
    assert err == skycoin.SKY_OK
    assert add != skycoin.cipher.SHA256()
    assert add != h
    assert add != i


def test_TestXorSHA256():
    _, b = skycoin.cipher.RandByte(128)
    _, c = skycoin.cipher.RandByte(128)
    h = skycoin.cipher.SHA256()
    i = skycoin.cipher.SHA256()
    err = skycoin.cipher.SumSHA256(b, h)
    assert err == skycoin.SKY_OK
    err = skycoin.cipher.SumSHA256(c, i)
    assert err == skycoin.SKY_OK
    temp = skycoin.cipher.SHA256()
    temp2 = skycoin.cipher.SHA256()
    err = skycoin.cipher.SHA256Xor(h, i, temp) 
    assert err == skycoin.SKY_OK
    err = skycoin.cipher.SHA256Xor(i, h, temp2) 
    assert err == skycoin.SKY_OK
    assert temp != h
    assert temp != i
    assert temp != skycoin.cipher.SHA256()
    assert temp == temp2


def test_TestSHA256Null():
    x = skycoin.cipher.SHA256()
    _, isNull = skycoin.cipher.SHA256Null(x)
    assert isNull
    _, b = skycoin.cipher.RandByte(128)
    skycoin.cipher.SumSHA256(b, x)
    _, isNull = skycoin.cipher.SHA256Null(x)
    assert not isNull

def test_TestMerkle():
    hashlist = []
    h = skycoin.cipher.SHA256()
    for _ in range(5):
        hashlist.append(h)
    
    for i in range(5):
        err, data = skycoin.cipher.RandByte(128)
        assert err == skycoin.SKY_OK
        err = skycoin.cipher.SumSHA256(data, hashlist[i])
        assert err == skycoin.SKY_OK
