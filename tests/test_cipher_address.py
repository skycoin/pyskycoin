import skycoin
from skycoin import _GoString_, SKY_cipher_BitcoinAddressFromPubkey


# cipher address
def test_TestMustDecodeBase58Address():
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    addres = skycoin.cipher__Address()
    skycoin.SKY_cipher_AddressFromPubKey(public_key, addres)
    assert skycoin.SKY_cipher_Address_Verify(addres, public_key) == 0

    assert skycoin.SKY_cipher_MustDecodeBase58Address(b'""', addres) != 0
    assert skycoin.SKY_cipher_MustDecodeBase58Address(b'"cascs"', addres) != 0

    _, byte = skycoin.SKY_cipher_Address_Bytes(addres)
    _, h = skycoin.SKY_base58_Hex2Base58(byte[:int(len(byte) / 2)])
    assert skycoin.SKY_cipher_MustDecodeBase58Address(b'h', addres) != 0

    _, h = skycoin.SKY_base58_Hex2Base58(byte)
    assert skycoin.SKY_cipher_MustDecodeBase58Address(h, addres) == 0

    addres_2 = skycoin.cipher__Address()
    skycoin.SKY_cipher_MustDecodeBase58Address(h, addres_2)
    assert addres == addres_2

    _, addres_str = skycoin.SKY_cipher_Address_String(addres)
    assert skycoin.SKY_cipher_MustDecodeBase58Address(addres_str, addres) == 0
    skycoin.SKY_cipher_MustDecodeBase58Address(addres_str, addres_2)
    assert addres == addres_2

    # preceding whitespace is invalid
    badAddr = skycoin.cipher__Address()
    badAddr = b'" " + addres_str'
    assert skycoin.SKY_cipher_MustDecodeBase58Address(badAddr, addres) != 0

    # preceding zeroes are invalid
    badAddr = b'"000" + addres_str'
    assert skycoin.SKY_cipher_MustDecodeBase58Address(badAddr, addres) != 0

    # trailing whitespace is invalid
    badAddr = b'addres_str + " "'
    assert skycoin.SKY_cipher_MustDecodeBase58Address(badAddr, addres) != 0

    # trailing zeroes are invalid
    badAddr = b'addres_str + "000"'
    assert skycoin.SKY_cipher_MustDecodeBase58Address(badAddr, addres) != 0


def test_TestDecodeBase58Address():
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    addres = skycoin.cipher__Address()
    skycoin.SKY_cipher_AddressFromPubKey(public_key, addres)
    assert skycoin.SKY_cipher_Address_Verify(addres, public_key) == 0

    addres_2 = skycoin.cipher__Address()

    assert skycoin.SKY_cipher_DecodeBase58Address(b'""', addres_2) != 0
    assert skycoin.SKY_cipher_DecodeBase58Address(b'"cascs"', addres_2) != 0

    _, byte = skycoin.SKY_cipher_Address_Bytes(addres)
    _, h = skycoin.SKY_base58_Hex2Base58(byte[:int(len(byte) / 2)])
    assert skycoin.SKY_cipher_DecodeBase58Address(b'h', addres_2) != 0
    _, h = skycoin.SKY_base58_Hex2Base58(byte)
    assert skycoin.SKY_cipher_DecodeBase58Address(h, addres_2) == 0
    assert addres == addres_2

    _, addres_str = skycoin.SKY_cipher_Address_String(addres)
    assert skycoin.SKY_cipher_DecodeBase58Address(addres_str, addres_2) == 0
    assert addres == addres_2

	#  preceding whitespace is invalid
    addres_2_str = b'" " + a_str'
    assert skycoin.SKY_cipher_DecodeBase58Address(addres_2_str, addres_2) != 0

	#  preceding zeroes are invalid
    addres_2_str = b'"000" + a_str'
    assert skycoin.SKY_cipher_DecodeBase58Address(addres_2_str, addres_2) != 0

	#  trailing whitespace is invalid
    addres_2_str = b'a_str + " "'
    assert skycoin.SKY_cipher_DecodeBase58Address(addres_2_str, addres_2) != 0

	# trailing zeroes are invalid
    addres_2_str = b'a_str + "000"'
    assert skycoin.SKY_cipher_DecodeBase58Address(addres_2_str, addres_2) != 0


def test_TestAddressFromBytes():
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    addres = skycoin.cipher__Address()
    skycoin.SKY_cipher_AddressFromPubKey(public_key, addres)
    addres_2 = skycoin.cipher__Address()
    _, byte = skycoin.SKY_cipher_Address_Bytes(addres)
    assert skycoin.SKY_cipher_AddressFromBytes(byte , addres_2) == 0
    assert addres ==addres_2

    # Invalid number of bytes
    __ = skycoin.cipher__Address()
    assert skycoin.SKY_cipher_AddressFromBytes(byte[:len(byte) - 2] , __) != 0  # "Invalid address length"

    # Invalid checksum
    str_bte = byte[:len(byte) - 2]
    bte = byte[len(byte) - 1]
    byte_bte_update = bytes(bte) + b'1'
    str_bte += byte_bte_update
    assert skycoin.SKY_cipher_AddressFromBytes(str_bte , __) != 0  # "Invalid checksum"

    addres.Version = 2
    _, b = skycoin.SKY_cipher_Address_Bytes(addres)
    assert skycoin.SKY_cipher_AddressFromBytes(b , __) != 0  # "Invalid Version"


def test_TestBitcoinAddressFromBytes():
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    addres = skycoin.cipher__Address()
    skycoin.SKY_cipher_AddressFromPubKey(public_key, addres)
    addres_2 = skycoin.cipher__Address()
    _, byte = skycoin.SKY_cipher_Address_BitcoinBytes(addres)
    assert skycoin.SKY_cipher_BitcoinAddressFromBytes(byte, addres_2) == 0
    assert addres_2 == addres

    # Invalid number of bytes
    __ = skycoin.cipher__Address()
    assert skycoin.SKY_cipher_BitcoinAddressFromBytes(byte[:len(byte) - 2], __) != 0 # "Invalid address length"

    # Invalid checksum
    str_bte = byte[:len(byte) - 2]
    bte = byte[len(byte) - 1]
    byte_bte_update = bytes(bte) + b'1'
    str_bte += byte_bte_update
    assert skycoin.SKY_cipher_BitcoinAddressFromBytes(str_bte , __) != 0  # "Invalid checksum"

    #Invalid Version
    addres.Version = 2
    _, byte = skycoin.SKY_cipher_Address_BitcoinBytes(addres)
    assert skycoin.SKY_cipher_BitcoinAddressFromBytes(byte, __) != 0 # "Invalid Version"


def test_TestAddressRoundtrip():
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    addres = skycoin.cipher__Address()
    addres_2 = skycoin.cipher__Address()
    skycoin.SKY_cipher_AddressFromPubKey(public_key, addres)
    _, byte = skycoin.SKY_cipher_Address_BitcoinBytes(addres)
    assert skycoin.SKY_cipher_BitcoinAddressFromBytes(byte, addres_2) == 0
    assert addres == addres_2
    _, addres_str = skycoin.SKY_cipher_Address_String(addres)
    _, addres_2_str = skycoin.SKY_cipher_Address_String(addres_2)
    assert addres_2_str == addres_str

def test_TestAddressVerify():
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    addres = skycoin.cipher__Address()
    skycoin.SKY_cipher_AddressFromPubKey(public_key, addres)

    # Valid pubkey+address
    assert skycoin.SKY_cipher_Address_Verify(addres, public_key) == 0

    # Invalid pubkey
    public_key_temp = skycoin.cipher_PubKey()
    assert skycoin.SKY_cipher_Address_Verify(addres, public_key_temp) != 0
    skycoin.SKY_cipher_GenerateKeyPair(public_key_temp, secret_key)
    assert skycoin.SKY_cipher_Address_Verify(addres, public_key_temp) != 0

    #  Bad version
    addres.Version = 0x01
    assert skycoin.SKY_cipher_Address_Verify(addres, public_key) != 0

def test_TestAddressString():
    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    addres = skycoin.cipher__Address()
    skycoin.SKY_cipher_AddressFromPubKey(public_key, addres)
    _, addres_str = skycoin.SKY_cipher_Address_String(addres)
    addres_2 = skycoin.cipher__Address()
    assert skycoin.SKY_cipher_DecodeBase58Address( addres_str, addres_2) == 0
    assert addres == addres_2
    _, addres_2_str = skycoin.SKY_cipher_Address_String(addres_2)
    addres_3 = skycoin.cipher__Address()
    assert skycoin.SKY_cipher_DecodeBase58Address( addres_2_str, addres_3) == 0
    assert addres_2 ==addres_3

def test_TestBitcoinAddress1():
    secret_key = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_MustSecKeyFromHex(b'1111111111111111111111111111111111111111111111111111111111111111', secret_key)
    public_key = skycoin.cipher_PubKey()
    skycoin.SKY_cipher_PubKeyFromSecKey(secret_key, public_key)
    public_key_str = b'034f355bdcb7cc0af728ef3cceb9615d90684bb5b2ca5f859ab0f0b704075871aa'
    _, public_key_hex = skycoin.SKY_cipher_PubKey_Hex(public_key)
    assert public_key_hex == public_key_str
    bitcoin_srt = b'1Q1pE5vPGEEMqRcVRMbtBK842Y6Pzo6nK9'
    _, bitcoin_addr = skycoin.SKY_cipher_BitcoinAddressFromPubkey(public_key)
    assert bitcoin_srt == bitcoin_addr

def test_TestBitcoinAddress2():
    secret_key = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_MustSecKeyFromHex(b'dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd', secret_key)
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
    skycoin.SKY_cipher_MustSecKeyFromHex(b'47f7616ea6f9b923076625b4488115de1ef1187f760e65f89eb6f4f7ff04b012', secret_key)
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
    _, wip_1 = skycoin.SKY_cipher_BitcoinWalletImportFormatFromSeckey(secret_key_1)
    assert skycoin.SKY_cipher_SecKeyFromWalletImportFormat(wip_1, secret_key_2) == 0
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
        assert skycoin.SKY_cipher_SecKeyFromWalletImportFormat(wips[p], secret_key) == 0
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
        addres_2 = skycoin.cipher__Address()
        data = skycoin.SKY_cipher_RandByte(32)
        skycoin.SKY_cipher_GenerateDeterministicKeyPair(b'data', public_key, secret_key)
        skycoin.SKY_cipher_AddressFromPubKey(public_key, addres_1)
        assert skycoin.SKY_cipher_Address_Verify(addres_1, public_key) == 0
        _, addres_str = skycoin.SKY_cipher_Address_String(addres_1)
        assert skycoin.SKY_cipher_DecodeBase58Address(addres_str, addres_2) == 0
        assert addres_1 == addres_2

def test_TestAddressNull():
    addres = skycoin.cipher__Address()
    error, isNull = skycoin.SKY_cipher_Address_Null(addres)
    assert error == 0
    assert isNull == 1

    public_key = skycoin.cipher_PubKey()
    secret_key = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)
    assert skycoin.SKY_cipher_AddressFromPubKey(public_key, addres) == 0 #Null False
