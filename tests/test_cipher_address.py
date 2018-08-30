import skycoin

def test_TestDecodeBase58Address():
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    address = skycoin.cipher__Address()
    skycoin.SKY_cipher_AddressFromPubKey(public_key, address)
    err = skycoin.SKY_cipher_Address_Verify(address, public_key) 
    assert err == skycoin.SKY_OK
    address_2 = skycoin.cipher__Address()
    err = skycoin.SKY_cipher_DecodeBase58Address(b'""', address_2) 
    assert err == skycoin.SKY_ErrInvalidBase58Char
    err = skycoin.SKY_cipher_DecodeBase58Address(b'"cascs"', address_2) 
    assert err == skycoin.SKY_ErrInvalidBase58Char
    _, byte = skycoin.SKY_cipher_Address_Bytes(address)
    _, h = skycoin.SKY_base58_Hex2Base58(byte[:int(len(byte) / 2)])
    err = skycoin.SKY_cipher_DecodeBase58Address(h, address_2) 
    assert err == skycoin.SKY_ErrAddressInvalidLength
    _, h = skycoin.SKY_base58_Hex2Base58(byte)
    err = skycoin.SKY_cipher_DecodeBase58Address(h, address_2) 
    assert err == skycoin.SKY_OK
    assert address == address_2
    _, addres_str = skycoin.SKY_cipher_Address_String(address)
    err = skycoin.SKY_cipher_DecodeBase58Address(addres_str, address_2)
    assert err == skycoin.SKY_OK
    assert address == address_2
    #  preceding whitespace is invalid
    addres_2_str = b'" " + a_str'
    err = skycoin.SKY_cipher_DecodeBase58Address(addres_2_str, address_2)
    assert err == skycoin.SKY_ErrInvalidBase58Char
    #  preceding zeroes are invalid
    addres_2_str = b'"000" + a_str'
    err = skycoin.SKY_cipher_DecodeBase58Address(addres_2_str, address_2)
    assert err == skycoin.SKY_ErrInvalidBase58Char
    #  trailing whitespace is invalid
    addres_2_str = b'a_str + " "'
    err = skycoin.SKY_cipher_DecodeBase58Address(addres_2_str, address_2)
    assert err == skycoin.SKY_ErrInvalidBase58Char
    # trailing zeroes are invalid
    addres_2_str = b'a_str + "000"'
    err = skycoin.SKY_cipher_DecodeBase58Address(addres_2_str, address_2)
    assert err == skycoin.SKY_ErrInvalidBase58Char


def test_TestAddressFromBytes():
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    address = skycoin.cipher__Address()
    skycoin.SKY_cipher_AddressFromPubKey(public_key, address)
    address_2 = skycoin.cipher__Address()
    _, byte = skycoin.SKY_cipher_Address_Bytes(address)
    err = skycoin.SKY_cipher_AddressFromBytes(byte, address_2) 
    assert err == skycoin.SKY_OK
    assert address == address_2
    # Invalid number of bytes
    __ = skycoin.cipher__Address()
    err = skycoin.SKY_cipher_AddressFromBytes(byte[:len(byte) - 2], __)
    assert err == skycoin.SKY_ErrAddressInvalidLength
    # Invalid checksum
    byte_array = bytearray(byte)
    byte_array[-1] = 1
    byte_new = bytes(byte_array)
    err = skycoin.SKY_cipher_AddressFromBytes(byte_new, __)
    assert err == skycoin.SKY_ErrAddressInvalidChecksum
    address.Version = 2
    _, b = skycoin.SKY_cipher_Address_Bytes(address)
    err = skycoin.SKY_cipher_AddressFromBytes(b, __) 
    assert err == skycoin.SKY_ErrAddressInvalidVersion


def test_TestBitcoinAddressFromBytes():
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    address = skycoin.cipher__Address()
    skycoin.SKY_cipher_AddressFromPubKey(public_key, address)
    address_2 = skycoin.cipher__Address()
    _, byte = skycoin.SKY_cipher_Address_BitcoinBytes(address)
    err = skycoin.SKY_cipher_BitcoinAddressFromBytes(byte, address_2) 
    assert err == skycoin.SKY_OK
    assert address_2 == address
    # Invalid number of bytes
    __ = skycoin.cipher__Address()
    err = skycoin.SKY_cipher_BitcoinAddressFromBytes(byte[:len(byte) - 2], __)
    assert err == skycoin.SKY_ErrAddressInvalidLength
    # Invalid checksum
    byte_array = bytearray(byte)
    byte_array[-1] = 1
    byte_new = bytes(byte_array)
    err = skycoin.SKY_cipher_BitcoinAddressFromBytes(byte_new, __)
    assert err == skycoin.SKY_ErrAddressInvalidChecksum
    # Invalid Version
    address.Version = 2
    _, byte = skycoin.SKY_cipher_Address_BitcoinBytes(address)
    err = skycoin.SKY_cipher_BitcoinAddressFromBytes(byte, __)
    assert err == skycoin.SKY_ErrAddressInvalidVersion


def test_TestAddressRoundtrip():
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    address = skycoin.cipher__Address()
    address_2 = skycoin.cipher__Address()
    skycoin.SKY_cipher_AddressFromPubKey(public_key, address)
    _, byte = skycoin.SKY_cipher_Address_BitcoinBytes(address)
    err = skycoin.SKY_cipher_BitcoinAddressFromBytes(byte, address_2)
    assert err == skycoin.SKY_OK
    assert address == address_2
    _, addres_str = skycoin.SKY_cipher_Address_String(address)
    _, addres_2_str = skycoin.SKY_cipher_Address_String(address_2)
    assert addres_2_str == addres_str


def test_TestAddressVerify():
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    address = skycoin.cipher__Address()
    skycoin.SKY_cipher_AddressFromPubKey(public_key, address)
    # Valid pubkey+address
    err = skycoin.SKY_cipher_Address_Verify(address, public_key)
    assert err == skycoin.SKY_OK
    # Invalid pubkey
    public_key_temp = skycoin.cipher_PubKey()
    err = skycoin.SKY_cipher_Address_Verify(address, public_key_temp) 
    assert err == skycoin.SKY_ErrAddressInvalidPubKey
    skycoin.SKY_cipher_GenerateKeyPair(public_key_temp, secret_key)
    err = skycoin.SKY_cipher_Address_Verify(address, public_key_temp)
    assert err == skycoin.SKY_ErrAddressInvalidPubKey
    #  Bad version
    address.Version = 0x01
    err = skycoin.SKY_cipher_Address_Verify(address, public_key)
    assert err == skycoin.SKY_ErrAddressInvalidVersion


def test_TestAddressString():
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    address = skycoin.cipher__Address()
    skycoin.SKY_cipher_AddressFromPubKey(public_key, address)
    _, addres_str = skycoin.SKY_cipher_Address_String(address)
    address_2 = skycoin.cipher__Address()
    err = skycoin.SKY_cipher_DecodeBase58Address(addres_str, address_2)
    assert err == skycoin.SKY_OK
    assert address == address_2
    _, addres_2_str = skycoin.SKY_cipher_Address_String(address_2)
    addres_3 = skycoin.cipher__Address()
    err = skycoin.SKY_cipher_DecodeBase58Address(addres_2_str, addres_3)
    assert err == skycoin.SKY_OK
    assert address_2 == addres_3




def test_TestBitcoinAddress2():
    secret_key = skycoin.cipher_SecKey()
    err = skycoin.SKY_cipher_SecKeyFromHex(b'dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd', secret_key)
    assert err == skycoin.SKY_OK
    public_key = skycoin.cipher_PubKey()
    skycoin.SKY_cipher_PubKeyFromSecKey(secret_key, public_key)
    public_key_str = b'02ed83704c95d829046f1ac27806211132102c34e9ac7ffa1b71110658e5b9d1bd'
    _, public_key_hex = skycoin.SKY_cipher_PubKey_Hex(public_key)
    assert public_key_hex == public_key_str
    bitcoin_srt = b'1NKRhS7iYUGTaAfaR5z8BueAJesqaTyc4a'
    _, bitcoin_addr = skycoin.SKY_cipher_BitcoinAddressFromPubkey(public_key)
    assert bitcoin_srt == bitcoin_addr


def test_TestBitcoinAddress3():
    secret_key = skycoin.cipher_SecKey()
    err = skycoin.SKY_cipher_SecKeyFromHex(b'47f7616ea6f9b923076625b4488115de1ef1187f760e65f89eb6f4f7ff04b012', secret_key)
    assert err == skycoin.SKY_OK
    public_key = skycoin.cipher_PubKey()
    skycoin.SKY_cipher_PubKeyFromSecKey(secret_key, public_key)
    public_key_str = b'032596957532fc37e40486b910802ff45eeaa924548c0e1c080ef804e523ec3ed3'
    _, public_key_hex = skycoin.SKY_cipher_PubKey_Hex(public_key)
    assert public_key_hex == public_key_str
    bitcoin_srt = b'19ck9VKC6KjGxR9LJg4DNMRc45qFrJguvV'
    _, bitcoin_addr = skycoin.SKY_cipher_BitcoinAddressFromPubkey(public_key)
    assert bitcoin_srt == bitcoin_addr


def test_TestBitcoinWIPRoundTrio():
    public_key = skycoin.cipher_PubKey()
    secret_key_1 = skycoin.cipher_SecKey()
    secret_key_2 = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key_1)
    _, wip_1 = skycoin.SKY_cipher_BitcoinWalletImportFormatFromSeckey(
        secret_key_1)
    err = skycoin.SKY_cipher_SecKeyFromWalletImportFormat(wip_1, secret_key_2)
    assert err == skycoin.SKY_OK
    _, wip_2 = skycoin.SKY_cipher_BitcoinWalletImportFormatFromSeckey(secret_key_2)
    _, secret_key_1_hex = skycoin.SKY_cipher_SecKey_Hex(secret_key_1)
    _, secret_key_2_hex = skycoin.SKY_cipher_SecKey_Hex(secret_key_2)
    assert secret_key_1_hex == secret_key_2_hex
    assert wip_1 == wip_2


def test_TestBitcoinWIP():
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
        err = skycoin.SKY_cipher_SecKeyFromWalletImportFormat(wips[p], secret_key)
        assert err == skycoin.SKY_OK
        skycoin.SKY_cipher_PubKeyFromSecKey(secret_key, public_key)
        _, public_key_hex = skycoin.SKY_cipher_PubKey_Hex(public_key)
        assert public_key_hex == publics[p]
        _, bitcoin_addr = skycoin.SKY_cipher_BitcoinAddressFromPubkey(public_key)
        assert bitcoin_addr == address[p]


def test_TestAddressBulk():
    for _ in range(1024):
        public_key = skycoin.cipher_PubKey()
        secret_key = skycoin.cipher_SecKey()
        addres_1 = skycoin.cipher__Address()
        address_2 = skycoin.cipher__Address()
        _, data = skycoin.SKY_cipher_RandByte(32)
        skycoin.SKY_cipher_GenerateDeterministicKeyPair(
            data, public_key, secret_key)
        skycoin.SKY_cipher_AddressFromPubKey(public_key, addres_1)
        err = skycoin.SKY_cipher_Address_Verify(addres_1, public_key)
        assert err == skycoin.SKY_OK
        _, addres_str = skycoin.SKY_cipher_Address_String(addres_1)
        err =skycoin.SKY_cipher_DecodeBase58Address(addres_str, address_2)
        assert err == skycoin.SKY_OK
        assert addres_1 == address_2


def test_TestAddressNull():
    address = skycoin.cipher__Address()
    _error, isNull = skycoin.SKY_cipher_Address_Null(address)
    assert _error == skycoin.SKY_OK
    assert isNull == 1
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    skycoin.SKY_cipher_AddressFromPubKey(public_key, address)
    assert address is not None
