import skycoin
import base64

tt = [
    [
        b"data length=1 password is empty=true",
    	skycoin.SKY_cipher_RandByte(1)[1],
    	b"",
    	skycoin.SKY_ErrSHA256orMissingPassword,
    ],
    [
        b"data length=1  password is empty=false",
    	skycoin.SKY_cipher_RandByte(1)[1],
    	b"key",
    	skycoin.SKY_OK,
    ],
    [
        b"data length<32 password is empty=false",
    	skycoin.SKY_cipher_RandByte(2)[1],
    	b"pwd",
    	skycoin.SKY_OK,
    ],
    [
        b"data length=32 password is empty=false",
    	skycoin.SKY_cipher_RandByte(32)[1],
    	b"pwd",
    	skycoin.SKY_OK,
    ],
    [
        b"data length=2*32 password is empty=false",
    	skycoin.SKY_cipher_RandByte(64)[1],
    	b"9JMkCPphe73NQvGhmab",
    	skycoin.SKY_OK,
    ],
    [
        b"data length>2*32 password is empty=false",
    	skycoin.SKY_cipher_RandByte(65)[1],
    	b"9JMkCPphe73NQvGhmab",
    	skycoin.SKY_OK,
    ],
]

sha256XorDataLengthSize = 4
sha256XorBlockSize = 32
sha256XorNonceSize = 32
sha256XorChecksumSize = 32

def test_TestEncrypt():
    for t in tt:
        err, encrypted = skycoin.SKY_encrypt_Sha256Xor_Encrypt(t[1], t[2])
        assert err == t[3]
        if t[3] == skycoin.SKY_ErrSHA256orMissingPassword:
            continue

        n = (sha256XorDataLengthSize + len(t[1])) // sha256XorBlockSize
        m = (sha256XorDataLengthSize + len(t[1])) % sha256XorBlockSize
        if m > 0:
            n += 1
        
        rdata = base64.standard_b64decode(str(encrypted))
        assert len(rdata) >= 0
        totalEncryptedDataLen = sha256XorBlockSize + sha256XorNonceSize + 32 + n * sha256XorBlockSize
        assert len(rdata) == totalEncryptedDataLen
        checksum = rdata[:sha256XorChecksumSize]
        sha_sum = skycoin.cipher_SHA256()
        skycoin.SKY_cipher_SumSHA256(rdata[sha256XorChecksumSize:], sha_sum)
        assert sha_sum.toStr() == checksum

    pwd = b"pwd"       
    for i in range(33, 64):
        err, data = skycoin.SKY_cipher_RandByte(i)
        assert err == skycoin.SKY_OK
        err, encrypted = skycoin.SKY_encrypt_Sha256Xor_Encrypt(data, pwd)
        assert err == skycoin.SKY_OK

        n = (sha256XorDataLengthSize + len(data)) // sha256XorBlockSize
        m = (sha256XorDataLengthSize + len(data)) % sha256XorBlockSize
        if m > 0:
            n += 1

        rdata = base64.standard_b64decode(str(encrypted))
        assert len(rdata) >= 0
        totalEncryptedDataLen = sha256XorBlockSize + sha256XorNonceSize + 32 + n * sha256XorBlockSize
        assert len(rdata) == totalEncryptedDataLen
        checksum = rdata[:sha256XorChecksumSize]
        sha_sum = skycoin.cipher_SHA256()
        skycoin.SKY_cipher_SumSHA256(rdata[sha256XorChecksumSize:], sha_sum)
        assert sha_sum.toStr() == checksum

