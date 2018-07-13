import skycoin


# cipher address
def test_TestMustDecodeBase58Address():
    p = skycoin.cipher_PubKey()
    s = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(p, s)
    a = skycoin.cipher__Address()
    skycoin.SKY_cipher_AddressFromPubKey(p, a)    
    assert skycoin.SKY_cipher_Address_Verify(a, p) == 0
    
    assert skycoin.SKY_cipher_MustDecodeBase58Address("", a) != 0 
    assert skycoin.SKY_cipher_MustDecodeBase58Address("cascs", a) != 0 
  
    _, b = skycoin.SKY_cipher_Address_Bytes(a)
    _, h = skycoin.SKY_base58_Hex2Base58(b[:len(b) / 2])
    assert skycoin.SKY_cipher_MustDecodeBase58Address(str(h), a) != 0

    _, h = skycoin.SKY_base58_Hex2Base58(b)    
    assert skycoin.SKY_cipher_MustDecodeBase58Address(str(h), a) == 0

    a2 = skycoin.cipher__Address()
    skycoin.SKY_cipher_MustDecodeBase58Address(h, a2)
    assert a.isEqual(a2)

    _, a_str = skycoin.SKY_cipher_Address_String(a)	
    assert skycoin.SKY_cipher_MustDecodeBase58Address(a_str, a) == 0
    skycoin.SKY_cipher_MustDecodeBase58Address(a_str, a2)
    assert a.isEqual(a2)

    # preceding whitespace is invalid
    badAddr = " " + a_str
    assert skycoin.SKY_cipher_MustDecodeBase58Address(badAddr, a) != 0
   
    # preceding zeroes are invalid
    badAddr = "000" + a_str
    assert skycoin.SKY_cipher_MustDecodeBase58Address(badAddr, a) != 0

    # trailing whitespace is invalid
    badAddr = a_str + " "
    assert skycoin.SKY_cipher_MustDecodeBase58Address(badAddr, a) != 0

    # trailing zeroes are invalid
    badAddr = a_str + "000"
    assert skycoin.SKY_cipher_MustDecodeBase58Address(badAddr, a) != 0


def test_TestDecodeBase58Address():
    p = skycoin.cipher_PubKey()
    s = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(p, s)
    a = skycoin.cipher__Address()
    skycoin.SKY_cipher_AddressFromPubKey(p, a)    
    assert skycoin.SKY_cipher_Address_Verify(a, p) == 0

    a2 = skycoin.cipher__Address()

    assert skycoin.SKY_cipher_DecodeBase58Address("", a2) != 0  
    assert skycoin.SKY_cipher_DecodeBase58Address("cascs", a2) != 0  
  
    _, b = skycoin.SKY_cipher_Address_Bytes(a)
    _, h = skycoin.SKY_base58_Hex2Base58(b[:len(b) / 2])
    assert skycoin.SKY_cipher_DecodeBase58Address(h, a2) != 0  
    _, h = skycoin.SKY_base58_Hex2Base58(b)
    assert skycoin.SKY_cipher_DecodeBase58Address(h, a2) == 0  
    assert a.isEqual(a2)

    _, a_str = skycoin.SKY_cipher_Address_String(a)
    assert skycoin.SKY_cipher_DecodeBase58Address(a_str, a2) == 0  
    assert a.isEqual(a2)

	#  preceding whitespace is invalid
    a2_str = " " + a_str
    assert skycoin.SKY_cipher_DecodeBase58Address(a2_str, a2) != 0

	#  preceding zeroes are invalid
    a2_str = "000" + a_str
    assert skycoin.SKY_cipher_DecodeBase58Address(a2_str, a2) != 0

	#  trailing whitespace is invalid
    a2_str = a_str + " "
    assert skycoin.SKY_cipher_DecodeBase58Address(a2_str, a2) != 0

	# trailing zeroes are invalid
    a2_str = a_str + "000"
    assert skycoin.SKY_cipher_DecodeBase58Address(a2_str, a2) != 0


def test_TestAddressFromBytes():
    p = skycoin.cipher_PubKey()
    s = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(p, s)
    a = skycoin.cipher__Address()
    skycoin.SKY_cipher_AddressFromPubKey(p, a) 
    a2 = skycoin.cipher__Address()   
    _, b = skycoin.SKY_cipher_Address_Bytes(a)
    assert skycoin.SKY_cipher_AddressFromBytes(b , a2) == 0                  
    assert a.isEqual(a2)

    # Invalid number of bytes
    __ = skycoin.cipher__Address()   
    assert skycoin.SKY_cipher_AddressFromBytes(b[:len(b) - 2] , __) != 0  # "Invalid address length"

    # Invalid checksum
    str_bte = b[:len(b) - 2]
    bte = b[len(b) - 1]
    byte_bte_update = b'bte' + str(0b1)
    str_bte += byte_bte_update 
    assert skycoin.SKY_cipher_AddressFromBytes(str_bte , __) != 0  # "Invalid checksum"

    a.Version = 2
    _, b = skycoin.SKY_cipher_Address_Bytes(a)
    assert skycoin.SKY_cipher_AddressFromBytes(b , __) != 0  # "Invalid Version"

    
def test_TestBitcoinAddressFromBytes():
    p = skycoin.cipher_PubKey()
    s = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(p, s)
    a = skycoin.cipher__Address()
    skycoin.SKY_cipher_AddressFromPubKey(p, a) 
    a2 = skycoin.cipher__Address()   
    _, byte = skycoin.SKY_cipher_Address_BitcoinBytes(a)
    assert skycoin.SKY_cipher_BitcoinAddressFromBytes(byte, a2) == 0
    assert a2.isEqual(a)

    # Invalid number of bytes
    __ = skycoin.cipher__Address() 
    assert skycoin.SKY_cipher_BitcoinAddressFromBytes(byte[:len(byte) - 2], __) != 0 # "Invalid address length"

    # Invalid checksum
    str_bte = byte[:len(byte) - 2]
    bte = byte[len(byte) - 1]
    byte_bte_update = b'bte' + str(0b1)
    str_bte += byte_bte_update 
    assert skycoin.SKY_cipher_AddressFromBytes(str_bte , __) != 0  # "Invalid checksum"

    #Invalid Version
    a.Version = 2
    _, byte = skycoin.SKY_cipher_Address_BitcoinBytes(a)
    assert skycoin.SKY_cipher_BitcoinAddressFromBytes(byte, __) != 0 # "Invalid Version"


def test_TestAddressRoundtrip():
    # Tests encode and decode
    p = skycoin.cipher_PubKey()
    s = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(p, s)
    a = skycoin.cipher__Address()
    a2 = skycoin.cipher__Address()
    skycoin.SKY_cipher_AddressFromPubKey(p, a)  
    _, byte = skycoin.SKY_cipher_Address_BitcoinBytes(a)
    assert skycoin.SKY_cipher_BitcoinAddressFromBytes(byte, a2) == 0
    assert a.isEqual(a2)
    _, a_str = skycoin.SKY_cipher_Address_String(a)	
    _, a2_str = skycoin.SKY_cipher_Address_String(a2)	
    assert a2_str == a_str