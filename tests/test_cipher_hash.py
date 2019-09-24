import skycoin
import tests.utils
import base64


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
    assert skycoin.SKY_cipher_HashRipemd160(b, r160) == skycoin.SKY_OK
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
    assert skycoin.SKY_cipher_Ripemd160_Set(
        h, b) == skycoin.SKY_ErrInvalidLengthRipemd160
    _, b = skycoin.SKY_cipher_RandByte(100)
    assert skycoin.SKY_cipher_Ripemd160_Set(
        h, b) == skycoin.SKY_ErrInvalidLengthRipemd160
    _, b = skycoin.SKY_cipher_RandByte(19)
    assert skycoin.SKY_cipher_Ripemd160_Set(
        h, b) == skycoin.SKY_ErrInvalidLengthRipemd160
    _, b = skycoin.SKY_cipher_RandByte(0)
    assert skycoin.SKY_cipher_Ripemd160_Set(
        h, b) == skycoin.SKY_ErrInvalidLengthRipemd160
    _, b = skycoin.SKY_cipher_RandByte(20)
    assert skycoin.SKY_cipher_Ripemd160_Set(h, b) == skycoin.SKY_OK
    _, b1 = skycoin.SKY_cipher_RandByte(20)
    skycoin.SKY_cipher_Ripemd160_Set(h, b1)
    assert h.compareToString(str(b))


def test_TestSHA256Set():
    h = skycoin.cipher_SHA256()
    _, b = skycoin.SKY_cipher_RandByte(33)
    assert skycoin.SKY_cipher_SHA256_Set(
        h, b) == skycoin.SKY_ErrInvalidLengthSHA256
    _, b = skycoin.SKY_cipher_RandByte(100)
    assert skycoin.SKY_cipher_SHA256_Set(
        h, b) == skycoin.SKY_ErrInvalidLengthSHA256
    _, b = skycoin.SKY_cipher_RandByte(31)
    assert skycoin.SKY_cipher_SHA256_Set(
        h, b) == skycoin.SKY_ErrInvalidLengthSHA256
    _, b = skycoin.SKY_cipher_RandByte(0)
    assert skycoin.SKY_cipher_SHA256_Set(
        h, b) == skycoin.SKY_ErrInvalidLengthSHA256
    _, b = skycoin.SKY_cipher_RandByte(32)
    assert skycoin.SKY_cipher_SHA256_Set(h, b) == skycoin.SKY_OK
    _, b = skycoin.SKY_cipher_RandByte(32)
    skycoin.SKY_cipher_SHA256_Set(h, b)
    assert h.toStr()[:] == b


def test_TestSHA256Hex():
    h = skycoin.cipher_SHA256()
    _, b = skycoin.SKY_cipher_RandByte(32)
    skycoin.SKY_cipher_SHA256_Set(h, b)
    _, s = skycoin.SKY_cipher_SHA256_Hex(h)
    h2 = skycoin.cipher_SHA256()
    err = skycoin.SKY_cipher_SHA256FromHex(s, h2)
    assert err == skycoin.SKY_OK
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
        assert err == skycoin.SKY_OK
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


def test_TestSHA256FromHex():
    # Invalid hex hash
    h = skycoin.cipher_SHA256()
    err = skycoin.SKY_cipher_SHA256FromHex(b"cawcad", h)
    assert err == skycoin.SKY_ERROR

    # Truncated hex hash
    _, b = skycoin.SKY_cipher_RandByte(128)
    h = skycoin.cipher_SHA256()
    skycoin.SKY_cipher_SumSHA256(b, h)
    h_bytes = h.toStr()
    h1 = skycoin.cipher_SHA256()
    err = skycoin.SKY_cipher_SHA256FromHex(h_bytes[:int(len(h_bytes) / 2)], h1)
    assert err == skycoin.SKY_ERROR

    # Valid hex hash
    h2 = skycoin.cipher_SHA256()
    err, b = skycoin.SKY_cipher_SHA256_Hex(h)
    err = skycoin.SKY_cipher_SHA256FromHex(b, h2)
    assert h == h2
    assert err == skycoin.SKY_OK


def test_TestDoubleSHA256():
    _, b = skycoin.SKY_cipher_RandByte(128)
    h = skycoin.cipher_SHA256()
    skycoin.SKY_cipher_DoubleSHA256(b, h)
    assert h != skycoin.cipher_SHA256()
    assert h != freshSumSHA256(b)


def test_TestAddSHA256():
    _, b = skycoin.SKY_cipher_RandByte(128)
    h = skycoin.cipher_SHA256()
    skycoin.SKY_cipher_SumSHA256(b, h)
    _, c = skycoin.SKY_cipher_RandByte(64)
    i = skycoin.cipher_SHA256()
    skycoin.SKY_cipher_SumSHA256(c, i)
    add = skycoin.cipher_SHA256()
    err = skycoin.SKY_cipher_AddSHA256(h, i, add)
    assert err == skycoin.SKY_OK
    assert add != skycoin.cipher_SHA256()
    assert add != h
    assert add != i


def test_TestXorSHA256():
    _, b = skycoin.SKY_cipher_RandByte(128)
    _, c = skycoin.SKY_cipher_RandByte(128)
    h = skycoin.cipher_SHA256()
    i = skycoin.cipher_SHA256()
    err = skycoin.SKY_cipher_SumSHA256(b, h)
    assert err == skycoin.SKY_OK
    err = skycoin.SKY_cipher_SumSHA256(c, i)
    assert err == skycoin.SKY_OK
    temp = skycoin.cipher_SHA256()
    temp2 = skycoin.cipher_SHA256()
    assert skycoin.SKY_cipher_SHA256_Xor(h, i, temp) == skycoin.SKY_OK
    assert skycoin.SKY_cipher_SHA256_Xor(i, h, temp2) == skycoin.SKY_OK
    assert temp != h
    assert temp != i
    assert temp != skycoin.cipher_SHA256()
    assert temp == temp2


def test_TestSHA256Null():
    x = skycoin.cipher_SHA256()
    _, isNull = skycoin.SKY_cipher_SHA256_Null(x)
    assert isNull
    _, b = skycoin.SKY_cipher_RandByte(128)
    skycoin.SKY_cipher_SumSHA256(b, x)
    _, isNull = skycoin.SKY_cipher_SHA256_Null(x)
    assert not isNull

# def test_TestMerkle():
#     hashlist = []
#     h = skycoin.cipher_SHA256()
#     for _ in range(5):
#         hashlist.append(h)

#     for i in range(5):
#         err, data = skycoin.SKY_cipher_RandByte(128)
#         assert err == skycoin.SKY_OK
#         err = skycoin.SKY_cipher_SumSHA256(data, hashlist[i])
#         assert err == skycoin.SKY_OK

#     # assert skycoin.SKY_cipher_Merkle(hashlist,h) == 45


# # err, data = skycoin.SKY_cipher_RandByte(128)
# # assert err == skycoin.SKY_OK
# # h = skycoin.cipher_SHA256()
# # err = skycoin.SKY_cipher_SumSHA256(data, h)
# # assert err == skycoin.SKY_OK
# # Single hash input returns hash
# # a = [x for x in h]
# # assert skycoin.SKY_cipher_Merkle(a,h) == 45
# #  DoubleSHA256 double SHA256
# # func DoubleSHA256(b []byte) SHA256 {
# # 	h1 := SumSHA256(b)
# # 	h2 := SumSHA256(h1[:])
# # 	return h2
# # }

# # // AddSHA256 returns the SHA256 hash of to two concatenated hashes
# # func AddSHA256(a SHA256, b SHA256) SHA256 {
# # 	c := append(a[:], b[:]...)
# # 	return SumSHA256(c)
# # }

# # // Returns the next highest power of 2 above n, if n is not already a
# # // power of 2
# # func nextPowerOfTwo(n uint64) uint64 {
# # 	var k uint64 = 1
# # 	for k < n {
# # 		k *= 2
# # 	}
# # 	return k
# # }

# # // Merkle computes the merkle root of a hash array
# # // Array of hashes is padded with 0 hashes until next power of 2
# # func Merkle(h0 []SHA256) SHA256 {
# # 	lh := uint64(len(h0))
# # 	np := nextPowerOfTwo(lh)
# # 	h1 := append(h0, make([]SHA256, np-lh)...)
# # 	for len(h1) != 1 {
# # 		h2 := make([]SHA256, len(h1)/2)
# # 		for i := 0; i < len(h2); i++ {
# # 			h2[i] = AddSHA256(h1[2*i], h1[2*i+1])
# # 		}
# # 		h1 = h2
# # 	}
# # 	return h1[0]
# # }

# # def merkle(h0):
# #     lh = base64.standard_b64decode(len(h0))
# #     np =

# # def nextPowerOfTwo():
