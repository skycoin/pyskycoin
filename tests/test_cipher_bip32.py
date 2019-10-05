import skycoin
import tests.utils as utils

FirstHardenedChild = 0x80000000


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
    err, expectedStr = skycoin.SKY_base58_Encode(expectedBytes)
    assert err == skycoin.SKY_OK
    err, serializedStr = skycoin.SKY_base58_Encode(serialized)
    assert err == skycoin.SKY_OK
    assert expectedStr == expected
    assert expectedStr == serializedStr
    assert expectedBytes == serialized
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
    assert expectedBytes == serialized
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
    err, privKey = skycoin.SKY_bip32_NewMasterKey(seed)
    assert err == skycoin.SKY_OK
    err, pubKey = skycoin.SKY_bip32_PrivateKey_Publickey(privKey)
    assert err == skycoin.SKY_OK

    err, depthPrivKey = skycoin.SKY_bip32_PrivateKey_GetDepth(privKey)
    assert err == skycoin.SKY_OK
    err, depthPubKey = skycoin.SKY_bip32_PublicKey_GetDepth(pubKey)
    assert err == skycoin.SKY_OK
    assert 0 == depthPubKey
    assert 0 == depthPrivKey

    err, privchildNumber = skycoin.SKY_bip32_PrivateKey_ChildNumber(privKey)
    assert err == skycoin.SKY_OK
    err, pubchildNumber = skycoin.SKY_bip32_PublicKey_ChildNumber(pubKey)
    assert err == skycoin.SKY_OK
    assert 0 == privchildNumber
    assert 0 == pubchildNumber

    err, privStr = skycoin.SKY_bip32_PrivateKey_String(privKey)
    assert err == skycoin.SKY_OK
    assert vector.privKey == privStr
    err, pubStr = skycoin.SKY_bip32_PublicKey_String(pubKey)
    assert err == skycoin.SKY_OK
    assert pubStr == vector.pubKey

    err, pub_key = skycoin.SKY_bip32_PublicKey_GetKey(pubKey)
    assert err == skycoin.SKY_OK
    err, pub_keyStr = skycoin.SKY_base58_Hex2String(pub_key)
    assert err == skycoin.SKY_OK
    assert vector.hexPubKey == pub_keyStr

    err, priv_ChainCode = skycoin.SKY_bip32_PrivateKey_GetChainCode(privKey)
    assert err == skycoin.SKY_OK
    err, priv_ChainCodeStr = skycoin.SKY_base58_Hex2String(priv_ChainCode)
    assert err == skycoin.SKY_OK
    assert vector.chainCode == priv_ChainCodeStr
    err, pub_ChainCode = skycoin.SKY_bip32_PublicKey_GetChainCode(pubKey)
    assert err == skycoin.SKY_OK
    err, priv_ChainCodeStr = skycoin.SKY_base58_Hex2String(priv_ChainCode)
    assert err == skycoin.SKY_OK
    assert vector.chainCode == priv_ChainCodeStr

    assertPrivateKeySerialization(privKey, vector.privKey)
    assertPublicKeySerialization(pubKey, vector.pubKey)

    err, b58pk = skycoin.SKY_base58_Decode(vector.privKey)
    assert err == skycoin.SKY_OK
    err, privKey2 = skycoin.SKY_bip32_DeserializePrivateKey(b58pk)
    assert err == skycoin.SKY_OK
    assert utils.isPrivateKeyEq(privKey, privKey2) == 1

    # Test that DeserializeEncodedPrivateKey
    # is equivalent to DeserializePrivateKey(base58.Decode(key))
    err, privKey3 = skycoin.SKY_bip32_DeserializeEncodedPrivateKey(
        vector.privKey)
    assert err == skycoin.SKY_OK
    assert utils.isPrivateKeyEq(privKey2, privKey3)

    for tck in vector.children:
        print("Depth ", tck.depth)
        err, privkey1 = skycoin.SKY_bip32_NewPrivateKeyFromPath(seed, tck.path)
        assert err == skycoin.SKY_OK
        # Get this private key's public key
        err, pubkey1 = skycoin.SKY_bip32_PrivateKey_Publickey(privkey1)
        assert err == skycoin.SKY_OK
        err, ppk = skycoin.SKY_base58_Decode(tck.privKey)
        assert err == skycoin.SKY_OK
        err, xx = skycoin.SKY_bip32_DeserializePrivateKey(ppk)
        assert err == skycoin.SKY_OK
        assert utils.isPrivateKeyEq(xx, privkey1)
        err, stringPrivKey = skycoin.SKY_bip32_PrivateKey_String(privkey1)
        assert err == skycoin.SKY_OK
        assert stringPrivKey == tck.privKey
        err, stringPubKey = skycoin.SKY_bip32_PublicKey_String(pubkey1)
        assert err == skycoin.SKY_OK
        assert stringPubKey == tck.pubKey

        err, privChainCode = skycoin.SKY_bip32_PrivateKey_GetChainCode(
            privkey1)
        assert err == skycoin.SKY_OK
        err, priv_ChainCode = skycoin.SKY_base58_Hex2String(privChainCode)
        assert priv_ChainCode == tck.chainCode
        assert err == skycoin.SKY_OK
        err, pubChainCode = skycoin.SKY_bip32_PublicKey_GetChainCode(pubkey1)
        assert err == skycoin.SKY_OK
        err, pub_ChainCode = skycoin.SKY_base58_Hex2String(pubChainCode)
        assert pub_ChainCode == tck.chainCode

        err, privFringerprint = skycoin.SKY_bip32_PrivateKey_Fingerprint(
            privkey1)
        assert err == skycoin.SKY_OK
        err, priv_Fringerprint = skycoin.SKY_base58_Hex2String(
            privFringerprint)
        assert err == skycoin.SKY_OK
        assert priv_Fringerprint == tck.fingerprint
        err, pubFringerprint = skycoin.SKY_bip32_PublicKey_Fingerprint(pubkey1)
        assert err == skycoin.SKY_OK
        err, pub_Fringerprint = skycoin.SKY_base58_Hex2String(pubFringerprint)
        assert pub_Fringerprint == tck.fingerprint

        err, privIdentifier = skycoin.SKY_bip32_PrivateKey_Identifier(privkey1)
        assert err == skycoin.SKY_OK
        err, priv_Identifier = skycoin.SKY_base58_Hex2String(privIdentifier)
        assert err == skycoin.SKY_OK
        assert priv_Identifier == tck.identifier
        err, pubIdentifier = skycoin.SKY_bip32_PublicKey_Identifier(pubkey1)
        assert err == skycoin.SKY_OK
        err, pub_Identifier = skycoin.SKY_base58_Hex2String(pubIdentifier)
        assert err == skycoin.SKY_OK
        assert pub_Identifier == tck.identifier

        err, privDepth = skycoin.SKY_bip32_PrivateKey_GetDepth(privkey1)
        assert err == skycoin.SKY_OK
        err, pubDepth = skycoin.SKY_bip32_PublicKey_GetDepth(pubkey1)
        assert err == skycoin.SKY_OK
        assert tck.depth == privDepth
        assert tck.depth == pubDepth

        err, privchildNumber = skycoin.SKY_bip32_PrivateKey_ChildNumber(
            privkey1)
        assert err == skycoin.SKY_OK
        assert tck.childNUmber == privchildNumber

        err, pubchildNumber = skycoin.SKY_bip32_PublicKey_ChildNumber(pubkey1)
        assert err == skycoin.SKY_OK
        assert tck.childNUmber == pubchildNumber

        # Serialize and deserialize both keys and ensure they're the same
        assertPrivateKeySerialization(privkey1, tck.privKey)
        assertPublicKeySerialization(pubkey1, tck.pubKey)


def test_TestBip32TestVectors():
    vector = []

    vector1 = testMasterKey()
    vector1.seed = b'000102030405060708090a0b0c0d0e0f'
    vector1.privKey = b"xprv9s21ZrQH143K3QTDL4LXw2F7HEK3wJUD2nW2nRk4stbPy6cq3jPPqjiChkVvvNKmPGJxWUtg6LnF5kejMRNNU3TGtRBeJgk33yuGBxrMPHi"
    vector1.pubKey = b"xpub661MyMwAqRbcFtXgS5sYJABqqG9YLmC4Q1Rdap9gSE8NqtwybGhePY2gZ29ESFjqJoCu1Rupje8YtGqsefD265TMg7usUDFdp6W1EGMcet8"
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

    children = testChildKey()
    children.path = b"m/0'/1"
    children.privKey = b"xprv9wTYmMFdV23N2TdNG573QoEsfRrWKQgWeibmLntzniatZvR9BmLnvSxqu53Kw1UmYPxLgboyZQaXwTCg8MSY3H2EU4pWcQDnRnrVA1xe8fs"
    children.pubKey = b"xpub6ASuArnXKPbfEwhqN6e3mwBcDTgzisQN1wXN9BJcM47sSikHjJf3UFHKkNAWbWMiGj7Wf5uMash7SyYq527Hqck2AxYysAA7xmALppuCkwQ"
    children.fingerprint = b"bef5a2f9"
    children.identifier = b"bef5a2f9a56a94aab12459f72ad9cf8cf19c7bbe"
    children.chainCode = b"2a7857631386ba23dacac34180dd1983734e444fdbf774041578e9b6adb37c19"
    children.hexPubKey = b"03501e454bf00751f24b1b489aa925215d66af2234e3891c3b21a52bedb3cd711c"
    children.wifPrivKey = b"KyFAjQ5rgrKvhXvNMtFB5PCSKUYD1yyPEe3xr3T34TZSUHycXtMM"
    children.depth = 2
    children.childNUmber = 1
    vector1.children.append(children)

    children = testChildKey()
    children.path = b"m/0'/1/2'"
    children.privKey = b"xprv9z4pot5VBttmtdRTWfWQmoH1taj2axGVzFqSb8C9xaxKymcFzXBDptWmT7FwuEzG3ryjH4ktypQSAewRiNMjANTtpgP4mLTj34bhnZX7UiM"
    children.pubKey = b"xpub6D4BDPcP2GT577Vvch3R8wDkScZWzQzMMUm3PWbmWvVJrZwQY4VUNgqFJPMM3No2dFDFGTsxxpG5uJh7n7epu4trkrX7x7DogT5Uv6fcLW5"
    children.fingerprint = b"ee7ab90c"
    children.identifier = b"ee7ab90cde56a8c0e2bb086ac49748b8db9dce72"
    children.chainCode = b"04466b9cc8e161e966409ca52986c584f07e9dc81f735db683c3ff6ec7b1503f"
    children.hexPubKey = b"0357bfe1e341d01c69fe5654309956cbea516822fba8a601743a012a7896ee8dc2"
    children.wifPrivKey = b"L43t3od1Gh7Lj55Bzjj1xDAgJDcL7YFo2nEcNaMGiyRZS1CidBVU"
    children.childNUmber = 2 + FirstHardenedChild
    children.depth = 3
    vector1.children.append(children)

    children = testChildKey()
    children.path = b"m/0'/1/2'/2"
    children.privKey = b"xprvA2JDeKCSNNZky6uBCviVfJSKyQ1mDYahRjijr5idH2WwLsEd4Hsb2Tyh8RfQMuPh7f7RtyzTtdrbdqqsunu5Mm3wDvUAKRHSC34sJ7in334"
    children.pubKey = b"xpub6FHa3pjLCk84BayeJxFW2SP4XRrFd1JYnxeLeU8EqN3vDfZmbqBqaGJAyiLjTAwm6ZLRQUMv1ZACTj37sR62cfN7fe5JnJ7dh8zL4fiyLHV"
    children.fingerprint = b"d880d7d8"
    children.identifier = b"d880d7d893848509a62d8fb74e32148dac68412f"
    children.chainCode = b"cfb71883f01676f587d023cc53a35bc7f88f724b1f8c2892ac1275ac822a3edd"
    children.hexPubKey = b"02e8445082a72f29b75ca48748a914df60622a609cacfce8ed0e35804560741d29"
    children.wifPrivKey = b"KwjQsVuMjbCP2Zmr3VaFaStav7NvevwjvvkqrWd5Qmh1XVnCteBR"
    children.childNUmber = 2
    children.depth = 4
    vector1.children.append(children)

    children = testChildKey()
    children.path = b"m/0'/1/2'/2/1000000000"
    children.privKey = b"xprvA41z7zogVVwxVSgdKUHDy1SKmdb533PjDz7J6N6mV6uS3ze1ai8FHa8kmHScGpWmj4WggLyQjgPie1rFSruoUihUZREPSL39UNdE3BBDu76"
    children.pubKey = b"xpub6H1LXWLaKsWFhvm6RVpEL9P4KfRZSW7abD2ttkWP3SSQvnyA8FSVqNTEcYFgJS2UaFcxupHiYkro49S8yGasTvXEYBVPamhGW6cFJodrTHy"
    children.fingerprint = b"d69aa102"
    children.identifier = b"d69aa102255fed74378278c7812701ea641fdf32"
    children.chainCode = b"c783e67b921d2beb8f6b389cc646d7263b4145701dadd2161548a8b078e65e9e"
    children.hexPubKey = b"022a471424da5e657499d1ff51cb43c47481a03b1e77f951fe64cec9f5a48f7011"
    children.wifPrivKey = b"Kybw8izYevo5xMh1TK7aUr7jHFCxXS1zv8p3oqFz3o2zFbhRXHYs"
    children.childNUmber = 1000000000
    children.depth = 5
    vector1.children.append(children)

    vector.append(vector1)

    vector2 = testMasterKey()
    vector2.seed = b"fffcf9f6f3f0edeae7e4e1dedbd8d5d2cfccc9c6c3c0bdbab7b4b1aeaba8a5a29f9c999693908d8a8784817e7b7875726f6c696663605d5a5754514e4b484542"
    vector2.privKey = b"xprv9s21ZrQH143K31xYSDQpPDxsXRTUcvj2iNHm5NUtrGiGG5e2DtALGdso3pGz6ssrdK4PFmM8NSpSBHNqPqm55Qn3LqFtT2emdEXVYsCzC2U"
    vector2.pubKey = b"xpub661MyMwAqRbcFW31YEwpkMuc5THy2PSt5bDMsktWQcFF8syAmRUapSCGu8ED9W6oDMSgv6Zz8idoc4a6mr8BDzTJY47LJhkJ8UB7WEGuduB"
    vector2.fingerprint = b"bd16bee5"
    vector2.identifier = b"bd16bee53961a47d6ad888e29545434a89bdfe95"
    vector2.chainCode = b"60499f801b896d83179a4374aeb7822aaeaceaa0db1f85ee3e904c4defbd9689"
    vector2.hexPubKey = b"03cbcaa9c98c877a26977d00825c956a238e8dddfbd322cce4f74b0b5bd6ace4a7"
    vector2.wifPrivKey = b"KyjXhyHF9wTphBkfpxjL8hkDXDUSbE3tKANT94kXSyh6vn6nKaoy"
    children = testChildKey()
    children.path = b"m/0"
    children.privKey = b"xprv9vHkqa6EV4sPZHYqZznhT2NPtPCjKuDKGY38FBWLvgaDx45zo9WQRUT3dKYnjwih2yJD9mkrocEZXo1ex8G81dwSM1fwqWpWkeS3v86pgKt"
    children.pubKey = b"xpub69H7F5d8KSRgmmdJg2KhpAK8SR3DjMwAdkxj3ZuxV27CprR9LgpeyGmXUbC6wb7ERfvrnKZjXoUmmDznezpbZb7ap6r1D3tgFxHmwMkQTPH"
    children.fingerprint = b"5a61ff8e"
    children.identifier = b"5a61ff8eb7aaca3010db97ebda76121610b78096"
    children.chainCode = b"f0909affaa7ee7abe5dd4e100598d4dc53cd709d5a5c2cac40e7412f232f7c9c"
    children.hexPubKey = b"02fc9e5af0ac8d9b3cecfe2a888e2117ba3d089d8585886c9c826b6b22a98d12ea"
    children.wifPrivKey = b"L2ysLrR6KMSAtx7uPqmYpoTeiRzydXBattRXjXz5GDFPrdfPzKbj"
    children.childNUmber = 0
    children.depth = 1
    vector2.children.append(children)

    children = testChildKey()
    children.path = b"m/0/2147483647'"
    children.privKey = b"xprv9wSp6B7kry3Vj9m1zSnLvN3xH8RdsPP1Mh7fAaR7aRLcQMKTR2vidYEeEg2mUCTAwCd6vnxVrcjfy2kRgVsFawNzmjuHc2YmYRmagcEPdU9"
    children.pubKey = b"xpub6ASAVgeehLbnwdqV6UKMHVzgqAG8Gr6riv3Fxxpj8ksbH9ebxaEyBLZ85ySDhKiLDBrQSARLq1uNRts8RuJiHjaDMBU4Zn9h8LZNnBC5y4a"
    children.fingerprint = b"d8ab4937"
    children.identifier = b"d8ab493736da02f11ed682f88339e720fb0379d1"
    children.chainCode = b"be17a268474a6bb9c61e1d720cf6215e2a88c5406c4aee7b38547f585c9a37d9"
    children.hexPubKey = b"03c01e7425647bdefa82b12d9bad5e3e6865bee0502694b94ca58b666abc0a5c3b"
    children.wifPrivKey = b"L1m5VpbXmMp57P3knskwhoMTLdhAAaXiHvnGLMribbfwzVRpz2Sr"
    children.childNUmber = 2147483647 + FirstHardenedChild
    children.depth = 2
    vector2.children.append(children)

    vector.append(vector2)

    # Test running
    i = 0
    for v in vector:
        print("Vector ", i)
        VectorKeyPairs(v)
        i += 1


class testStruct:
    err = skycoin.SKY_OK
    base58 = b""


def test_TestDeserializePrivateInvalidStrings():
    tests = []

    childen = testStruct()
    childen.err = skycoin.SKY_ErrSerializedKeyWrongSize
    childen.base58 = b"xprv9s21ZrQH143K4YUcKrp6cVxQaX59ZFkN6MFdeZjt8CHVYNs55xxQSvZpHWfojWMv6zgjmzopCyWPSFAnV4RU33J4pwCcnhsB4R4mPEnTsM"
    tests.append(childen)

    childen = testStruct()
    childen.err = skycoin.SKY_bip32_ErrInvalidChecksum
    childen.base58 = b"xprv9s21ZrQH143K3YSbAXLMPCzJso5QAarQksAGc5rQCyZCBfw4Rj2PqVLFNgezSBhktYkiL3Ta2stLPDF9yZtLMaxk6Spiqh3DNFG8p8MVeEc"
    tests.append(childen)

    childen = testStruct()
    childen.err = skycoin.SKY_ErrInvalidPrivateKeyVersion
    childen.base58 = b"xpub6DxSCdWu6jKqr4isjo7bsPeDD6s3J4YVQV1JSHZg12Eagdqnf7XX4fxqyW2sLhUoFWutL7tAELU2LiGZrEXtjVbvYptvTX5Eoa4Mamdjm9u"
    tests.append(childen)

    childen = testStruct()
    childen.err = skycoin.SKY_ErrInvalidKeyVersion
    childen.base58 = b"8FH81Rao5EgGmdScoN66TJAHsQP7phEMeyMTku9NBJd7hXgaj3HTvSNjqJjoqBpxdbuushwPEM5otvxXt2p9dcw33AqNKzZEPMqGHmz7Dpayi6Vb"
    tests.append(childen)

    childen = testStruct()
    childen.err = skycoin.SKY_bip32_ErrInvalidChecksum
    childen.base58 = b"xprvQQQQQQQQQQQQQQQQCviVfJSKyQ1mDYahRjijr5idH2WwLsEd4Hsb2Tyh8RfQMuPh7f7RtyzTtdrbdqqsunu5Mm3wDvUAKRHSC34sJ7in334"
    tests.append(childen)

    childen = testStruct()
    childen.err = skycoin.SKY_ErrSerializedKeyWrongSize
    childen.base58 = b"HAsbc6CgKmTYEQg2CTz7m5STEPAB"
    tests.append(childen)

    childen = testStruct()
    childen.err = skycoin.SKY_ErrInvalidFingerprint
    childen.base58 = b"xprv9tnJFvAXAXPfPnMTKfwpwnkty7MzJwELVgp4NTBquaKXy4RndyfJJCJJf7zNaVpBpzrwVRutZNLRCVLEcZHcvuCNG3zGbGBcZn57FbNnmSP"
    tests.append(childen)

    childen = testStruct()
    childen.err = skycoin.SKY_ErrInvalidPrivateKey
    childen.base58 = b"xprv9s21ZrQH143K3yLysFvsu3n1dMwhNusmNHr7xArzAeCc7MQYqDBBStmqnZq6WLi668siBBNs3SjiyaexduHu9sXT9ixTsqptL67ADqcaBdm"
    tests.append(childen)

    childen = testStruct()
    childen.err = skycoin.SKY_ErrInvalidChildNumber
    childen.base58 = b"xprv9s21ZrQYdgnodnKW4Drm1Qg7poU6Gf2WUDsjPxvYiK7iLBMrsjbnF1wsZZQgmXNeMSG3s7jmHk1b3JrzhG5w8mwXGxqFxfrweico7k8DtxR"
    tests.append(childen)

    childen = testStruct()
    childen.err = skycoin.SKY_ErrInvalidKeyVersion
    childen.base58 = b"1111111111111adADjFaSNPxwXqLjHLj4mBfYxuewDPbw9hEj1uaXCzMxRPXDFF3cUoezTFYom4sEmEVSQmENPPR315cFk9YUFVek73wE9"
    tests.append(childen)

    childen = testStruct()
    childen.err = skycoin.SKY_ErrSerializedKeyWrongSize
    childen.base58 = b"9XpNiB4DberdMn4jZiMhNGtuZUd7xUrCEGw4MG967zsVNvUKBEC9XLrmVmFasanWGp15zXfTNw4vW4KdvUAynEwyKjdho9QdLMPA2H5uyt"
    tests.append(childen)

    childen = testStruct()
    childen.err = skycoin.SKY_ErrSerializedKeyWrongSize
    childen.base58 = b"7JJikZQ2NUXjSAnAF2SjFYE3KXbnnVxzRBNddFE1DjbDEHVGEJzYC7zqSgPoauBJS3cWmZwsER94oYSFrW9vZ4Ch5FtGeifdzmtS3FGYDB1vxFZsYKgMc"
    tests.append(childen)

    for test in tests:
        print(test.base58)
        err, b = skycoin.SKY_base58_Decode(test.base58)
        assert err == skycoin.SKY_OK

        err, _ = skycoin.SKY_bip32_DeserializePrivateKey(b)
        assert err == test.err


def test_TestDeserializePublicInvalidStrings():
    tests = []

    childen = testStruct()
    childen.err = skycoin.SKY_ErrSerializedKeyWrongSize
    childen.base58 = b"xpub661MyMwAqRbcFtXgS5sYJABqqG9YLmC4Q1Rdap9gSE8NqtwybGhePY2gZ29ESFjqJoCu1Rupje8YtGqsefD265TMg7usUDFdp6W1EGMcet888"
    tests.append(childen)

    childen = testStruct()
    childen.err = skycoin.SKY_bip32_ErrInvalidChecksum
    childen.base58 = b"xpub661MyMwAqRbcFtXgS5sYJABqqG9YLmC4Q1Rdap9gSE8NqtwybGhePY2gZ29ESFjqJoCu1Rupje8YtGqsefD265TMg7usUDFdp6W11GMcet8"
    tests.append(childen)

    childen = testStruct()
    childen.err = skycoin.SKY_ErrInvalidPublicKeyVersion
    childen.base58 = b"xprv9uHRZZhk6KAJC1avXpDAp4MDc3sQKNxDiPvvkX8Br5ngLNv1TxvUxt4cV1rGL5hj6KCesnDYUhd7oWgT11eZG7XnxHrnYeSvkzY7d2bhkJ7"
    tests.append(childen)

    childen = testStruct()
    childen.err = skycoin.SKY_ErrInvalidFingerprint
    childen.base58 = b"xpub67tVq9SuNQCfm2PXBqjGRAtNZ935kx2uHJaURePth4JBpMfEy6jum7Euj7FTpbs7fnjhfZcNEktCucWHcJf74dbKLKNSTZCQozdDVwvkJhs"
    tests.append(childen)

    childen = testStruct()
    childen.err = skycoin.SKY_ErrInvalidChildNumber
    childen.base58 = b"xpub661MyMwTWkfYZq6BEh3ywGVXFvNj5hhzmWMhFBHSqmub31B1LZ9wbJ3DEYXZ8bHXGqnHKfepTud5a2XxGdnnePzZa2m2DyzTnFGBUXtaf9M"
    tests.append(childen)

    childen = testStruct()
    childen.err = skycoin.SKY_ErrInvalidPublicKey
    childen.base58 = b"xpub661MyMwAqRbcFtXgS5sYJABqqG9YLmC4Q1Rdap9gSE8NqtwybGhePY2gYymDsxxRe3WWeZQ7TadaLSdKUffezzczTCpB8j3JP96UwE2n6w1"
    tests.append(childen)

    childen = testStruct()
    childen.err = skycoin.SKY_ErrInvalidKeyVersion
    childen.base58 = b"8FH81Rao5EgGmdScoN66TJAHsQP7phEMeyMTku9NBJd7hXgaj3HTvSNjqJjoqBpxdbuushwPEM5otvxXt2p9dcw33AqNKzZEPMqGHmz7Dpayi6Vb"
    tests.append(childen)

    childen = testStruct()
    childen.err = skycoin.SKY_ErrInvalidKeyVersion
    childen.base58 = b"1111111111111adADjFaSNPxwXqLjHLj4mBfYxuewDPbw9hEj1uaXCzMxRPXDFF3cUoezTFYom4sEmEVSQmENPPR315cFk9YUFVek73wE9"
    tests.append(childen)

    childen = testStruct()
    childen.err = skycoin.SKY_ErrSerializedKeyWrongSize
    childen.base58 = b"7JJikZQ2NUXjSAnAF2SjFYE3KXbnnVxzRBNddFE1DjbDEHVGEJzYC7zqSgPoauBJS3cWmZwsER94oYSFrW9vZ4Ch5FtGeifdzmtS3FGYDB1vxFZsYKgMc"
    tests.append(childen)

    for test in tests:
        print(test.base58)
        err, b = skycoin.SKY_base58_Decode(test.base58)
        assert err == skycoin.SKY_OK

        err, _ = skycoin.SKY_bip32_DeserializePublicKey(b)
        assert err == test.err
