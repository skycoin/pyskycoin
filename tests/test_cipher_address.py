import skycoin

def test_TestDecodeBase58Address():
    public_key = skycoin.cipher.PubKey()
    secret_key = skycoin.cipher.SecKey()
    skycoin.cipher.GenerateKeyPair(public_key, secret_key)
    address = skycoin.cipher.Address()
    skycoin.cipher.AddressFromPubKey(public_key, address)
    err = skycoin.cipher.AddressVerify(address, public_key)
    assert err == skycoin.SKY_OK
    address_2 = skycoin.cipher.Address()
    err = skycoin.cipher.DecodeBase58Address(b'""', address_2) 
    assert err == skycoin.SKY_ErrInvalidBase58Char
    err = skycoin.cipher.DecodeBase58Address(b'"cascs"', address_2) 
    assert err == skycoin.SKY_ErrInvalidBase58Char
    _, byte = skycoin.cipher.AddressBytes(address)
    _, h = skycoin.base58.Hex2Base58(byte[:int(len(byte) / 2)])
    err = skycoin.cipher.DecodeBase58Address(h, address_2) 
    assert err == skycoin.SKY_ErrAddressInvalidLength
    _, h = skycoin.base58.Hex2Base58(byte)
    err = skycoin.cipher.DecodeBase58Address(h, address_2) 
    assert err == skycoin.SKY_OK
    assert address == address_2
    _, addres_str = skycoin.cipher.AddressString(address)
    err = skycoin.cipher.DecodeBase58Address(addres_str, address_2)
    assert err == skycoin.SKY_OK
    assert address == address_2
    #  preceding whitespace is invalid
    addres_2_str = b'" " + a_str'
    err = skycoin.cipher.DecodeBase58Address(addres_2_str, address_2)
    assert err == skycoin.SKY_ErrInvalidBase58Char
    #  preceding zeroes are invalid
    addres_2_str = b'"000" + a_str'
    err = skycoin.cipher.DecodeBase58Address(addres_2_str, address_2)
    assert err == skycoin.SKY_ErrInvalidBase58Char
    #  trailing whitespace is invalid
    addres_2_str = b'a_str + " "'
    err = skycoin.cipher.DecodeBase58Address(addres_2_str, address_2)
    assert err == skycoin.SKY_ErrInvalidBase58Char
    # trailing zeroes are invalid
    addres_2_str = b'a_str + "000"'
    err = skycoin.cipher.DecodeBase58Address(addres_2_str, address_2)
    assert err == skycoin.SKY_ErrInvalidBase58Char


def test_TestAddressFromBytes():
    public_key = skycoin.cipher.PubKey()
    secret_key = skycoin.cipher.SecKey()
    skycoin.cipher.GenerateKeyPair(public_key, secret_key)
    address = skycoin.cipher.Address()
    skycoin.cipher.AddressFromPubKey(public_key, address)
    address_2 = skycoin.cipher.Address()
    _, byte = skycoin.cipher.AddressBytes(address)
    err = skycoin.cipher.AddressFromBytes(byte, address_2) 
    assert err == skycoin.SKY_OK
    assert address == address_2
    # Invalid number of bytes
    __ = skycoin.cipher.Address()
    err = skycoin.cipher.AddressFromBytes(byte[:len(byte) - 2], __)
    assert err == skycoin.SKY_ErrAddressInvalidLength
    # Invalid checksum
    byte_array = bytearray(byte)
    byte_array[-1] = 1
    byte_new = bytes(byte_array)
    err = skycoin.cipher.AddressFromBytes(byte_new, __)
    assert err == skycoin.SKY_ErrAddressInvalidChecksum
    address.Version = 2
    _, b = skycoin.cipher.AddressBytes(address)
    err = skycoin.cipher.AddressFromBytes(b, __) 
    assert err == skycoin.SKY_ErrAddressInvalidVersion


def test_TestBitcoinAddressFromBytes():
    public_key = skycoin.cipher.PubKey()
    secret_key = skycoin.cipher.SecKey()
    skycoin.cipher.GenerateKeyPair(public_key, secret_key)
    address = skycoin.cipher.Address()
    skycoin.cipher.AddressFromPubKey(public_key, address)
    address_2 = skycoin.cipher.Address()
    _, byte = skycoin.cipher.AddressBitcoinBytes(address)
    err = skycoin.cipher.BitcoinAddressFromBytes(byte, address_2) 
    assert err == skycoin.SKY_OK
    assert address_2 == address
    # Invalid number of bytes
    __ = skycoin.cipher.Address()
    err = skycoin.cipher.BitcoinAddressFromBytes(byte[:len(byte) - 2], __)
    assert err == skycoin.SKY_ErrAddressInvalidLength
    # Invalid checksum
    byte_array = bytearray(byte)
    byte_array[-1] = 1
    byte_new = bytes(byte_array)
    err = skycoin.cipher.BitcoinAddressFromBytes(byte_new, __)
    assert err == skycoin.SKY_ErrAddressInvalidChecksum
    # Invalid Version
    address.Version = 2
    _, byte = skycoin.cipher.AddressBitcoinBytes(address)
    err = skycoin.cipher.BitcoinAddressFromBytes(byte, __)
    assert err == skycoin.SKY_ErrAddressInvalidVersion


def test_TestAddressRoundtrip():
    public_key = skycoin.cipher.PubKey()
    secret_key = skycoin.cipher.SecKey()
    skycoin.cipher.GenerateKeyPair(public_key, secret_key)
    address = skycoin.cipher.Address()
    address_2 = skycoin.cipher.Address()
    skycoin.cipher.AddressFromPubKey(public_key, address)
    _, byte = skycoin.cipher.AddressBitcoinBytes(address)
    err = skycoin.cipher.BitcoinAddressFromBytes(byte, address_2)
    assert err == skycoin.SKY_OK
    assert address == address_2
    _, addres_str = skycoin.cipher.AddressString(address)
    _, addres_2_str = skycoin.cipher.AddressString(address_2)
    assert addres_2_str == addres_str


def test_TestAddressVerify():
    public_key = skycoin.cipher.PubKey()
    secret_key = skycoin.cipher.SecKey()
    skycoin.cipher.GenerateKeyPair(public_key, secret_key)
    address = skycoin.cipher.Address()
    skycoin.cipher.AddressFromPubKey(public_key, address)
    # Valid pubkey+address
    err = skycoin.cipher.AddressVerify(address, public_key)
    assert err == skycoin.SKY_OK
    # Invalid pubkey
    public_key_temp = skycoin.cipher.PubKey()
    err = skycoin.cipher.AddressVerify(address, public_key_temp) 
    assert err == skycoin.SKY_ErrAddressInvalidPubKey
    skycoin.cipher.GenerateKeyPair(public_key_temp, secret_key)
    err = skycoin.cipher.AddressVerify(address, public_key_temp)
    assert err == skycoin.SKY_ErrAddressInvalidPubKey
    #  Bad version
    address.Version = 0x01
    err = skycoin.cipher.AddressVerify(address, public_key)
    assert err == skycoin.SKY_ErrAddressInvalidVersion


def test_TestAddressString():
    public_key = skycoin.cipher.PubKey()
    secret_key = skycoin.cipher.SecKey()
    skycoin.cipher.GenerateKeyPair(public_key, secret_key)
    address = skycoin.cipher.Address()
    skycoin.cipher.AddressFromPubKey(public_key, address)
    _, addres_str = skycoin.cipher.AddressString(address)
    address_2 = skycoin.cipher.Address()
    err = skycoin.cipher.DecodeBase58Address(addres_str, address_2)
    assert err == skycoin.SKY_OK
    assert address == address_2
    _, addres_2_str = skycoin.cipher.AddressString(address_2)
    addres_3 = skycoin.cipher.Address()
    err = skycoin.cipher.DecodeBase58Address(addres_2_str, addres_3)
    assert err == skycoin.SKY_OK
    assert address_2 == addres_3


def test_TestBitcoinAddress2():
    secret_key = skycoin.cipher.SecKey()
    err = skycoin.cipher.SecKeyFromHex(b'dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd', secret_key)
    assert err == skycoin.SKY_OK
    public_key = skycoin.cipher.PubKey()
    skycoin.cipher.PubKeyFromSecKey(secret_key, public_key)
    public_key_str = b'02ed83704c95d829046f1ac27806211132102c34e9ac7ffa1b71110658e5b9d1bd'
    _, public_key_hex = skycoin.cipher.PubKeyHex(public_key)
    assert public_key_hex == public_key_str
    bitcoin_srt = b'1NKRhS7iYUGTaAfaR5z8BueAJesqaTyc4a'
    _, bitcoin_addr = skycoin.cipher.BitcoinAddressFromPubkey(public_key)
    assert bitcoin_srt == bitcoin_addr


def test_TestBitcoinAddress3():
    secret_key = skycoin.cipher.SecKey()
    err = skycoin.cipher.SecKeyFromHex(b'47f7616ea6f9b923076625b4488115de1ef1187f760e65f89eb6f4f7ff04b012', secret_key)
    assert err == skycoin.SKY_OK
    public_key = skycoin.cipher.PubKey()
    skycoin.cipher.PubKeyFromSecKey(secret_key, public_key)
    public_key_str = b'032596957532fc37e40486b910802ff45eeaa924548c0e1c080ef804e523ec3ed3'
    _, public_key_hex = skycoin.cipher.PubKeyHex(public_key)
    assert public_key_hex == public_key_str
    bitcoin_srt = b'19ck9VKC6KjGxR9LJg4DNMRc45qFrJguvV'
    _, bitcoin_addr = skycoin.cipher.BitcoinAddressFromPubkey(public_key)
    assert bitcoin_srt == bitcoin_addr


def test_TestBitcoinWIPRoundTrio():
    public_key = skycoin.cipher.PubKey()
    secret_key_1 = skycoin.cipher.SecKey()
    secret_key_2 = skycoin.cipher.SecKey()
    skycoin.cipher.GenerateKeyPair(public_key, secret_key_1)
    _, wip_1 = skycoin.cipher.BitcoinWalletImportFormatFromSeckey(secret_key_1)
    err = skycoin.cipher.SecKeyFromWalletImportFormat(wip_1, secret_key_2)
    assert err == skycoin.SKY_OK
    _, wip_2 = skycoin.cipher.BitcoinWalletImportFormatFromSeckey(secret_key_2)
    _, secret_key_1_hex = skycoin.cipher.SecKeyHex(secret_key_1)
    _, secret_key_2_hex = skycoin.cipher.SecKeyHex(secret_key_2)
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
        secret_key = skycoin.cipher.SecKey()
        public_key = skycoin.cipher.PubKey()
        err = skycoin.cipher.SecKeyFromWalletImportFormat(wips[p], secret_key)
        assert err == skycoin.SKY_OK
        skycoin.cipher.PubKeyFromSecKey(secret_key, public_key)
        _, public_key_hex = skycoin.cipher.PubKeyHex(public_key)
        assert public_key_hex == publics[p]
        _, bitcoin_addr = skycoin.cipher.BitcoinAddressFromPubkey(public_key)
        assert bitcoin_addr == address[p]


def test_TestAddressBulk():
    for _ in range(1024):
        public_key = skycoin.cipher.PubKey()
        secret_key = skycoin.cipher.SecKey()
        address_1 = skycoin.cipher.Address()
        address_2 = skycoin.cipher.Address()
        _, data = skycoin.cipher.RandByte(32)
        skycoin.cipher.GenerateDeterministicKeyPair(data, public_key, secret_key)
        skycoin.cipher.AddressFromPubKey(public_key, address_1)
        err = skycoin.cipher.AddressVerify(address_1, public_key)
        assert err == skycoin.SKY_OK
        _, addres_str = skycoin.cipher.AddressString(address_1)
        err =skycoin.cipher.DecodeBase58Address(addres_str, address_2)
        assert err == skycoin.SKY_OK
        assert address_1 == address_2


def test_TestAddressNull():
    address = skycoin.cipher.Address()
    _error, isNull = skycoin.cipher.AddressNull(address)
    assert _error == skycoin.SKY_OK
    assert isNull == 1
    public_key = skycoin.cipher.PubKey()
    secret_key = skycoin.cipher.SecKey()
    skycoin.cipher.GenerateKeyPair(public_key, secret_key)
    skycoin.cipher.AddressFromPubKey(public_key, address)
    assert address is not None
