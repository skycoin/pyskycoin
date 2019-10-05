import skycoin
import tests.utils as utils


def test_TestNewPubKey():
    public_key = skycoin.cipher_PubKey()
    _, data = skycoin.SKY_cipher_RandByte(31)
    assert skycoin.SKY_cipher_NewPubKey(
        data, public_key) == skycoin.SKY_ErrInvalidLengthPubKey
    _, data = skycoin.SKY_cipher_RandByte(32)
    assert skycoin.SKY_cipher_NewPubKey(
        data, public_key) == skycoin.SKY_ErrInvalidLengthPubKey
    _, data = skycoin.SKY_cipher_RandByte(34)
    assert skycoin.SKY_cipher_NewPubKey(
        data, public_key) == skycoin.SKY_ErrInvalidLengthPubKey
    _, data = skycoin.SKY_cipher_RandByte(0)
    assert skycoin.SKY_cipher_NewPubKey(
        data, public_key) == skycoin.SKY_ErrInvalidLengthPubKey
    _, data = skycoin.SKY_cipher_RandByte(100)
    assert skycoin.SKY_cipher_NewPubKey(
        data, public_key) == skycoin.SKY_ErrInvalidLengthPubKey
    _, data = skycoin.SKY_cipher_RandByte(33)
    assert skycoin.SKY_cipher_NewPubKey(
        data, public_key) == skycoin.SKY_ErrInvalidPubKey
    pubkey = skycoin.cipher_PubKey()
    seckey = skycoin.cipher_SecKey()
    err = skycoin.SKY_cipher_GenerateKeyPair(pubkey, seckey)
    assert err == skycoin.SKY_OK
    ptemp = pubkey.toStr()
    pubkey2 = skycoin.cipher_PubKey()
    err = skycoin.SKY_cipher_NewPubKey(ptemp, pubkey2)
    assert err == skycoin.SKY_OK
    assert pubkey == pubkey2


def test_TestPubKeyVerify():
    # Random bytes should not be valid, most of the time
    failed = False
    for _ in range(10):
        public_key = skycoin.cipher_PubKey()
        _, data = skycoin.SKY_cipher_RandByte(33)
        skycoin.SKY_cipher_NewPubKey(data, public_key)
        if skycoin.SKY_cipher_PubKey_Verify(public_key) != None:
            failed = True
            break
    assert failed is True


def test_TestPubKeyVerifyNil():
    # Empty public key should not be valid
    public_key = skycoin.cipher_PubKey()
    assert skycoin.SKY_cipher_PubKey_Verify(
        public_key) == skycoin.SKY_ErrInvalidPubKey


def test_TestPubKeyVerifyDefault1():
    #  Generated pub key should be valid
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    assert skycoin.SKY_cipher_PubKey_Verify(public_key) == skycoin.SKY_OK


def test_TestPubKeyVerifyDefault2():
    for _ in range(1024):
        public_key = skycoin.cipher_PubKey()
        secret_key = skycoin.cipher_SecKey()
        skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
        assert skycoin.SKY_cipher_PubKey_Verify(public_key) == skycoin.SKY_OK


def test_TestPubKeyToAddress():
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    addres = skycoin.cipher__Address()
    skycoin.SKY_cipher_AddressFromPubKey(public_key, addres)
    # func (self Address) Verify(key PubKey) error
    assert skycoin.SKY_cipher_Address_Verify(
        addres, public_key) == skycoin.SKY_OK
    # func DecodeBase58Address(addr string) (Address, error)
    _, addres_str = skycoin.SKY_cipher_Address_String(addres)
    assert skycoin.SKY_cipher_DecodeBase58Address(
        addres_str, addres) == skycoin.SKY_OK


def test_TestPubKeyToAddress2():
    for _ in range(1024):
        public_key = skycoin.cipher_PubKey()
        secret_key = skycoin.cipher_SecKey()
        skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
        addres = skycoin.cipher__Address()
        skycoin.SKY_cipher_AddressFromPubKey(public_key, addres)
        # func (self Address) Verify(key PubKey) error
        assert skycoin.SKY_cipher_Address_Verify(
            addres, public_key) == skycoin.SKY_OK
        # func DecodeBase58Address(addr string) (Address, error)
        _, addres_str = skycoin.SKY_cipher_Address_String(addres)
        assert skycoin.SKY_cipher_DecodeBase58Address(
            addres_str, addres) == skycoin.SKY_OK


def test_TestMustNewSecKey():
    secret_key = skycoin.cipher_SecKey()
    _, data = skycoin.SKY_cipher_RandByte(31)
    assert skycoin.SKY_cipher_NewSecKey(
        data, secret_key) == skycoin.SKY_ErrInvalidLengthSecKey
    _, data = skycoin.SKY_cipher_RandByte(33)
    assert skycoin.SKY_cipher_NewSecKey(
        data, secret_key) == skycoin.SKY_ErrInvalidLengthSecKey
    _, data = skycoin.SKY_cipher_RandByte(34)
    assert skycoin.SKY_cipher_NewSecKey(
        data, secret_key) == skycoin.SKY_ErrInvalidLengthSecKey
    _, data = skycoin.SKY_cipher_RandByte(0)
    assert skycoin.SKY_cipher_NewSecKey(
        data, secret_key) == skycoin.SKY_ErrInvalidLengthSecKey
    _, data = skycoin.SKY_cipher_RandByte(100)
    assert skycoin.SKY_cipher_NewSecKey(
        data, secret_key) == skycoin.SKY_ErrInvalidLengthSecKey
    _, data = skycoin.SKY_cipher_RandByte(32)
    assert skycoin.SKY_cipher_NewSecKey(data, secret_key) == skycoin.SKY_OK
    assert secret_key.toStr() == data


def test_TestSecKeyVerify():
    # Empty secret key should not be valid
    secret_key = skycoin.cipher_SecKey()
    public_key = skycoin.cipher_PubKey()
    assert skycoin.SKY_cipher_SecKey_Verify(secret_key) != None
    # Generated sec key should be valid
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    assert skycoin.SKY_cipher_PubKey_Verify(public_key) == skycoin.SKY_OK


def test_TestECDHonce():
    secret_key_1 = skycoin.cipher_SecKey()
    public_key_1 = skycoin.cipher_PubKey()
    secret_key_2 = skycoin.cipher_SecKey()
    public_key_2 = skycoin.cipher_PubKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key_1, secret_key_1)
    skycoin.SKY_cipher_GenerateKeyPair(public_key_2, secret_key_2)
    _, data_1 = skycoin.SKY_cipher_ECDH(public_key_2, secret_key_1)
    _, data_2 = skycoin.SKY_cipher_ECDH(public_key_1, secret_key_2)
    assert data_1 == data_2


def test_TestECDHloop():
    for _ in range(128):
        secret_key_1 = skycoin.cipher_SecKey()
        public_key_1 = skycoin.cipher_PubKey()
        secret_key_2 = skycoin.cipher_SecKey()
        public_key_2 = skycoin.cipher_PubKey()
        skycoin.SKY_cipher_GenerateKeyPair(public_key_1, secret_key_1)
        skycoin.SKY_cipher_GenerateKeyPair(public_key_2, secret_key_2)
        _, data_1 = skycoin.SKY_cipher_ECDH(public_key_2, secret_key_1)
        _, data_2 = skycoin.SKY_cipher_ECDH(public_key_1, secret_key_2)
        assert data_1 == data_2


def test_TestNewSig():
    sig = skycoin.cipher_Sig()
    _, data = skycoin.SKY_cipher_RandByte(64)
    assert skycoin.SKY_cipher_NewSig(
        data, sig) == skycoin.SKY_ErrInvalidLengthSig
    _, data = skycoin.SKY_cipher_RandByte(66)
    assert skycoin.SKY_cipher_NewSig(
        data, sig) == skycoin.SKY_ErrInvalidLengthSig
    _, data = skycoin.SKY_cipher_RandByte(67)
    assert skycoin.SKY_cipher_NewSig(
        data, sig) == skycoin.SKY_ErrInvalidLengthSig
    _, data = skycoin.SKY_cipher_RandByte(0)
    assert skycoin.SKY_cipher_NewSig(
        data, sig) == skycoin.SKY_ErrInvalidLengthSig
    _, data = skycoin.SKY_cipher_RandByte(100)
    assert skycoin.SKY_cipher_NewSig(
        data, sig) == skycoin.SKY_ErrInvalidLengthSig
    _, data = skycoin.SKY_cipher_RandByte(65)
    assert skycoin.SKY_cipher_NewSig(data, sig) == skycoin.SKY_OK
    assert sig.toStr() == data


def test_TestSignHash():
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    addres = skycoin.cipher__Address()
    sha_sum = skycoin.cipher_SHA256()
    sig_1 = skycoin.cipher_Sig()
    sig_2 = skycoin.cipher_Sig()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    skycoin.SKY_cipher_AddressFromPubKey(public_key, addres)
    _, data = skycoin.SKY_cipher_RandByte(256)
    skycoin.SKY_cipher_SumSHA256(data, sha_sum)
    skycoin.SKY_cipher_SignHash(sha_sum, secret_key, sig_1)
    assert sig_1 != sig_2


def test_TestPubKeyFromSecKey():
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    public_key_2 = skycoin.cipher_PubKey()
    skycoin.SKY_cipher_PubKeyFromSecKey(secret_key, public_key_2)
    assert public_key == public_key_2
    secret_key_2 = skycoin.cipher_SecKey()
    assert skycoin.SKY_cipher_PubKeyFromSecKey(
        secret_key_2, public_key) == skycoin.SKY_ErrPubKeyFromNullSecKey
    _, data = skycoin.SKY_cipher_RandByte(99)
    assert skycoin.SKY_cipher_NewSecKey(
        data, secret_key) == skycoin.SKY_ErrInvalidLengthSecKey
    _, data = skycoin.SKY_cipher_RandByte(31)
    assert skycoin.SKY_cipher_NewSecKey(
        data, secret_key) == skycoin.SKY_ErrInvalidLengthSecKey


def test_TestPubKeyFromSig():
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    sha_sum = skycoin.cipher_SHA256()
    _, data = skycoin.SKY_cipher_RandByte(256)
    skycoin.SKY_cipher_SumSHA256(data, sha_sum)
    sig_1 = skycoin.cipher_Sig()
    skycoin.SKY_cipher_SignHash(sha_sum, secret_key, sig_1)
    public_key_2 = skycoin.cipher_PubKey()
    assert skycoin.SKY_cipher_PubKeyFromSig(
        sig_1, sha_sum, public_key_2) == skycoin.SKY_OK
    assert public_key == public_key_2
    sig_2 = skycoin.cipher_Sig()
    assert skycoin.SKY_cipher_PubKeyFromSig(
        sig_2, sha_sum, public_key_2) == skycoin.SKY_ErrInvalidSigPubKeyRecovery


def test_TestGenerateKeyPair():
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    assert skycoin.SKY_cipher_PubKey_Verify(public_key) == skycoin.SKY_OK
    assert skycoin.SKY_cipher_SecKey_Verify(secret_key) == skycoin.SKY_OK


def test_TestGenerateDeterministicKeyPair():
    # deterministic key pairs are useless as is because we can't
    # generate pair n+1, only pair 0
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    _, seed = skycoin.SKY_cipher_RandByte(32)
    skycoin.SKY_cipher_GenerateDeterministicKeyPair(
        seed, public_key, secret_key)
    assert skycoin.SKY_cipher_PubKey_Verify(public_key) == skycoin.SKY_OK
    assert skycoin.SKY_cipher_SecKey_Verify(secret_key) == skycoin.SKY_OK
    skycoin.SKY_cipher_GenerateDeterministicKeyPair(
        seed, public_key, secret_key)
    assert skycoin.SKY_cipher_PubKey_Verify(public_key) == skycoin.SKY_OK
    assert skycoin.SKY_cipher_SecKey_Verify(secret_key) == skycoin.SKY_OK


def test_TestSecKeyTest():
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    secret_key_2 = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    value = skycoin.skycoin.SKY_cipher_CheckSecKey(secret_key)
    assert value == skycoin.SKY_OK
    value = skycoin.skycoin.SKY_cipher_CheckSecKey(secret_key_2)
    assert value == skycoin.SKY_ErrInvalidSecKyVerification


def test_TestSecKeyHashTest():
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    secret_key_2 = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    sha_sum_1 = skycoin.cipher_SHA256()
    _, data = skycoin.SKY_cipher_RandByte(256)
    skycoin.SKY_cipher_SumSHA256(data, sha_sum_1)
    value = skycoin.skycoin.SKY_cipher_CheckSecKeyHash(secret_key, sha_sum_1)
    assert value == skycoin.SKY_OK
    value = skycoin.skycoin.SKY_cipher_CheckSecKeyHash(secret_key_2, sha_sum_1)
    assert value == skycoin.SKY_ErrInvalidSecKyVerification


def test_TestGenerateDeterministicKeyPairsUsesAllBytes():
    # Tests that if a seed >128 bits is used, the generator does not ignore bits > 128
    seed = b"property diet little foster provide disagree witness mountain alley weekend kitten general"
    secret_keys = skycoin.SKY_cipher_GenerateDeterministicKeyPairsSeed(seed, 3)[
        1:]
    secret_keys_2 = skycoin.SKY_cipher_GenerateDeterministicKeyPairsSeed(seed[:16], 3)[
        1:]
    assert secret_keys != secret_keys_2


def test_TestPubKeyFromHex():
    p1 = skycoin.cipher_PubKey()
    # Invalid hex
    err = skycoin.SKY_cipher_PubKeyFromHex(b"", p1)
    assert err == skycoin.SKY_ErrInvalidLengthPubKey
    err = skycoin.SKY_cipher_PubKeyFromHex(b"cascs", p1)
    assert err == skycoin.SKY_ErrInvalidPubKey


def test_TestPubKeyHex():
    p, sk = utils.makecipher_PubKeyAndcipher_SecKey()
    err, s3 = skycoin.SKY_cipher_PubKey_Hex(p)
    assert err == skycoin.SKY_OK
    p2 = skycoin.cipher_PubKey()
    err = skycoin.SKY_cipher_PubKeyFromHex(s3, p2)
    assert err == skycoin.SKY_OK
    assert p == p2
    err, s4 = skycoin.SKY_cipher_PubKey_Hex(p2)
    assert err == skycoin.SKY_OK
    assert s3 == s4


def test_TestSecKeyFromHex():
    sk = skycoin.cipher_SecKey()
    # Invalid hex
    err = skycoin.SKY_cipher_SecKeyFromHex(b"", sk)
    assert err == skycoin.SKY_ErrInvalidLengthSecKey
    err = skycoin.SKY_cipher_SecKeyFromHex(b"cascs", sk)
    assert err == skycoin.SKY_ErrInvalidSecKey
    # INvalid hex length
    err, b = skycoin.SKY_cipher_RandByte(32)
    p = skycoin.cipher_SecKey()
    err = skycoin.SKY_cipher_NewSecKey(b, p)
    assert err == skycoin.SKY_OK
