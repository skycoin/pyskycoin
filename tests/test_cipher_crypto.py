import skycoin


def test_TestNewPubKey():
    public_key = skycoin.cipher_PubKey()
    _, data = skycoin.SKY_cipher_RandByte(31)
    assert skycoin.SKY_cipher_NewPubKey(data, public_key) != 0
    _, data = skycoin.SKY_cipher_RandByte(32)
    assert skycoin.SKY_cipher_NewPubKey(data, public_key) != 0
    _, data = skycoin.SKY_cipher_RandByte(34)
    assert skycoin.SKY_cipher_NewPubKey(data, public_key) != 0
    _, data = skycoin.SKY_cipher_RandByte(0)
    assert skycoin.SKY_cipher_NewPubKey(data, public_key) != 0
    _, data = skycoin.SKY_cipher_RandByte(100)
    assert skycoin.SKY_cipher_NewPubKey(data, public_key) != 0
    _, data = skycoin.SKY_cipher_RandByte(33)
    assert skycoin.SKY_cipher_NewPubKey(data, public_key) == 0
#    # assert public_key[:] == data


def test_TestPubKeyFromHex():
    public_key = skycoin.cipher_PubKey()
    public_key_2 = skycoin.cipher_PubKey()
    # Invalid hex
    assert skycoin.SKY_cipher_PubKeyFromHex(b'""', public_key) != 0 
    assert skycoin.SKY_cipher_PubKeyFromHex(b'"cascs"', public_key) != 0 
    # Invalid hex length
    _, data = skycoin.SKY_cipher_RandByte(33)
    skycoin.SKY_cipher_NewPubKey(data, public_key)
    _, public_key_hex = skycoin.SKY_cipher_PubKey_Hex(public_key)
    assert skycoin.SKY_cipher_MustPubKeyFromHex(public_key_hex[:int(len(public_key_hex) / 2)], public_key) != 0
    # Valid
    assert skycoin.SKY_cipher_MustPubKeyFromHex(public_key_hex, public_key_2) == 0
    assert public_key == public_key_2

def test_TestPubKeyHex():
    public_key = skycoin.cipher_PubKey()
    public_key_2 = skycoin.cipher_PubKey()
    _, data = skycoin.SKY_cipher_RandByte(33)
    skycoin.SKY_cipher_NewPubKey(data, public_key)
    _, public_key_hex = skycoin.SKY_cipher_PubKey_Hex(public_key)
    skycoin.SKY_cipher_MustPubKeyFromHex(public_key_hex, public_key_2)
    _, public_key_hex_2 = skycoin.SKY_cipher_PubKey_Hex(public_key_2)
    assert public_key == public_key_2
    assert public_key_hex == public_key_hex_2

def test_TestPubKeyVerify():
    # Random bytes should not be valid, most of the time
    failed = False
    for _ in range(10):
        public_key = skycoin.cipher_PubKey()
        _,  data = skycoin.SKY_cipher_RandByte(33)
        skycoin.SKY_cipher_NewPubKey(data, public_key)
        if skycoin.SKY_cipher_PubKey_Verify(public_key) != None:
            failed = True
            break
    assert failed is True 

def test_TestPubKeyVerifyNil():
    # Empty public key should not be valid
    public_key = skycoin.cipher_PubKey()
    assert skycoin.SKY_cipher_PubKey_Verify(public_key) != 0

def test_TestPubKeyVerifyDefault1():
    #  Generated pub key should be valid   
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    assert skycoin.SKY_cipher_PubKey_Verify(public_key) == 0
    
def test_TestPubKeyVerifyDefault2():
    for _ in range(1024):
        public_key = skycoin.cipher_PubKey()
        secret_key = skycoin.cipher_SecKey()
        skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
        assert skycoin.SKY_cipher_PubKey_Verify(public_key) == 0
    
# def test_TestPubKeyToAddressHash():
#     public_key = skycoin.cipher_PubKey()
#     secret_key = skycoin.cipher_SecKey()
#     skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
#     data = skycoin.cipher_Ripemd160()
#     skycoin.SKY_cipher_PubKey_ToAddressHash(public_key, data)
#     # Should be Ripemd160(SHA256(SHA256()))
#     skycoin.SKY_cipher_SumSHA256(p0, p1)
    ## x := sha256.Sum256(p[:])
    ## x = sha256.Sum256(x[:])
    ## rh := ripemd160.New()
    ## rh.Write(x[:])
    ## y := rh.Sum(nil)
    ## assert.True(t, bytes.Equal(h[:], y))

def test_TestPubKeyToAddress():
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    addres = skycoin.cipher__Address()
    skycoin.SKY_cipher_AddressFromPubKey(public_key, addres) 
    # func (self Address) Verify(key PubKey) error
    assert skycoin.SKY_cipher_Address_Verify(addres, public_key) == 0
    # func DecodeBase58Address(addr string) (Address, error)
    _, addres_str = skycoin.SKY_cipher_Address_String(addres)
    assert skycoin.SKY_cipher_DecodeBase58Address(addres_str, addres) == 0

def test_TestPubKeyToAddress2():
    for _ in range(1024):
        public_key = skycoin.cipher_PubKey()
        secret_key = skycoin.cipher_SecKey()
        skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
        addres = skycoin.cipher__Address()
        skycoin.SKY_cipher_AddressFromPubKey(public_key, addres) 
        # func (self Address) Verify(key PubKey) error
        assert skycoin.SKY_cipher_Address_Verify(addres, public_key) == 0
        # func DecodeBase58Address(addr string) (Address, error)
        _, addres_str = skycoin.SKY_cipher_Address_String(addres)
        assert skycoin.SKY_cipher_DecodeBase58Address(addres_str, addres) == 0
    
def test_TestMustNewSecKey():
    secret_key = skycoin.cipher_SecKey()
    _, data = skycoin.SKY_cipher_RandByte(31)
    assert skycoin.SKY_cipher_NewSecKey(data, secret_key) != 0
    _, data = skycoin.SKY_cipher_RandByte(33)
    assert skycoin.SKY_cipher_NewSecKey(data, secret_key) != 0
    _, data = skycoin.SKY_cipher_RandByte(34)
    assert skycoin.SKY_cipher_NewSecKey(data, secret_key) != 0
    _, data = skycoin.SKY_cipher_RandByte(0)
    assert skycoin.SKY_cipher_NewSecKey(data, secret_key) != 0
    _, data = skycoin.SKY_cipher_RandByte(100)
    assert skycoin.SKY_cipher_NewSecKey(data, secret_key) != 0
    _, data = skycoin.SKY_cipher_RandByte(32)
    assert skycoin.SKY_cipher_NewSecKey(data, secret_key) == 0
    # assert.True(t, bytes.Equal(p[:], b))

def test_TestMustSecKeyFromHex():
    secret_key = skycoin.cipher_SecKey()
    secret_key_2 = skycoin.cipher_SecKey()
    # Invalid hex
    assert skycoin.SKY_cipher_SecKeyFromHex(b'""', secret_key) != 0 
    assert skycoin.SKY_cipher_SecKeyFromHex(b'"cascs"', secret_key) != 0 
    # Invalid hex length
    _, data = skycoin.SKY_cipher_RandByte(32)
    skycoin.SKY_cipher_NewSecKey(data, secret_key)
    _, secret_key_hex = skycoin.SKY_cipher_SecKey_Hex(secret_key)
    assert skycoin.SKY_cipher_MustSecKeyFromHex(secret_key_hex[:int(len(secret_key_hex) / 2)], secret_key) != 0
    # Valid
    assert skycoin.SKY_cipher_MustSecKeyFromHex(secret_key_hex, secret_key_2) == 0
    assert secret_key == secret_key_2 

def test_TestSecKeyHex():
    secret_key = skycoin.cipher_SecKey()
    secret_key_2 = skycoin.cipher_SecKey()
    _, data = skycoin.SKY_cipher_RandByte(32)
    skycoin.SKY_cipher_NewSecKey(data, secret_key)
    _, secret_key_hex = skycoin.SKY_cipher_SecKey_Hex(secret_key)
    skycoin.SKY_cipher_MustSecKeyFromHex(secret_key_hex, secret_key_2)
    _, secret_key_hex_2 = skycoin.SKY_cipher_SecKey_Hex(secret_key_2)
    assert secret_key == secret_key_2
    assert secret_key_hex == secret_key_hex_2

def test_TestSecKeyVerify():
    # Empty secret key should not be valid
    secret_key = skycoin.cipher_SecKey()
    public_key = skycoin.cipher_PubKey()
    assert skycoin.SKY_cipher_SecKey_Verify(secret_key) != None
    # Generated sec key should be valid
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    assert skycoin.SKY_cipher_PubKey_Verify(public_key) == 0

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
    assert skycoin.SKY_cipher_NewSig(data, sig) != 0
    _, data = skycoin.SKY_cipher_RandByte(66)
    assert skycoin.SKY_cipher_NewSig(data, sig) != 0
    _, data = skycoin.SKY_cipher_RandByte(67)
    assert skycoin.SKY_cipher_NewSig(data, sig) != 0
    _, data = skycoin.SKY_cipher_RandByte(0)
    assert skycoin.SKY_cipher_NewSig(data, sig) != 0
    _, data = skycoin.SKY_cipher_RandByte(100)
    assert skycoin.SKY_cipher_NewSig(data, sig) != 0
    _, data = skycoin.SKY_cipher_RandByte(65)
    assert skycoin.SKY_cipher_NewSig(data, sig) == 0
#    # assert.True(t, bytes.Equal(p[:], b))

def test_TestMustSigFromHex():
    sig_1 = skycoin.cipher_Sig()
    sig_2 = skycoin.cipher_Sig()
    # Invalid hex
    assert skycoin.SKY_cipher_SigFromHex(b"", sig_1) != 0
    assert skycoin.SKY_cipher_SigFromHex(b"cascs", sig_1) != 0
    # Invalid hex length
    _, data = skycoin.SKY_cipher_RandByte(65)
    skycoin.SKY_cipher_NewSig(data, sig_1)
    _, sig_1_hex = skycoin.SKY_cipher_Sig_Hex(sig_1)
    assert skycoin.SKY_cipher_MustSigFromHex(sig_1_hex[:int(len(sig_1_hex) / 2)], sig_1) != 0
    # Valid 
    assert skycoin.SKY_cipher_MustSigFromHex(sig_1_hex, sig_2) == 0
    assert sig_1 == sig_2 

def tes_TestSigHex():
    sig_1 = skycoin.cipher_Sig()
    sig_2 = skycoin.cipher_Sig()
    _, data = skycoin.SKY_cipher_RandByte(65)
    skycoin.SKY_cipher_NewSig(data, sig_1)
    _, sig_hex_1 = skycoin.SKY_cipher_Sig_Hex(sig_1)
    skycoin.SKY_cipher_MustSigFromHex(sig_hex_1, sig_2)
    _, sig_hex_2 = skycoin.SKY_cipher_Sig_Hex(sig_2)
    assert sig_1 == sig_2
    assert sig_hex_1 == sig_hex_2

def test_TestChkSig():
    secret_key_1 = skycoin.cipher_SecKey()
    secret_key_2 = skycoin.cipher_SecKey()
    public_key_1 = skycoin.cipher_PubKey()
    public_key_2 = skycoin.cipher_PubKey()
    addres = skycoin.cipher__Address()
    addres_2 = skycoin.cipher__Address()
    sig_1 = skycoin.cipher_Sig()
    sig_2 = skycoin.cipher_Sig()
    sha_sum = skycoin.cipher_SHA256()
    sha_sum_2 = skycoin.cipher_SHA256()
    skycoin.SKY_cipher_GenerateKeyPair(public_key_1, secret_key_1)
    skycoin.SKY_cipher_PubKey_Verify(public_key_1)
    skycoin.SKY_cipher_SecKey_Verify(secret_key_1)
    skycoin.SKY_cipher_AddressFromPubKey(public_key_1, addres)
    _, data = skycoin.SKY_cipher_RandByte(256)
    skycoin.SKY_cipher_SumSHA256(data, sha_sum)
    skycoin.SKY_cipher_SignHash(sha_sum, secret_key_1, sig_1)
    assert skycoin.SKY_cipher_ChkSig(addres, sha_sum, sig_1) == 0
    # Empty sig should be invalid
    assert skycoin.SKY_cipher_ChkSig(addres, sha_sum, sig_2) != 0
    # Random sigs should not pass
    for _ in range(100):
        _, data = skycoin.SKY_cipher_RandByte(65)
        skycoin.SKY_cipher_NewSig(data, sig_1)
        assert skycoin.SKY_cipher_ChkSig(addres, sha_sum, sig_1) != 0
    # Sig for one hash does not work for another hash
    _, data = skycoin.SKY_cipher_RandByte(256)
    skycoin.SKY_cipher_SumSHA256(data, sha_sum_2)
    skycoin.SKY_cipher_SignHash(sha_sum_2, secret_key_1, sig_2)
    assert skycoin.SKY_cipher_ChkSig(addres, sha_sum_2, sig_2) == 0
    assert skycoin.SKY_cipher_ChkSig(addres, sha_sum, sig_2) != 0
    assert skycoin.SKY_cipher_ChkSig(addres, sha_sum_2, sig_1) != 0
    # Different secret keys should not create same sig
    skycoin.SKY_cipher_GenerateKeyPair(public_key_2, secret_key_2)
    skycoin.SKY_cipher_AddressFromPubKey(public_key_2, addres_2)
    sha_sum = skycoin.cipher_SHA256()
    skycoin.SKY_cipher_SignHash(sha_sum, secret_key_1, sig_1)
    skycoin.SKY_cipher_SignHash(sha_sum, secret_key_2, sig_2)
    assert skycoin.SKY_cipher_ChkSig(addres, sha_sum, sig_1) == 0
    assert skycoin.SKY_cipher_ChkSig(addres_2, sha_sum, sig_2) == 0
    assert sig_1 != sig_2
    _, data = skycoin.SKY_cipher_RandByte(256)
    skycoin.SKY_cipher_SumSHA256(data, sha_sum)
    skycoin.SKY_cipher_SignHash(sha_sum, secret_key_1, sig_1)
    skycoin.SKY_cipher_SignHash(sha_sum, secret_key_2, sig_2)
    assert skycoin.SKY_cipher_ChkSig(addres, sha_sum, sig_1) == 0
    assert skycoin.SKY_cipher_ChkSig(addres_2, sha_sum, sig_2) == 0
    assert sig_1 != sig_2
    # Bad address should be invalid
    assert skycoin.SKY_cipher_ChkSig(addres, sha_sum, sig_2) != 0
    assert skycoin.SKY_cipher_ChkSig(addres_2, sha_sum, sig_1) != 0

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
    assert sig_1 !=  sig_2
    assert skycoin.SKY_cipher_ChkSig(addres, sha_sum, sig_1) == 0

def test_TestPubKeyFromSecKey():
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    public_key_2 = skycoin.cipher_PubKey()
    skycoin.SKY_cipher_PubKeyFromSecKey(secret_key, public_key_2)
    assert public_key == public_key_2
    secret_key_2 = skycoin.cipher_SecKey()
    assert skycoin.SKY_cipher_PubKeyFromSecKey(secret_key_2, public_key) != 0
    _, data = skycoin.SKY_cipher_RandByte(99)
    assert skycoin.SKY_cipher_NewSecKey(data, secret_key) != 0
    _, data = skycoin.SKY_cipher_RandByte(31)
    assert skycoin.SKY_cipher_NewSecKey(data, secret_key) != 0

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
    assert skycoin.SKY_cipher_PubKeyFromSig(sig_1, sha_sum, public_key_2) == 0
    assert public_key == public_key_2
    sig_2 = skycoin.cipher_Sig()
    assert skycoin.SKY_cipher_PubKeyFromSig(sig_2, sha_sum, public_key_2) != 0

def test_TestVerifySignature():
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    sha_sum_1 = skycoin.cipher_SHA256()
    sha_sum_2 = skycoin.cipher_SHA256()
    _, data = skycoin.SKY_cipher_RandByte(256)
    skycoin.SKY_cipher_SumSHA256(data, sha_sum_1)
    _, data = skycoin.SKY_cipher_RandByte(256)
    skycoin.SKY_cipher_SumSHA256(data, sha_sum_2)
    sig_1 = skycoin.cipher_Sig()
    sig_2 = skycoin.cipher_Sig()
    skycoin.SKY_cipher_SignHash(sha_sum_1, secret_key, sig_1)
    assert skycoin.SKY_cipher_VerifySignature(public_key, sig_1, sha_sum_1) == 0
    assert skycoin.SKY_cipher_VerifySignature(public_key, sig_2, sha_sum_1) != 0
    assert skycoin.SKY_cipher_VerifySignature(public_key, sig_1, sha_sum_2) != 0
    public_key_2 = skycoin.cipher_PubKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key_2, secret_key)
    assert skycoin.SKY_cipher_VerifySignature(public_key_2, sig_1, sha_sum_1) != 0
    public_key_3 = skycoin.cipher_PubKey()
    assert skycoin.SKY_cipher_VerifySignature(public_key_3, sig_1, sha_sum_1) != 0

def test_TestGenerateKeyPair():
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    assert skycoin.SKY_cipher_PubKey_Verify(public_key) == 0
    assert skycoin.SKY_cipher_SecKey_Verify(secret_key) == 0

def test_TestGenerateDeterministicKeyPair():
    # TODO -- deterministic key pairs are useless as is because we can't
	# generate pair n+1, only pair 0
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    _, seed = skycoin.SKY_cipher_RandByte(32)
    skycoin.SKY_cipher_GenerateDeterministicKeyPair(seed, public_key, secret_key)
    assert skycoin.SKY_cipher_PubKey_Verify(public_key) == 0
    assert skycoin.SKY_cipher_SecKey_Verify(secret_key) == 0
    skycoin.SKY_cipher_GenerateDeterministicKeyPair(seed, public_key, secret_key)
    assert skycoin.SKY_cipher_PubKey_Verify(public_key) == 0
    assert skycoin.SKY_cipher_SecKey_Verify(secret_key) == 0
    
def test_TestSecKeTest():
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    secret_key_2 = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    assert skycoin.SKY_cipher_TestSecKey(secret_key) == 0
    assert skycoin.SKY_cipher_TestSecKey(secret_key_2) != 0

def test_TestSecKeyHashTest():
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    secret_key_2 = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    sha_sum_1 = skycoin.cipher_SHA256()
    _, data = skycoin.SKY_cipher_RandByte(256)
    skycoin.SKY_cipher_SumSHA256(data, sha_sum_1)
    assert skycoin.SKY_cipher_TestSecKeyHash(secret_key, sha_sum_1) == 0
    assert skycoin.SKY_cipher_TestSecKeyHash(secret_key_2, sha_sum_1) != 0

def test_TestGenerateDeterministicKeyPairsUsesAllBytes():
    # Tests that if a seed >128 bits is used, the generator does not ignore bits > 128
    seed = "property diet little foster provide disagree witness mountain alley weekend kitten general"
    secret_keys =  skycoin.SKY_cipher_GenerateDeterministicKeyPairsSeed(seed, 3)[1:]
    secret_keys_2 =  skycoin.SKY_cipher_GenerateDeterministicKeyPairsSeed(seed[:16], 3)[1:]
    assert secret_keys != secret_keys_2

