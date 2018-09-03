import skycoin

def test_TestAddress1():
    address_hex = b"02fa939957e9fc52140e180264e621c2576a1bfe781f88792fb315ca3d1786afb8"
    assert len(address_hex) > 0
    public_key = skycoin.cipher.PubKey()
    err, hex_str = skycoin.base58.String2Hex(b"02fa939957e9fc52140e180264e621c2576a1bfe781f88792fb315ca3d1786afb8")
    assert err == skycoin.SKY_OK 
    err = skycoin.cipher.NewPubKey(hex_str, public_key)
    assert err == skycoin.SKY_OK 
    addres = skycoin.cipher.Address()
    err = skycoin.cipher.AddressFromPubKey(public_key, addres)
    assert err == skycoin.SKY_OK 


def test_TestAddress2():
    address_hex = b"5a42c0643bdb465d90bf673b99c14f5fa02db71513249d904573d2b8b63d353d"
    assert len(address_hex) > 0
    public_key = skycoin.cipher.PubKey()
    secret_key = skycoin.cipher.SecKey()
    err, hex_str = skycoin.base58.String2Hex(b"5a42c0643bdb465d90bf673b99c14f5fa02db71513249d904573d2b8b63d353d")
    assert err == skycoin.SKY_OK 
    err = skycoin.cipher.NewSecKey(hex_str, secret_key)
    assert err == skycoin.SKY_OK 
    err = skycoin.cipher.PubKeyFromSecKey(secret_key, public_key )
    assert err == skycoin.SKY_OK
    address = skycoin.cipher.Address()
    err = skycoin.cipher.AddressFromPubKey(public_key, address) 
    assert err == skycoin.SKY_OK


def test_TestCrypto1():
    public_key = skycoin.cipher.PubKey()
    secret_key = skycoin.cipher.SecKey()
    for _ in range(10):
        err = skycoin.cipher.GenerateKeyPair(public_key, secret_key)
        assert err == skycoin.SKY_OK
        err = skycoin.cipher.TestSecKey(secret_key)
        assert err == skycoin.SKY_OK


def test_TestCrypto2():
    err, hex_str = skycoin.base58.String2Hex(b"5a42c0643bdb465d90bf673b99c14f5fa02db71513249d904573d2b8b63d353d")
    assert err == skycoin.SKY_OK 
    assert  len(hex_str) == 32
    public_key = skycoin.cipher.PubKey()
    secret_key = skycoin.cipher.SecKey()
    err = skycoin.cipher.NewSecKey(hex_str, secret_key)
    assert err == skycoin.SKY_OK 
    err = skycoin.cipher.PubKeyFromSecKey(secret_key, public_key )
    assert err == skycoin.SKY_OK
    address = skycoin.cipher.Address()
    err = skycoin.cipher.AddressFromPubKey(public_key, address) 
    assert err == skycoin.SKY_OK
    text = b"test message"
    sha = skycoin.cipher.SHA256()
    err = skycoin.cipher.SumSHA256(text, sha)
    assert err == skycoin.SKY_OK
    err = skycoin.cipher.TestSecKeyHash(secret_key, sha)
    assert err == skycoin.SKY_OK