import skycoin
def test_TestBitcoinAddressFromBytes():
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    address = skycoin.cipher__BitcoinAddress()
    skycoin.SKY_cipher_BitcoinAddressFromPubKey(public_key, address)
    address_2 = skycoin.cipher__BitcoinAddress()
    byte = skycoin.skycoin.SKY_cipher_BitcoinAddress_Bytes(address)
    err = skycoin.skycoin.SKY_cipher_BitcoinAddressFromBytes(byte, address_2)
    assert err == skycoin.SKY_OK
    assert address_2 == address
    ## Invalid number of bytes
    __ = skycoin.cipher__BitcoinAddress()
    err = skycoin.skycoin.SKY_cipher_BitcoinAddressFromBytes(byte[:len(byte) - 2], __)
    assert err == skycoin.SKY_ErrAddressInvalidLength
    ## Invalid checksum
    byte_array = bytearray(byte)
    byte_array[-1] = 1
    byte_new = bytes(byte_array)
    err = skycoin.skycoin.SKY_cipher_BitcoinAddressFromBytes(byte_new, __)
    assert err == skycoin.SKY_ErrAddressInvalidChecksum
    ## Invalid Version
    address.Version = 2
    byte = skycoin.skycoin.SKY_cipher_BitcoinAddress_Bytes(address)
    err = skycoin.skycoin.SKY_cipher_BitcoinAddressFromBytes(byte, __)
    assert err == skycoin.SKY_ErrAddressInvalidVersion

def test_TestBitcoinWIPRoundTrio():
    public_key = skycoin.cipher_PubKey()
    secret_key_1 = skycoin.cipher_SecKey()
    secret_key_2 = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key_1)
    wip_1 = skycoin.skycoin.SKY_cipher_BitcoinWalletImportFormatFromSeckey(secret_key_1)
    err = skycoin.skycoin.SKY_cipher_SecKeyFromBitcoinWalletImportFormat(wip_1, secret_key_2)
    assert err == skycoin.SKY_OK
    wip_2 = skycoin.skycoin.SKY_cipher_BitcoinWalletImportFormatFromSeckey(secret_key_2)
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
        err = skycoin.skycoin.SKY_cipher_SecKeyFromBitcoinWalletImportFormat(wips[p], secret_key)
        assert err == skycoin.SKY_OK
        skycoin.SKY_cipher_PubKeyFromSecKey(secret_key, public_key)
        _, public_key_hex = skycoin.SKY_cipher_PubKey_Hex(public_key)
        assert public_key_hex == publics[p]
        bitcoin_addr = skycoin.cipher__BitcoinAddress()
        skycoin.SKY_cipher_BitcoinAddressFromPubKey(public_key, bitcoin_addr)
        bitcoin_addr_str = skycoin.skycoin.SKY_cipher_BitcoinAddress_String(bitcoin_addr)
        assert bitcoin_addr_str == address[p]


