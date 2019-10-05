import skycoin
import tests.utils as utils


def test_TestBitcoinAddressFromBytes():
    p, s = utils.makecipher_PubKeyAndcipher_SecKey()
    a = skycoin.cipher__BitcoinAddress()
    err = skycoin.SKY_cipher_BitcoinAddressFromSecKey(s, a)
    assert err == skycoin.SKY_OK
    # Valid pubkey+address
    err = skycoin.SKY_cipher_BitcoinAddress_Verify(a, p)
    assert err == skycoin.SKY_OK
    s = skycoin.cipher_SecKey()
    err = skycoin.SKY_cipher_BitcoinAddressFromSecKey(s, a)
    assert err == skycoin.SKY_ErrPubKeyFromNullSecKey


def test_TestBitcoinWIPRoundTrio():
    public_key = skycoin.cipher_PubKey()
    secret_key_1 = skycoin.cipher_SecKey()
    secret_key_2 = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key_1)
    wip_1 = skycoin.SKY_cipher_BitcoinWalletImportFormatFromSeckey(
        secret_key_1)
    err = skycoin.SKY_cipher_SecKeyFromBitcoinWalletImportFormat(
        wip_1, secret_key_2)
    assert err == skycoin.SKY_OK
    wip_2 = skycoin.SKY_cipher_BitcoinWalletImportFormatFromSeckey(
        secret_key_2)
    _, secret_key_1_hex = skycoin.SKY_cipher_SecKey_Hex(secret_key_1)
    _, secret_key_2_hex = skycoin.SKY_cipher_SecKey_Hex(secret_key_2)
    assert secret_key_1_hex == secret_key_2_hex
    assert wip_1 == wip_2


def test_TestBitcoinWIF():
    wips = [
        b"KwntMbt59tTsj8xqpqYqRRWufyjGunvhSyeMo3NTYpFYzZbXJ5Hp",
        b"L4ezQvyC6QoBhxB4GVs9fAPhUKtbaXYUn8YTqoeXwbevQq4U92vN",
        b"KydbzBtk6uc7M6dXwEgTEH2sphZxSPbmDSz6kUUHi4eUpSQuhEbq"
    ]

    publics = [
        b"034f355bdcb7cc0af728ef3cceb9615d90684bb5b2ca5f859ab0f0b704075871aa",
        b"02ed83704c95d829046f1ac27806211132102c34e9ac7ffa1b71110658e5b9d1bd",
        b"032596957532fc37e40486b910802ff45eeaa924548c0e1c080ef804e523ec3ed3"
    ]

    address = [
        b"1Q1pE5vPGEEMqRcVRMbtBK842Y6Pzo6nK9",
        b"1NKRhS7iYUGTaAfaR5z8BueAJesqaTyc4a",
        b"19ck9VKC6KjGxR9LJg4DNMRc45qFrJguvV"
    ]

    for p in range(len(wips)):
        secret_key = skycoin.cipher_SecKey()
        public_key = skycoin.cipher_PubKey()
        err = skycoin.skycoin.SKY_cipher_SecKeyFromBitcoinWalletImportFormat(
            wips[p], secret_key)
        assert err == skycoin.SKY_OK
        skycoin.SKY_cipher_PubKeyFromSecKey(secret_key, public_key)
        _, public_key_hex = skycoin.SKY_cipher_PubKey_Hex(public_key)
        assert public_key_hex == publics[p]
        bitcoin_addr = skycoin.cipher__BitcoinAddress()
        skycoin.SKY_cipher_BitcoinAddressFromPubKey(public_key, bitcoin_addr)
        bitcoin_addr_str = skycoin.skycoin.SKY_cipher_BitcoinAddress_String(
            bitcoin_addr)
        assert bitcoin_addr_str == address[p]


def test_TestDecodeBase58BitcoinAddress():
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    address = skycoin.cipher__BitcoinAddress()
    skycoin.SKY_cipher_BitcoinAddressFromPubKey(public_key, address)
    err = skycoin.SKY_cipher_BitcoinAddress_Verify(address, public_key)
    assert err == skycoin.SKY_OK
    address_2 = skycoin.cipher__BitcoinAddress()
    err = skycoin.SKY_cipher_DecodeBase58BitcoinAddress(b'""', address_2)
    assert err == skycoin.SKY_ERROR
    err = skycoin.SKY_cipher_DecodeBase58BitcoinAddress(b'"cascs"', address_2)
    assert err == skycoin.SKY_ERROR
    byte = skycoin.SKY_cipher_BitcoinAddress_Bytes(address)
    _, h = skycoin.SKY_base58_Hex2Base58(byte[:int(len(byte) / 2)])
    err = skycoin.SKY_cipher_DecodeBase58BitcoinAddress(h, address_2)
    assert err == skycoin.SKY_ErrAddressInvalidLength
    _, h = skycoin.SKY_base58_Hex2Base58(byte)
    err = skycoin.SKY_cipher_DecodeBase58BitcoinAddress(h, address_2)
    assert err == skycoin.SKY_OK
    assert address == address_2
    addres_str = skycoin.SKY_cipher_BitcoinAddress_String(address)
    err = skycoin.SKY_cipher_DecodeBase58BitcoinAddress(addres_str, address_2)
    assert err == skycoin.SKY_OK
    assert address == address_2
    #  preceding whitespace is invalid
    addres_2_str = b'" " + a_str'
    err = skycoin.SKY_cipher_DecodeBase58BitcoinAddress(
        addres_2_str, address_2)
    assert err == skycoin.SKY_ERROR
    #  preceding zeroes are invalid
    addres_2_str = b'"000" + a_str'
    err = skycoin.SKY_cipher_DecodeBase58BitcoinAddress(
        addres_2_str, address_2)
    assert err == skycoin.SKY_ERROR
    #  trailing whitespace is invalid
    addres_2_str = b'a_str + " "'
    err = skycoin.SKY_cipher_DecodeBase58BitcoinAddress(
        addres_2_str, address_2)
    assert err == skycoin.SKY_ERROR
    # trailing zeroes are invalid
    addres_2_str = b'a_str + "000"'
    err = skycoin.SKY_cipher_DecodeBase58BitcoinAddress(
        addres_2_str, address_2)
    assert err == skycoin.SKY_ERROR


def test_TestBitcoinAddressNull():
    a = skycoin.cipher__BitcoinAddress()
    err = skycoin.SKY_cipher_BitcoinAddress_Null(a)
    assert err == 1
    p = skycoin.cipher_PubKey()
    s = skycoin.cipher_SecKey()
    err = skycoin.SKY_cipher_GenerateKeyPair(p, s)
    assert err == skycoin.SKY_OK
    skycoin.SKY_cipher_BitcoinAddressFromPubKey(p, a)
    err = skycoin.SKY_cipher_BitcoinAddress_Null(a)
    assert err == 0


def test_TestBitcoinAddressVerify():
    p = skycoin.cipher_PubKey()
    s = skycoin.cipher_SecKey()
    err = skycoin.SKY_cipher_GenerateKeyPair(p, s)
    assert err == skycoin.SKY_OK
    a = skycoin.cipher__BitcoinAddress()
    skycoin.SKY_cipher_BitcoinAddressFromPubKey(p, a)
    # Valid pubkey+address
    err = skycoin.SKY_cipher_BitcoinAddress_Verify(a, p)
    assert err == skycoin.SKY_OK
    # Invalid pubkey
    p = skycoin.cipher_PubKey()
    err = skycoin.SKY_cipher_BitcoinAddress_Verify(a, p)
    assert err == skycoin.SKY_ErrAddressInvalidPubKey
    p2 = skycoin.cipher_PubKey()
    err = skycoin.SKY_cipher_GenerateKeyPair(p2, s)
    err = skycoin.SKY_cipher_BitcoinAddress_Verify(a, p2)
    assert err == skycoin.SKY_ErrAddressInvalidPubKey
    # Bad version
    a.Version = 0x01
    err = skycoin.SKY_cipher_BitcoinAddress_Verify(a, p2)
    assert err == skycoin.SKY_ErrAddressInvalidVersion


def test_TestBitcoinWIFRoundTrip():
    p, s = utils.makecipher_PubKeyAndcipher_SecKey()
    wip1 = skycoin.SKY_cipher_BitcoinWalletImportFormatFromSeckey(s)
    s2 = skycoin.cipher_SecKey()
    err = skycoin.SKY_cipher_SecKeyFromBitcoinWalletImportFormat(wip1, s2)
    assert err == skycoin.SKY_OK
    wip2 = skycoin.SKY_cipher_BitcoinWalletImportFormatFromSeckey(s2)
    assert s == s2
    sh = skycoin.SKY_cipher_SecKey_Hex(s)
    sh2 = skycoin.SKY_cipher_SecKey_Hex(s2)
    assert sh == sh2
    assert wip1 == wip2
