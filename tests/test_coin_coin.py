import skycoin

def test_TestAddress1():
    address_hex = b"02fa939957e9fc52140e180264e621c2576a1bfe781f88792fb315ca3d1786afb8"
    assert len(address_hex) > 0
    public_key = skycoin.cipher_PubKey()
    err, hex_str = skycoin.SKY_base58_String2Hex(b"02fa939957e9fc52140e180264e621c2576a1bfe781f88792fb315ca3d1786afb8")
    assert err == skycoin.SKY_OK 
    err = skycoin.SKY_cipher_NewPubKey(hex_str, public_key)
    assert err == skycoin.SKY_OK 
    addres = skycoin.cipher__Address()
    err = skycoin.SKY_cipher_AddressFromPubKey(public_key, addres)
    assert err == skycoin.SKY_OK 

def test_TestAddress2():
    address_hex = b"5a42c0643bdb465d90bf673b99c14f5fa02db71513249d904573d2b8b63d353d"
    assert len(address_hex) > 0
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    err, hex_str = skycoin.SKY_base58_String2Hex(b"5a42c0643bdb465d90bf673b99c14f5fa02db71513249d904573d2b8b63d353d")
    assert err == skycoin.SKY_OK 
    err = skycoin.SKY_cipher_NewSecKey(hex_str, secret_key)
    assert err == skycoin.SKY_OK 
    err = skycoin.SKY_cipher_PubKeyFromSecKey(secret_key, public_key )
    assert err == skycoin.SKY_OK
    addres = skycoin.cipher__Address()
    err = skycoin.SKY_cipher_AddressFromPubKey(public_key, addres) 
    assert err == skycoin.SKY_OK

def test_TestCrypto1():
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    for _ in range(10):
        err = skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
        assert err == skycoin.SKY_OK
        err = skycoin.SKY_cipher_TestSecKey(secret_key)
        assert err == skycoin.SKY_OK

def test_TestCrypto2():
    err, hex_str = skycoin.SKY_base58_String2Hex(b"5a42c0643bdb465d90bf673b99c14f5fa02db71513249d904573d2b8b63d353d")
    assert err == skycoin.SKY_OK 
    assert  len(hex_str) == 32
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    err = skycoin.SKY_cipher_NewSecKey(hex_str, secret_key)
    assert err == skycoin.SKY_OK 
    err = skycoin.SKY_cipher_PubKeyFromSecKey(secret_key, public_key )
    assert err == skycoin.SKY_OK
    addres = skycoin.cipher__Address()
    err = skycoin.SKY_cipher_AddressFromPubKey(public_key, addres) 
    assert err == skycoin.SKY_OK

    text = b"test message"
    sha = skycoin.cipher_SHA256()
    err = skycoin.SKY_cipher_SumSHA256(text, sha)
    assert err == skycoin.SKY_OK
    err = skycoin.SKY_cipher_TestSecKeyHash(secret_key, sha)
    assert err == skycoin.SKY_OK