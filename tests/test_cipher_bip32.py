import skycoin
import tests.utils as utils


class testChildKey():
    path = b''
    privKey = b''
    pubKey = b''
    fingerprint = b''
    identifier = b''
    chainCode = b''
    hexPubKey = b''
    wifPrivKey = b''
    childNUmber = 0
    depth = 0


class testMasterKey():
    seed = b''
    children = []
    privKey = b''
    pubKey = b''
    hexPubKey = b''
    wifPrivKey = b''
    fingerprint = b''
    identifier = b''
    chainCode = b''
    childNUmber = 0
    depth = 0
    depthNumber = 0


def assertPrivateKeySerialization(key, expected):
    err, expectedBytes = skycoin.SKY_base58_Decode(expected)
    assert err == skycoin.SKY_OK
    err, serialized = skycoin.SKY_bip32_PrivateKey_Serialize(key)
    assert err == skycoin.SKY_OK
    err, key2 = skycoin.SKY_bip32_DeserializePrivateKey(serialized)
    assert err == skycoin.SKY_OK
    assert utils.isPrivateKeyEq(key, key2) == 1
    err, key3 = skycoin.SKY_bip32_DeserializeEncodedPrivateKey(expected)
    assert err == skycoin.SKY_OK
    assert utils.isPrivateKeyEq(key2, key3) == 1


def assertPublicKeySerialization(key, expected):
    err, expectedBytes = skycoin.SKY_base58_Decode(expected)
    assert err == skycoin.SKY_OK
    err, serialized = skycoin.SKY_bip32_PublicKey_Serialize(key)
    assert err == skycoin.SKY_OK
    err, key2 = skycoin.SKY_bip32_DeserializePublicKey(serialized)
    assert err == skycoin.SKY_OK
    assert utils.isPublicKeyEq(key, key2) == 1
    err, key3 = skycoin.SKY_bip32_DeserializeEncodedPublicKey(expected)
    assert err == skycoin.SKY_OK
    assert utils.isPublicKeyEq(key3, key2) == 1


def VectorKeyPairs(vector):
    # Decode master seed into hex
    err, seed = skycoin.SKY_base58_String2Hex(vector.seed)
    assert err == skycoin.SKY_OK
    # Generate a master private and public key
    err, privkey = skycoin.SKY_bip32_NewMasterKey(seed)
    assert err == skycoin.SKY_OK
    err, pubkey = skycoin.SKY_bip32_PrivateKey_Publickey(privkey)
    assert err == skycoin.SKY_OK

    err, depthPrivKey = skycoin.SKY_bip32_PrivateKey_GetDepth(privkey)
    assert err == skycoin.SKY_OK
    err, depthPubKey = skycoin.SKY_bip32_PublicKey_GetDepth(pubkey)
    assert err == skycoin.SKY_OK
    assert 0 == depthPubKey

    err, privchildNumber = skycoin.SKY_bip32_PrivateKey_ChildNumber(privkey)
    assert err == skycoin.SKY_OK
    err, pubchildNumber = skycoin.SKY_bip32_PublicKey_ChildNumber(pubkey)
    assert err == skycoin.SKY_OK
    assert vector.childNUmber == privchildNumber
    assert vector.childNUmber == pubchildNumber
    assertPrivateKeySerialization(privkey, vector.privKey)
    assertPublicKeySerialization(pubkey, vector.pubKey)

    err, b58pk = skycoin.SKY_base58_Decode(vector.privKey)
    assert err == skycoin.SKY_OK
    err, privKey2 = skycoin.SKY_bip32_DeserializePrivateKey(b58pk)
    assert err == skycoin.SKY_OK
    assert utils.isPrivateKeyEq(privkey, privKey2) == 1

    # Test that DeserializeEncodedPrivateKey
    # is equivalent to DeserializePrivateKey(base58.Decode(key))
    err, privKey3 = skycoin.SKY_bip32_DeserializeEncodedPrivateKey(
        vector.privKey)
    assert err == skycoin.SKY_OK
    assert utils.isPrivateKeyEq(privKey2, privKey3)

    for tck in vector.children:
        err, privkey = skycoin.SKY_bip32_NewPrivateKeyFromPath(seed, tck.path)
        assert err == skycoin.SKY_OK
        # Get this private key's public key
        err, pubkey = skycoin.SKY_bip32_PrivateKey_Publickey(privkey)
        assert err == skycoin.SKY_OK
        err, ppk = skycoin.SKY_base58_Decode(tck.privKey)
        assert err == skycoin.SKY_OK
        err, xx = skycoin.SKY_bip32_DeserializePrivateKey(ppk)
        assert err == skycoin.SKY_OK
        assert utils.isPrivateKeyEq(xx, privkey)
        err, stringPrivKey = skycoin.SKY_bip32_PrivateKey_String(privkey)
        assert err == skycoin.SKY_OK
        assert stringPrivKey == tck.privKey
        err, stringPubKey = skycoin.SKY_bip32_PublicKey_String(pubkey)
        assert err == skycoin.SKY_OK
        assert stringPubKey == tck.pubKey

        err, privChainCode = skycoin.SKY_bip32_PrivateKey_GetChainCode(privkey)
        assert err == skycoin.SKY_OK
        err, priv_ChainCode = skycoin.SKY_base58_Hex2String(privChainCode)
        assert priv_ChainCode == tck.chainCode
        assert err == skycoin.SKY_OK
        err, pubChainCode = skycoin.SKY_bip32_PublicKey_GetChainCode(pubkey)
        assert err == skycoin.SKY_OK
        err, pub_ChainCode = skycoin.SKY_base58_Hex2String(pubChainCode)
        assert pub_ChainCode == tck.chainCode

        err, privFringerprint = skycoin.SKY_bip32_PrivateKey_Fingerprint(
            privkey)
        assert err == skycoin.SKY_OK
        err, priv_Fringerprint = skycoin.SKY_base58_Hex2String(
            privFringerprint)
        assert err == skycoin.SKY_OK
        assert priv_Fringerprint == tck.fingerprint
        err, pubFringerprint = skycoin.SKY_bip32_PublicKey_Fingerprint(pubkey)
        assert err == skycoin.SKY_OK
        err, pub_Fringerprint = skycoin.SKY_base58_Hex2String(pubFringerprint)
        assert pub_Fringerprint == tck.fingerprint

        err, privIdentifier = skycoin.SKY_bip32_PrivateKey_Identifier(privkey)
        assert err == skycoin.SKY_OK
        err, priv_Identifier = skycoin.SKY_base58_Hex2String(privIdentifier)
        assert err == skycoin.SKY_OK
        assert priv_Identifier == tck.identifier
        err, pubIdentifier = skycoin.SKY_bip32_PublicKey_Identifier(pubkey)
        assert err == skycoin.SKY_OK
        err, pub_Identifier = skycoin.SKY_base58_Hex2String(pubIdentifier)
        assert err == skycoin.SKY_OK
        assert pub_Identifier == tck.identifier

        err, privDepth = skycoin.SKY_bip32_PrivateKey_GetDepth(privkey)
        assert err == skycoin.SKY_OK
        err, pubDepth = skycoin.SKY_bip32_PublicKey_GetDepth(pubkey)
        assert err == skycoin.SKY_OK
        assert tck.depth == privDepth
        assert tck.depth == pubDepth

        err, privchildNumber = skycoin.SKY_bip32_PrivateKey_ChildNumber(
            privkey)
        assert err == skycoin.SKY_OK
        err, pubchildNumber = skycoin.SKY_bip32_PublicKey_ChildNumber(pubkey)
        assert err == skycoin.SKY_OK
        assert tck.childNUmber == abs(privchildNumber)
        assert tck.childNUmber == abs(pubchildNumber)

        # Serialize and deserialize both keys and ensure they're the same
        assertPrivateKeySerialization(privkey, tck.privKey)
        assertPublicKeySerialization(pubkey, tck.pubKey)


def test_TestBip32TestVectors():
    vector1 = testMasterKey()
    vector1.seed = b'000102030405060708090a0b0c0d0e0f'
    vector1.privKey = b'xprv9s21ZrQH143K3QTDL4LXw2F7HEK3wJUD2nW2nRk4stbPy6cq3jPPqjiChkVvvNKmPGJxWUtg6LnF5kejMRNNU3TGtRBeJgk33yuGBxrMPHi'
    vector1.pubKey = b'xpub661MyMwAqRbcFtXgS5sYJABqqG9YLmC4Q1Rdap9gSE8NqtwybGhePY2gZ29ESFjqJoCu1Rupje8YtGqsefD265TMg7usUDFdp6W1EGMcet8'
    vector1.hexPubKey = b'0339a36013301597daef41fbe593a02cc513d0b55527ec2df1050e2e8ff49c85c2'
    vector1.wifPrivKey = b'L52XzL2cMkHxqxBXRyEpnPQZGUs3uKiL3R11XbAdHigRzDozKZeW'
    vector1.fingerprint = b'3442193e'
    vector1.identifier = b'3442193e1bb70916e914552172cd4e2dbc9df811'
    vector1.chainCode = b'873dff81c02f525623fd1fe5167eac3a55a049de3d314bb42ee227ffed37d508'
    vector1.childNUmber = 0
    vector1.depth = 0

    vector1.children = []
    children = testChildKey()
    children.path = b"m/0'"
    children.privKey = b'xprv9uHRZZhk6KAJC1avXpDAp4MDc3sQKNxDiPvvkX8Br5ngLNv1TxvUxt4cV1rGL5hj6KCesnDYUhd7oWgT11eZG7XnxHrnYeSvkzY7d2bhkJ7'
    children.pubKey = b'xpub68Gmy5EdvgibQVfPdqkBBCHxA5htiqg55crXYuXoQRKfDBFA1WEjWgP6LHhwBZeNK1VTsfTFUHCdrfp1bgwQ9xv5ski8PX9rL2dZXvgGDnw'
    children.fingerprint = b'5c1bd648'
    children.identifier = b'5c1bd648ed23aa5fd50ba52b2457c11e9e80a6a7'
    children.chainCode = b'47fdacbd0f1097043b78c63c20c34ef4ed9a111d980047ad16282c7ae6236141'
    children.hexPubKey = b'035a784662a4a20a65bf6aab9ae98a6c068a81c52e4b032c0fb5400c706cfccc56'
    children.wifPrivKey = b'L5BmPijJjrKbiUfG4zbiFKNqkvuJ8usooJmzuD7Z8dkRoTThYnAT'
    children.childNUmber = 2147483648
    children.depth = 1
    vector1.children.append(children)
    # Test running
    VectorKeyPairs(vector1)
