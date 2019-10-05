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
    print(len(vector.children))
    for tck in vector.children:
        print("## Depth ", tck.depth)
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
    vector2.children = []

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

    children = testChildKey()
    children.path = b"m/0/2147483647'/1"
    children.privKey = b"xprv9zFnWC6h2cLgpmSA46vutJzBcfJ8yaJGg8cX1e5StJh45BBciYTRXSd25UEPVuesF9yog62tGAQtHjXajPPdbRCHuWS6T8XA2ECKADdw4Ef"
    children.pubKey = b"xpub6DF8uhdarytz3FWdA8TvFSvvAh8dP3283MY7p2V4SeE2wyWmG5mg5EwVvmdMVCQcoNJxGoWaU9DCWh89LojfZ537wTfunKau47EL2dhHKon"
    children.fingerprint = b"78412e3a"
    children.identifier = b"78412e3a2296a40de124307b6485bd19833e2e34"
    children.chainCode = b"f366f48f1ea9f2d1d3fe958c95ca84ea18e4c4ddb9366c336c927eb246fb38cb"
    children.hexPubKey = b"03a7d1d856deb74c508e05031f9895dab54626251b3806e16b4bd12e781a7df5b9"
    children.wifPrivKey = b"KzyzXnznxSv249b4KuNkBwowaN3akiNeEHy5FWoPCJpStZbEKXN2"
    children.childNUmber = 1
    children.depth = 3
    vector2.children.append(children)

    children = testChildKey()
    children.path = b"m/0/2147483647'/1/2147483646'"
    children.privKey = b"xprvA1RpRA33e1JQ7ifknakTFpgNXPmW2YvmhqLQYMmrj4xJXXWYpDPS3xz7iAxn8L39njGVyuoseXzU6rcxFLJ8HFsTjSyQbLYnMpCqE2VbFWc"
    children.pubKey = b"xpub6ERApfZwUNrhLCkDtcHTcxd75RbzS1ed54G1LkBUHQVHQKqhMkhgbmJbZRkrgZw4koxb5JaHWkY4ALHY2grBGRjaDMzQLcgJvLJuZZvRcEL"
    children.fingerprint = b"31a507b8"
    children.identifier = b"31a507b815593dfc51ffc7245ae7e5aee304246e"
    children.chainCode = b"637807030d55d01f9a0cb3a7839515d796bd07706386a6eddf06cc29a65a0e29"
    children.hexPubKey = b"02d2b36900396c9282fa14628566582f206a5dd0bcc8d5e892611806cafb0301f0"
    children.wifPrivKey = b"L5KhaMvPYRW1ZoFmRjUtxxPypQ94m6BcDrPhqArhggdaTbbAFJEF"
    children.childNUmber = 2147483646 + FirstHardenedChild
    children.depth = 4
    vector2.children.append(children)

    children = testChildKey()
    children.path = b"m/0/2147483647'/1/2147483646'/2"
    children.privKey = b"xprvA2nrNbFZABcdryreWet9Ea4LvTJcGsqrMzxHx98MMrotbir7yrKCEXw7nadnHM8Dq38EGfSh6dqA9QWTyefMLEcBYJUuekgW4BYPJcr9E7j"
    children.pubKey = b"xpub6FnCn6nSzZAw5Tw7cgR9bi15UV96gLZhjDstkXXxvCLsUXBGXPdSnLFbdpq8p9HmGsApME5hQTZ3emM2rnY5agb9rXpVGyy3bdW6EEgAtqt"
    children.fingerprint = b"26132fdb"
    children.identifier = b"26132fdbe7bf89cbc64cf8dafa3f9f88b8666220"
    children.chainCode = b"9452b549be8cea3ecb7a84bec10dcfd94afe4d129ebfd3b3cb58eedf394ed271"
    children.hexPubKey = b"024d902e1a2fc7a8755ab5b694c575fce742c48d9ff192e63df5193e4c7afe1f9c"
    children.wifPrivKey = b"L3WAYNAZPxx1fr7KCz7GN9nD5qMBnNiqEJNJMU1z9MMaannAt4aK"
    children.childNUmber = 2
    children.depth = 5
    vector2.children.append(children)

    vector.append(vector2)

    vector3 = testMasterKey()
    vector3.seed = b"4b381541583be4423346c643850da4b320e46a87ae3d2a4e6da11eba819cd4acba45d239319ac14f863b8d5ab5a0d0c64d2e8a1e7d1457df2e5a3c51c73235be"
    vector3.privKey = b"xprv9s21ZrQH143K25QhxbucbDDuQ4naNntJRi4KUfWT7xo4EKsHt2QJDu7KXp1A3u7Bi1j8ph3EGsZ9Xvz9dGuVrtHHs7pXeTzjuxBrCmmhgC6"
    vector3.pubKey = b"xpub661MyMwAqRbcEZVB4dScxMAdx6d4nFc9nvyvH3v4gJL378CSRZiYmhRoP7mBy6gSPSCYk6SzXPTf3ND1cZAceL7SfJ1Z3GC8vBgp2epUt13"
    vector3.fingerprint = b"41d63b50"
    vector3.identifier = b"41d63b50d8dd5e730cdf4c79a56fc929a757c548"
    vector3.chainCode = b"01d28a3e53cffa419ec122c968b3259e16b65076495494d97cae10bbfec3c36f"
    vector3.hexPubKey = b"03683af1ba5743bdfc798cf814efeeab2735ec52d95eced528e692b8e34c4e5669"
    vector3.wifPrivKey = b"KwFPqAq9SKx1sPg15Qk56mqkHwrfGPuywtLUxoWPkiTSBoxCs8am"
    vector3.children = []

    children = testChildKey()
    children.path = b"m/0'"
    children.privKey = b"xprv9uPDJpEQgRQfDcW7BkF7eTya6RPxXeJCqCJGHuCJ4GiRVLzkTXBAJMu2qaMWPrS7AANYqdq6vcBcBUdJCVVFceUvJFjaPdGZ2y9WACViL4L"
    children.pubKey = b"xpub68NZiKmJWnxxS6aaHmn81bvJeTESw724CRDs6HbuccFQN9Ku14VQrADWgqbhhTHBaohPX4CjNLf9fq9MYo6oDaPPLPxSb7gwQN3ih19Zm4Y"
    children.fingerprint = b"c61368bb"
    children.identifier = b"c61368bb50e066acd95bd04a0b23d3837fb75698"
    children.chainCode = b"e5fea12a97b927fc9dc3d2cb0d1ea1cf50aa5a1fdc1f933e8906bb38df3377bd"
    children.hexPubKey = b"027c3591221e28939e45f8ea297d62c3640ebb09d7058b01d09c963d984a40ad49"
    children.wifPrivKey = b"L3z3MSqZtDQ1FPHKi7oWf1nc9rMEGFtZUDCoFa7n4F695g5qZiSu"
    children.childNUmber = FirstHardenedChild
    children.depth = 1
    vector3.children.append(children)

    vector.append(vector3)

    # Test case copied from:
    # https://github.com/bitcoinjs/bip32/blob/master/test/fixtures/index.json

    vector4 = testMasterKey()
    vector4.seed = b"d13de7bd1e54422d1a3b3b699a27fb460de2849e7e66a005c647e8e4a54075cb"
    vector4.privKey = b"xprv9s21ZrQH143K3zWpEJm5QtHFh93eNJrNbNqzqLN5XoE9MvC7gs5TmBFaL2PpaXpDc8FBYVe5EChc73ApjSQ5fWsXS7auHy1MmG6hdpywE1q"
    vector4.pubKey = b"xpub661MyMwAqRbcGUbHLLJ5n2DzFAt8mmaDxbmbdimh68m8EiXGEQPiJya4BJat5yMzy4e68VSUoLGCu5uvzf8dUoGvwuJsLE6F1cibmWsxFNn"
    vector4.fingerprint = b"1a87677b"
    vector4.identifier = b"1a87677be6f73cc9655e8b4c5d2fd0aeeb1b23c7"
    vector4.chainCode = b"c23ab32b36ddff49fae350a1bed8ec6b4d9fc252238dd789b7273ba4416054eb"
    vector4.hexPubKey = b"0298ccc720d5dea817c7077605263bae52bca083cf8888fee77ff4c1b4797ee180"
    vector4.wifPrivKey = b"KwDiCU5bs8xQwsRgxjhkcJcVuR7NE4Mei8X9uSAVviVTE7JmMoS6"
    vector4.children = []

    children = testChildKey()
    children.path = b"m/44'/0'/0'/0/0'"
    children.privKey = b"xprvA3cqPFaMpr7n1wRh6BPtYfwdYRoKCaPzgDdQnUmgMrz1WxWNEW3EmbBr9ieh9BJAsRGKFPLvotb4p4Aq79jddUVKPVJt7exVzLHcv777JVf"
    children.pubKey = b"xpub6GcBnm7FfDg5ERWACCvtuotN6Tdoc37r3SZ1asBHvCWzPkqWn3MVKPWKzy6GsfmdMUGanR3D12dH1cp5tJauuubwc4FAJDn67SH2uUjwAT1"
    children.fingerprint = b"e371d69b"
    children.identifier = b"e371d69b5dae6eacee832a130ee9f55545275a09"
    children.chainCode = b"ca27553aa89617e982e621637d6478f564b32738f8bbe2e48d0a58a8e0f6da40"
    children.hexPubKey = b"027c3591221e28939e45f8ea297d62c3640ebb09d7058b01d09c963d984a40ad49"
    children.wifPrivKey = b"L3z3MSqZtDQ1FPHKi7oWf1nc9rMEGFtZUDCoFa7n4F695g5qZiSu"
    children.childNUmber = FirstHardenedChild
    children.depth = 5
    vector4.children.append(children)

    vector.append(vector4)

    # Test running
    i = 1
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


def test_TestCantCreateHardenedPublicChild():
    err, b = skycoin.SKY_cipher_RandByte(32)
    assert err == skycoin.SKY_OK
    err, key = skycoin.SKY_bip32_NewMasterKey(b)
    assert err == skycoin.SKY_OK

    # Test that it works for private keys
    err, _ = skycoin.SKY_bip32_PrivateKey_NewPrivateChildKey(key,
                                                             FirstHardenedChild - 1)
    assert err == skycoin.SKY_OK
    err, _ = skycoin.SKY_bip32_PrivateKey_NewPrivateChildKey(
        key, FirstHardenedChild)
    assert err == skycoin.SKY_OK
    err, _ = skycoin.SKY_bip32_PrivateKey_NewPrivateChildKey(
        key, FirstHardenedChild + 1)
    assert err == skycoin.SKY_OK

    # Test that it throws an error for public keys if hardened
    err, pubkey = skycoin.SKY_bip32_PrivateKey_Publickey(key)
    assert err == skycoin.SKY_OK

    err, _ = skycoin.SKY_bip32_PublicKey_NewPublicChildKey(
        pubkey, FirstHardenedChild - 1)
    assert err == skycoin.SKY_OK
    err, _ = skycoin.SKY_bip32_PublicKey_NewPublicChildKey(
        pubkey, FirstHardenedChild)
    assert err == skycoin.SKY_ErrHardenedChildPublicKey
    err, _ = skycoin.SKY_bip32_PublicKey_NewPublicChildKey(
        pubkey, FirstHardenedChild + 1)
    assert err == skycoin.SKY_ErrHardenedChildPublicKey


class case():
    seed = b""
    path = b""
    key = b""
    err = skycoin.SKY_OK


def test_TestNewPrivateKeyFromPath():
    cases = []
    childen = case()
    childen.seed = b"6162636465666768696A6B6C6D6E6F707172737475767778797A"
    childen.path = b"m"
    childen.key = b"xprv9s21ZrQH143K3GfuLFf1UxUB4GzmFav1hrzTG1bPorBTejryu4YfYVxZn6LNmwfvsi6uj1Wyv9vLDPsfKDuuqwEqYier1ZsbgWVd9NCieNv"
    cases.append(childen)

    childen = case()
    childen.seed = b"6162636465666768696A6B6C6D6E6F707172737475767778797A"
    childen.path = b"m/1'"
    childen.key = b"xprv9uWf8oyvCHcAUg3kSjSroz67s7M3qJRWmNcdVwYGf91GFsaAatsVVp1bjH7z3WiWevqB7WK92B415oBwcahjoMvvb4mopPyqZUDeVW4168c"
    cases.append(childen)

    childen = case()
    childen.path = b"6162636465666768696A6B6C6D6E6F707172737475767778797A"
    childen.path = b"m/1'/foo"
    childen.err = skycoin.SKY_ErrPathNodeNotNumber
    cases.append(childen)

    childen = case()
    childen.seed = b"6162"
    childen.path = b"m/1'"
    childen.err = skycoin.SKY_ErrInvalidSeedLength
    cases.append(childen)

    for tc in cases:
        print(tc.path)
        err, seed = skycoin.SKY_base58_String2Hex(tc.seed)
        assert err == skycoin.SKY_OK

        err, k = skycoin.SKY_bip32_NewPrivateKeyFromPath(seed, tc.path)
        if tc.err != skycoin.SKY_OK:
            assert tc.err == err
            return

        assert err == skycoin.SKY_OK
        err, kStr = skycoin.SKY_bip32_PrivateKey_String(k)
        assert err == skycoin.SKY_OK
        assert tc.key == kStr


def test_TestMaxChildDepthError():
    err, b = skycoin.SKY_cipher_RandByte(32)
    assert err == skycoin.SKY_OK
    err, key = skycoin.SKY_bip32_NewMasterKey(b)
    assert err == skycoin.SKY_OK

    reached = False
    for i in range(256):
        err, key = skycoin.SKY_bip32_PrivateKey_NewPrivateChildKey(key, 0)
        if i == 255:
            assert err == skycoin.SKY_ErrMaxDepthReached
            reached = True
        if i != 255:
            assert err == skycoin.SKY_OK
    assert reached == True


def test_TestParentPublicChildDerivation():
    # Generated using https://iancoleman.github.io/bip39/
        # Root key:
        # xprv9s21ZrQH143K2Cfj4mDZBcEecBmJmawReGwwoAou2zZzG45bM6cFPJSvobVTCB55L6Ld2y8RzC61CpvadeAnhws3CHsMFhNjozBKGNgucYm
        # Derivation Path m/44'/60'/0'/0:
        # xprv9zy5o7z1GMmYdaeQdmabWFhUf52Ytbpe3G5hduA4SghboqWe7aDGWseN8BJy1GU72wPjkCbBE1hvbXYqpCecAYdaivxjNnBoSNxwYD4wHpW
        # xpub6DxSCdWu6jKqr4isjo7bsPeDD6s3J4YVQV1JSHZg12Eagdqnf7XX4fxqyW2sLhUoFWutL7tAELU2LiGZrEXtjVbvYptvTX5Eoa4Mamdjm9u

    err, extendedMasterPublicBytes = skycoin.SKY_base58_Decode(
        b"xpub6DxSCdWu6jKqr4isjo7bsPeDD6s3J4YVQV1JSHZg12Eagdqnf7XX4fxqyW2sLhUoFWutL7tAELU2LiGZrEXtjVbvYptvTX5Eoa4Mamdjm9u")
    assert err == skycoin.SKY_OK

    err, extendedMasterPublic = skycoin.SKY_bip32_DeserializePublicKey(
        extendedMasterPublicBytes)
    assert err == skycoin.SKY_OK

    err, extendedMasterPrivateBytes = skycoin.SKY_base58_Decode(
        b"xprv9zy5o7z1GMmYdaeQdmabWFhUf52Ytbpe3G5hduA4SghboqWe7aDGWseN8BJy1GU72wPjkCbBE1hvbXYqpCecAYdaivxjNnBoSNxwYD4wHpW")
    assert err == skycoin.SKY_OK

    err, extendedMasterPrivate = skycoin.SKY_bip32_DeserializePrivateKey(
        extendedMasterPrivateBytes)
    assert err == skycoin.SKY_OK

    expectedChildren = []

    childen = testChildKey()
    childen.path = b"m/0"
    childen.hexPubKey = b"0243187e1a2ba9ba824f5f81090650c8f4faa82b7baf93060d10b81f4b705afd46"
    childen.wifPrivKey = b"KyNPkzzaQ9xa7d2iFacTBgjP4rM3SydTzUZW7uwDh6raePWRJkeM"
    expectedChildren.append(childen)

    childen = testChildKey()
    childen.path = b"m/1"
    childen.hexPubKey = b"023790d11eb715c4320d8e31fba3a09b700051dc2cdbcce03f44b11c274d1e220b"
    childen.wifPrivKey = b"KwVyk5XXaamsPPiGLHciv6AjhUV88CM7xTto7sRMCEy12GfwZzZQ"
    expectedChildren.append(childen)

    childen = testChildKey()
    childen.path = b"m/2"
    childen.hexPubKey = b"0302c5749c3c75cea234878ae3f4d8f65b75d584bcd7ed0943b016d6f6b59a2bad"
    childen.wifPrivKey = b"L1o7CpgTjkcBYmbeuNigVpypgJ9GKq87WNqz8QDjWMqdKVKFf826"
    expectedChildren.append(childen)

    childen = testChildKey()
    childen.path = b"m/3"
    childen.hexPubKey = b"03f0440c94e5b14ea5b15875934597afff541bec287c6e65dc1102cafc07f69699"
    childen.wifPrivKey = b"KzmYqf8WSUNzf2LhAWJjxv7pYX34XhFeLLxSoaSD8y9weJ4j6Z7q"
    expectedChildren.append(childen)

    childen = testChildKey()
    childen.path = b"m/4"
    childen.hexPubKey = b"026419d0d8996707605508ac44c5871edc7fe206a79ef615b74f2eea09c5852e2b"
    childen.wifPrivKey = b"KzezMKd7Yc4jwJd6ASji2DwXX8jB8XwNTggLoAJU78zPAfXhzRLD"
    expectedChildren.append(childen)

    childen = testChildKey()
    childen.path = b"m/5"
    childen.hexPubKey = b"02f63c6f195eea98bdb163c4a094260dea71d264b21234bed4df3899236e6c2298"
    childen.wifPrivKey = b"Kwxik5cHiQCZYy5g9gdfQmr7c3ivLDhFjpSF7McHKHeox6iu6MjL"
    expectedChildren.append(childen)

    childen = testChildKey()
    childen.path = b"m/6"
    childen.hexPubKey = b"02d74709cd522081064858f393d009ead5a0ecd43ede3a1f57befcc942025cb5f9"
    childen.wifPrivKey = b"KwGhZYHovZoczyfupFRgZcr2xz1nHTSKx79uZuWhuzDSU7L7LrxE"
    expectedChildren.append(childen)

    childen = testChildKey()
    childen.path = b"m/7"
    childen.hexPubKey = b"03e54bb92630c943d38bbd8a4a2e65fca7605e672d30a0e545a7198cbb60729ceb"
    childen.wifPrivKey = b"L4iGJ3JCfnMU1ia2bMQeF88hs6tkkS9QrmLbWPsj1ULHrUJid4KT"
    expectedChildren.append(childen)

    childen = testChildKey()
    childen.path = b"m/8"
    childen.hexPubKey = b"027e9d5acd14d39c4938697fba388cd2e8f31fc1c5dc02fafb93a10a280de85199"
    childen.wifPrivKey = b"L3xfynMTDMR8vs6G5VxxjoKLBQyihvtcBHF4KHY5wvFMwevLjZKU"
    expectedChildren.append(childen)

    childen = testChildKey()
    childen.path = b"m/9"
    childen.hexPubKey = b"02a167a9f0d57468fb6abf2f3f7967e2cadf574314753a06a9ef29bc76c54638d2"
    childen.wifPrivKey = b"KxiUV7CcdCuF3bLajqaP6qMFERQFvzsRj9aeCCf3TNWXioLwwJAm"
    expectedChildren.append(childen)

    childen = testChildKey()
    childen.path = b"m/100"
    childen.hexPubKey = b"020db9ba00ddf68428e3f5bfe54252bbcd75b21e42f51bf3bfc4172bf0e5fa7905"
    childen.wifPrivKey = b"L5ipKgExgKZYaxsQPEmyjrhoSepoxuSAxSWgK1GX5kaTUN3zGCU7"
    expectedChildren.append(childen)

    childen = testChildKey()
    childen.path = b"m/101"
    childen.hexPubKey = b"0299e3790956570737d6164e6fcda5a3daa304065ca95ba46bc73d436b84f34d46"
    childen.wifPrivKey = b"L1iUjHWpYSead5vYZycMdMzCZDFQzveG3S6NviAi5BvvGdnuQbi6"
    expectedChildren.append(childen)

    childen = testChildKey()
    childen.path = b"m/102"
    childen.hexPubKey = b"0202e0732c4c5d2b1036af173640e01957998cfd4f9cdaefab6ffe76eb869e2c59"
    childen.wifPrivKey = b"KybjnK4e985dgzxL5pgXTfq8YFagG8gB9HWAjLimagR4pdodCSNo"
    expectedChildren.append(childen)

    childen = testChildKey()
    childen.path = b"m/103"
    childen.hexPubKey = b"03d050adbd996c0c5d737ff638402dfbb8c08e451fef10e6d62fb57887c1ac6cb2"
    childen.wifPrivKey = b"Kx9bf5cyf29fp7uuMVnqn47692xRwXStVmnL75w9i1sLQDjbFHP5"
    expectedChildren.append(childen)

    childen = testChildKey()
    childen.path = b"m/104"
    childen.hexPubKey = b"038d466399e2d68b4b16043ad4d88893b3b2f84fc443368729a973df1e66f4f530"
    childen.wifPrivKey = b"L5myg7MNjKHcgVMS9ytmHgBftiWAi1awGpeC6p9dygsEQV9ZRvpz"
    expectedChildren.append(childen)

    childen = testChildKey()
    childen.path = b"m/105"
    childen.hexPubKey = b"034811e2f0c8c50440c08c2c9799b99c911c036e877e8325386ff61723ae3ffdce"
    childen.wifPrivKey = b"L1KHrLBPhaJnvysjKUYk5QwkyWDb6uHgDM8EmE4eKtfqyJ13a7HC"
    expectedChildren.append(childen)

    childen = testChildKey()
    childen.path = b"m/106"
    childen.hexPubKey = b"026339fd5842921888e711a6ba9104a5f0c94cc0569855273cf5faefdfbcd3cc29"
    childen.wifPrivKey = b"Kz4WPV43po7LRkatwHf9YGknGZRYfvo7TkvojinzxoFRXRYXyfDn"
    expectedChildren.append(childen)

    childen = testChildKey()
    childen.path = b"m/107"
    childen.hexPubKey = b"02833705c1069fab2aa92c6b0dac27807290d72e9f52378d493ac44849ca003b22"
    childen.wifPrivKey = b"L3PxeN4w336kTk1becdFsAnR8ihh8SeMYXRHEzSmRNQTjtmcUjr9"
    expectedChildren.append(childen)

    childen = testChildKey()
    childen.path = b"m/108"
    childen.hexPubKey = b"032d2639bde1eb7bdf8444bd4f6cc26a9d1bdecd8ea15fac3b992c3da68d9d1df5"
    childen.wifPrivKey = b"L2wf8FYiA888qrhDzHkFkZ3ZRBntysjtJa1QfcxE1eFiyDUZBRSi"
    expectedChildren.append(childen)

    childen = testChildKey()
    childen.path = b"m/109"
    childen.hexPubKey = b"02479c6d4a64b93a2f4343aa862c938fbc658c99219dd7bebb4830307cbd76c9e9"
    childen.wifPrivKey = b"L5A5hcupWnYTNJTLTWDDfWyb3hnrJgdDgyN7c4PuF17bsY1tNjxS"
    expectedChildren.append(childen)

    childen = testChildKey()
    childen

    for child in expectedChildren:
        print(child.path)
        err, path = skycoin.SKY_bip32_ParsePath(child.path)
        assert err == skycoin.SKY_OK
        assert skycoin.SKY_bip32_Path_Count(path)[1] == 2
        element_tmp = skycoin.bip32__PathNode()
        err = skycoin.SKY_bip32_Path_GetElements(path, 1, element_tmp)
        assert err == skycoin.SKY_OK
        err, pubkey = skycoin.SKY_bip32_PublicKey_NewPublicChildKey(
            extendedMasterPublic, element_tmp.ChildNumber)
        assert err == skycoin.SKY_OK
        err, pubkey_key = skycoin.SKY_bip32_PublicKey_GetKey(pubkey)
        assert err == skycoin.SKY_OK
        err, pubkey_hexpubkey = skycoin.SKY_base58_Hex2String(pubkey_key)
        assert err == skycoin.SKY_OK
        assert child.hexPubKey == pubkey_hexpubkey

        err, pubkey2 = skycoin.SKY_bip32_PrivateKey_NewPublicChildKey(
            extendedMasterPrivate, element_tmp.ChildNumber)
        assert err == skycoin.SKY_OK
        assert utils.isPublicKeyEq(pubkey, pubkey2) == 1

        err, privkey = skycoin.SKY_bip32_PrivateKey_NewPrivateChildKey(
            extendedMasterPrivate, element_tmp.ChildNumber)
        assert err == skycoin.SKY_OK
        expectedPrivKey = skycoin.cipher_SecKey()
        err = skycoin.SKY_cipher_SecKeyFromBitcoinWalletImportFormat(
            child.wifPrivKey, expectedPrivKey)
        assert err == skycoin.SKY_OK

        err, pubkey3 = skycoin.SKY_bip32_PrivateKey_Publickey(privkey)
        assert err == skycoin.SKY_OK
        assert utils.isPublicKeyEq(pubkey, pubkey3) == 1
