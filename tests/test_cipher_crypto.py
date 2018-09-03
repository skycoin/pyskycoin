import skycoin

def test_TestNewPubKey():
    public_key = skycoin.cipher.PubKey()
    _, data = skycoin.cipher.RandByte(31)
    err = skycoin.cipher.NewPubKey(data, public_key) 
    assert err == skycoin.SKY_ErrInvalidLengthPubKey
    _, data = skycoin.cipher.RandByte(32)
    err = skycoin.cipher.NewPubKey(data, public_key)
    assert err == skycoin.SKY_ErrInvalidLengthPubKey
    _, data = skycoin.cipher.RandByte(34)
    err = skycoin.cipher.NewPubKey(data, public_key)
    assert err == skycoin.SKY_ErrInvalidLengthPubKey
    _, data = skycoin.cipher.RandByte(0)
    err = skycoin.cipher.NewPubKey(data, public_key)
    assert err == skycoin.SKY_ErrInvalidLengthPubKey
    _, data = skycoin.cipher.RandByte(100)
    assert skycoin.cipher.NewPubKey(data, public_key) == skycoin.SKY_ErrInvalidLengthPubKey
    _, data = skycoin.cipher.RandByte(33)
    assert skycoin.cipher.NewPubKey(data, public_key) == skycoin.SKY_OK
    assert public_key.toStr() == data


def test_TestPubKeyVerify():
    # Random bytes should not be valid, most of the time
    failed = False
    for _ in range(10):
        public_key = skycoin.cipher.PubKey()
        _,  data = skycoin.cipher.RandByte(33)
        skycoin.cipher.NewPubKey(data, public_key)
        if skycoin.cipher.PubKeyVerify(public_key) != None:
            failed = True
            break
    assert failed is True 

def test_TestPubKeyVerifyNil():
    # Empty public key should not be valid
    public_key = skycoin.cipher.PubKey()
    err = skycoin.cipher.PubKeyVerify(public_key)
    assert err == skycoin.SKY_ErrInvalidPubKey

def test_TestPubKeyVerifyDefault1():
    #  Generated pub key should be valid   
    public_key = skycoin.cipher.PubKey()
    secret_key = skycoin.cipher.SecKey()
    skycoin.cipher.GenerateKeyPair(public_key, secret_key)
    assert skycoin.cipher.PubKeyVerify(public_key) == skycoin.SKY_OK
    
def test_TestPubKeyVerifyDefault2():
    for _ in range(1024):
        public_key = skycoin.cipher.PubKey()
        secret_key = skycoin.cipher.SecKey()
        skycoin.cipher.GenerateKeyPair(public_key, secret_key)
        assert skycoin.cipher.PubKeyVerify(public_key) == skycoin.SKY_OK
    
def test_TestPubKeyToAddress():
    public_key = skycoin.cipher.PubKey()
    secret_key = skycoin.cipher.SecKey()
    skycoin.cipher.GenerateKeyPair(public_key, secret_key)
    addres = skycoin.cipher.Address()
    skycoin.cipher.AddressFromPubKey(public_key, addres) 
    err = skycoin.cipher.AddressVerify(addres, public_key)
    assert err == skycoin.SKY_OK
    _, addres_str = skycoin.cipher.AddressString(addres)
    err = skycoin.cipher.DecodeBase58Address(addres_str, addres)
    assert err == skycoin.SKY_OK

def test_TestPubKeyToAddress2():
    for _ in range(1024):
        public_key = skycoin.cipher.PubKey()
        secret_key = skycoin.cipher.SecKey()
        skycoin.cipher.GenerateKeyPair(public_key, secret_key)
        addres = skycoin.cipher.Address()
        skycoin.cipher.AddressFromPubKey(public_key, addres) 
        assert skycoin.cipher.AddressVerify(addres, public_key) == skycoin.SKY_OK
        _, addres_str = skycoin.cipher.AddressString(addres)
        assert skycoin.cipher.DecodeBase58Address(addres_str, addres) == skycoin.SKY_OK
    
def test_TestMustNewSecKey():
    secret_key = skycoin.cipher.SecKey()
    _, data = skycoin.cipher.RandByte(31)
    assert skycoin.cipher.NewSecKey(data, secret_key) == skycoin.SKY_ErrInvalidLengthSecKey
    _, data = skycoin.cipher.RandByte(33)
    assert skycoin.cipher.NewSecKey(data, secret_key) == skycoin.SKY_ErrInvalidLengthSecKey
    _, data = skycoin.cipher.RandByte(34)
    assert skycoin.cipher.NewSecKey(data, secret_key) == skycoin.SKY_ErrInvalidLengthSecKey
    _, data = skycoin.cipher.RandByte(0)
    assert skycoin.cipher.NewSecKey(data, secret_key) == skycoin.SKY_ErrInvalidLengthSecKey
    _, data = skycoin.cipher.RandByte(100)
    assert skycoin.cipher.NewSecKey(data, secret_key) == skycoin.SKY_ErrInvalidLengthSecKey
    _, data = skycoin.cipher.RandByte(32)
    assert skycoin.cipher.NewSecKey(data, secret_key) == skycoin.SKY_OK
    assert secret_key.toStr() == data



def test_TestSecKeyVerify():
    # Empty secret key should not be valid
    secret_key = skycoin.cipher.SecKey()
    public_key = skycoin.cipher.PubKey()
    err = skycoin.cipher.SecKeyVerify(secret_key) 
    assert err != None
    # Generated sec key should be valid
    skycoin.cipher.GenerateKeyPair(public_key, secret_key)
    err = skycoin.cipher.PubKeyVerify(public_key)
    assert err == skycoin.SKY_OK

def test_TestECDHonce():
    secret_key_1 = skycoin.cipher.SecKey()
    public_key_1 = skycoin.cipher.PubKey()
    secret_key_2 = skycoin.cipher.SecKey()
    public_key_2 = skycoin.cipher.PubKey()
    skycoin.cipher.GenerateKeyPair(public_key_1, secret_key_1)
    skycoin.cipher.GenerateKeyPair(public_key_2, secret_key_2)
    _, data_1 = skycoin.cipher.ECDH(public_key_2, secret_key_1)
    _, data_2 = skycoin.cipher.ECDH(public_key_1, secret_key_2)
    assert data_1 == data_2

def test_TestECDHloop():
    for _ in range(128):
        secret_key_1 = skycoin.cipher.SecKey()
        public_key_1 = skycoin.cipher.PubKey()
        secret_key_2 = skycoin.cipher.SecKey()
        public_key_2 = skycoin.cipher.PubKey()
        skycoin.cipher.GenerateKeyPair(public_key_1, secret_key_1)
        skycoin.cipher.GenerateKeyPair(public_key_2, secret_key_2)
        _, data_1 = skycoin.cipher.ECDH(public_key_2, secret_key_1)
        _, data_2 = skycoin.cipher.ECDH(public_key_1, secret_key_2)
        assert data_1 == data_2

def test_TestNewSig():
    sig = skycoin.cipher.Sig()
    _, data = skycoin.cipher.RandByte(64)
    err = skycoin.cipher.NewSig(data, sig)
    assert err == skycoin.SKY_ErrInvalidLengthSig
    _, data = skycoin.cipher.RandByte(66)
    assert skycoin.cipher.NewSig(data, sig) == skycoin.SKY_ErrInvalidLengthSig
    _, data = skycoin.cipher.RandByte(67)
    assert skycoin.cipher.NewSig(data, sig) == skycoin.SKY_ErrInvalidLengthSig
    _, data = skycoin.cipher.RandByte(0)
    assert skycoin.cipher.NewSig(data, sig) == skycoin.SKY_ErrInvalidLengthSig
    _, data = skycoin.cipher.RandByte(100)
    assert skycoin.cipher.NewSig(data, sig) == skycoin.SKY_ErrInvalidLengthSig
    _, data = skycoin.cipher.RandByte(65)
    assert skycoin.cipher.NewSig(data, sig) == skycoin.SKY_OK
    assert sig.toStr() == data



def test_TestChkSig():
    secret_key_1 = skycoin.cipher.SecKey()
    secret_key_2 = skycoin.cipher.SecKey()
    public_key_1 = skycoin.cipher.PubKey()
    public_key_2 = skycoin.cipher.PubKey()
    addres = skycoin.cipher.Address()
    addres_2 = skycoin.cipher.Address()
    sig_1 = skycoin.cipher.Sig()
    sig_2 = skycoin.cipher.Sig()
    sha_sum = skycoin.cipher.SHA256()
    sha_sum_2 = skycoin.cipher.SHA256()
    skycoin.cipher.GenerateKeyPair(public_key_1, secret_key_1)
    skycoin.cipher.PubKeyVerify(public_key_1)
    skycoin.cipher.SecKeyVerify(secret_key_1)
    skycoin.cipher.AddressFromPubKey(public_key_1, addres)
    _, data = skycoin.cipher.RandByte(256)
    skycoin.cipher.SumSHA256(data, sha_sum)
    skycoin.cipher.SignHash(sha_sum, secret_key_1, sig_1)
    err = skycoin.cipher.ChkSig(addres, sha_sum, sig_1) 
    assert err == skycoin.SKY_OK
    # Empty sig should be invalid
    err = skycoin.cipher.ChkSig(addres, sha_sum, sig_2)
    assert err == skycoin.SKY_ErrInvalidSigForPubKey
    # Random sigs should not pass
    for _ in range(100):
        _, data = skycoin.cipher.RandByte(65)
        skycoin.cipher.NewSig(data, sig_1)
        assert skycoin.cipher.ChkSig(addres, sha_sum, sig_1) != skycoin.SKY_OK
    # Sig for one hash does not work for another hash
    _, data = skycoin.cipher.RandByte(256)
    skycoin.cipher.SumSHA256(data, sha_sum_2)
    skycoin.cipher.SignHash(sha_sum_2, secret_key_1, sig_2)
    err = skycoin.cipher.ChkSig(addres, sha_sum_2, sig_2) 
    assert err == skycoin.SKY_OK
    err = skycoin.cipher.ChkSig(addres, sha_sum, sig_2) 
    assert err != skycoin.SKY_OK
    err = skycoin.cipher.ChkSig(addres, sha_sum_2, sig_1)
    assert err != skycoin.SKY_OK
    # Different secret keys should not create same sig
    skycoin.cipher.GenerateKeyPair(public_key_2, secret_key_2)
    skycoin.cipher.AddressFromPubKey(public_key_2, addres_2)
    sha_sum = skycoin.cipher.SHA256()
    skycoin.cipher.SignHash(sha_sum, secret_key_1, sig_1)
    skycoin.cipher.SignHash(sha_sum, secret_key_2, sig_2)
    err = skycoin.cipher.ChkSig(addres, sha_sum, sig_1)
    assert err == skycoin.SKY_OK
    err = skycoin.cipher.ChkSig(addres_2, sha_sum, sig_2) 
    assert err == skycoin.SKY_OK
    assert sig_1 != sig_2
    _, data = skycoin.cipher.RandByte(256)
    skycoin.cipher.SumSHA256(data, sha_sum)
    skycoin.cipher.SignHash(sha_sum, secret_key_1, sig_1)
    skycoin.cipher.SignHash(sha_sum, secret_key_2, sig_2)
    assert skycoin.cipher.ChkSig(addres, sha_sum, sig_1) == skycoin.SKY_OK
    assert skycoin.cipher.ChkSig(addres_2, sha_sum, sig_2) == skycoin.SKY_OK
    assert sig_1 != sig_2
    # Bad address should be invalid
    err = skycoin.cipher.ChkSig(addres, sha_sum, sig_2)
    assert err != skycoin.SKY_OK
    err = skycoin.cipher.ChkSig(addres_2, sha_sum, sig_1)
    assert err != skycoin.SKY_OK

def test_TestSignHash():
    public_key = skycoin.cipher.PubKey()
    secret_key = skycoin.cipher.SecKey()
    addres = skycoin.cipher.Address()
    sha_sum = skycoin.cipher.SHA256()
    sig_1 = skycoin.cipher.Sig()
    sig_2 = skycoin.cipher.Sig()
    skycoin.cipher.GenerateKeyPair(public_key, secret_key)
    skycoin.cipher.AddressFromPubKey(public_key, addres)
    _, data = skycoin.cipher.RandByte(256)
    skycoin.cipher.SumSHA256(data, sha_sum)
    skycoin.cipher.SignHash(sha_sum, secret_key, sig_1)
    assert sig_1 !=  sig_2
    assert skycoin.cipher.ChkSig(addres, sha_sum, sig_1) == skycoin.SKY_OK

def test_TestPubKeyFromSecKey():
    public_key = skycoin.cipher.PubKey()
    secret_key = skycoin.cipher.SecKey()
    skycoin.cipher.GenerateKeyPair(public_key, secret_key)
    public_key_2 = skycoin.cipher.PubKey()
    skycoin.cipher.PubKeyFromSecKey(secret_key, public_key_2)
    assert public_key == public_key_2
    secret_key_2 = skycoin.cipher.SecKey()
    err = skycoin.cipher.PubKeyFromSecKey(secret_key_2, public_key)
    assert err == skycoin.SKY_ErrPubKeyFromNullSecKey
    _, data = skycoin.cipher.RandByte(99)
    err = skycoin.cipher.NewSecKey(data, secret_key)
    assert err == skycoin.SKY_ErrInvalidLengthSecKey
    _, data = skycoin.cipher.RandByte(31)
    err = skycoin.cipher.NewSecKey(data, secret_key) 
    assert err == skycoin.SKY_ErrInvalidLengthSecKey

def test_TestPubKeyFromSig():
    public_key = skycoin.cipher.PubKey()
    secret_key = skycoin.cipher.SecKey()
    skycoin.cipher.GenerateKeyPair(public_key, secret_key)
    sha_sum = skycoin.cipher.SHA256()
    _, data = skycoin.cipher.RandByte(256)
    skycoin.cipher.SumSHA256(data, sha_sum)
    sig_1 = skycoin.cipher.Sig()
    skycoin.cipher.SignHash(sha_sum, secret_key, sig_1)
    public_key_2 = skycoin.cipher.PubKey()
    assert skycoin.cipher.PubKeyFromSig(sig_1, sha_sum, public_key_2) == skycoin.SKY_OK
    assert public_key == public_key_2
    sig_2 = skycoin.cipher.Sig()
    assert skycoin.cipher.PubKeyFromSig(sig_2, sha_sum, public_key_2) == skycoin.SKY_ErrInvalidSigForPubKey

def test_TestVerifySignature():
    public_key = skycoin.cipher.PubKey()
    secret_key = skycoin.cipher.SecKey()
    skycoin.cipher.GenerateKeyPair(public_key, secret_key)
    sha_sum_1 = skycoin.cipher.SHA256()
    sha_sum_2 = skycoin.cipher.SHA256()
    _, data = skycoin.cipher.RandByte(256)
    skycoin.cipher.SumSHA256(data, sha_sum_1)
    _, data = skycoin.cipher.RandByte(256)
    skycoin.cipher.SumSHA256(data, sha_sum_2)
    sig_1 = skycoin.cipher.Sig()
    sig_2 = skycoin.cipher.Sig()
    skycoin.cipher.SignHash(sha_sum_1, secret_key, sig_1)
    assert skycoin.cipher.VerifySignature(public_key, sig_1, sha_sum_1) == skycoin.SKY_OK
    assert skycoin.cipher.VerifySignature(public_key, sig_2, sha_sum_1) == skycoin.SKY_ErrInvalidSigForPubKey
    assert skycoin.cipher.VerifySignature(public_key, sig_1, sha_sum_2) == skycoin.SKY_ErrPubKeyRecoverMismatch
    public_key_2 = skycoin.cipher.PubKey()
    skycoin.cipher.GenerateKeyPair(public_key_2, secret_key)
    assert skycoin.cipher.VerifySignature(public_key_2, sig_1, sha_sum_1) == skycoin.SKY_ErrPubKeyRecoverMismatch
    public_key_3 = skycoin.cipher.PubKey()
    assert skycoin.cipher.VerifySignature(public_key_3, sig_1, sha_sum_1) == skycoin.SKY_ErrPubKeyRecoverMismatch

def test_TestGenerateKeyPair():
    public_key = skycoin.cipher.PubKey()
    secret_key = skycoin.cipher.SecKey()
    skycoin.cipher.GenerateKeyPair(public_key, secret_key)
    err = skycoin.cipher.PubKeyVerify(public_key)
    assert err == skycoin.SKY_OK
    err = skycoin.cipher.SecKeyVerify(secret_key)
    assert err == skycoin.SKY_OK

def test_TestGenerateDeterministicKeyPair():
    # deterministic key pairs are useless as is because we can't
    # generate pair n+1, only pair 0
    public_key = skycoin.cipher.PubKey()
    secret_key = skycoin.cipher.SecKey()
    _, seed = skycoin.cipher.RandByte(32)
    skycoin.cipher.GenerateDeterministicKeyPair(seed, public_key, secret_key)
    err = skycoin.cipher.PubKeyVerify(public_key)
    assert err == skycoin.SKY_OK
    err = skycoin.cipher.SecKeyVerify(secret_key)
    assert err == skycoin.SKY_OK
    skycoin.cipher.GenerateDeterministicKeyPair(seed, public_key, secret_key)
    err = skycoin.cipher.PubKeyVerify(public_key)
    assert err == skycoin.SKY_OK
    err = skycoin.cipher.SecKeyVerify(secret_key)
    assert err == skycoin.SKY_OK
    
def test_TestSecKeTest():
    public_key = skycoin.cipher.PubKey()
    secret_key = skycoin.cipher.SecKey()
    secret_key_2 = skycoin.cipher.SecKey()
    skycoin.cipher.GenerateKeyPair(public_key, secret_key)
    err = skycoin.cipher.TestSecKey(secret_key) 
    assert err == skycoin.SKY_OK
    err = skycoin.cipher.TestSecKey(secret_key_2) 
    assert err == skycoin.SKY_ErrInvalidSecKyVerification

def test_TestSecKeyHashTest():
    public_key = skycoin.cipher.PubKey()
    secret_key = skycoin.cipher.SecKey()
    secret_key_2 = skycoin.cipher.SecKey()
    skycoin.cipher.GenerateKeyPair(public_key, secret_key)
    sha_sum_1 = skycoin.cipher.SHA256()
    _, data = skycoin.cipher.RandByte(256)
    skycoin.cipher.SumSHA256(data, sha_sum_1)
    err = skycoin.cipher.TestSecKeyHash(secret_key, sha_sum_1) 
    assert err == skycoin.SKY_OK
    err = skycoin.cipher.TestSecKeyHash(secret_key_2, sha_sum_1) 
    assert err == skycoin.SKY_ErrInvalidSecKyVerification

def test_TestGenerateDeterministicKeyPairsUsesAllBytes():
    # Tests that if a seed >128 bits is used, the generator does not ignore bits > 128
    seed = b"property diet little foster provide disagree witness mountain alley weekend kitten general"
    secret_keys =  skycoin.cipher.GenerateDeterministicKeyPairsSeed(seed, 3)[1:]
    secret_keys_2 =  skycoin.cipher.GenerateDeterministicKeyPairsSeed(seed[:16], 3)[1:]
    assert secret_keys != secret_keys_2

