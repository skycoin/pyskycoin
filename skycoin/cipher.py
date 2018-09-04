from libpy import skycoin

def PubKey():
    return skycoin.cipher_PubKey()

def SecKey():
    return skycoin.cipher_SecKey()

def Address():
    return skycoin.cipher__Address()

def AddressFromPubKey(public_key, addres):
    return skycoin.SKY_cipher_AddressFromPubKey(public_key, addres)

def NewPubKey(hex_str, public_key):
    return skycoin.SKY_cipher_NewPubKey(hex_str, public_key)

def NewSecKey(hex_str, secret_key):
    return skycoin.SKY_cipher_NewSecKey(hex_str, secret_key)

def PubKeyFromSecKey(secret_key, public_key):
    return skycoin.SKY_cipher_PubKeyFromSecKey(secret_key, public_key)

def GenerateKeyPair(public_key, secret_key):
    return skycoin.SKY_cipher_GenerateKeyPair(public_key, secret_key)

def TestSecKey(secret_key):
    return skycoin.SKY_cipher_TestSecKey(secret_key)

def SHA256():
    return skycoin.cipher_SHA256()

def SumSHA256(text, sha):
    return skycoin.SKY_cipher_SumSHA256(text, sha)

def TestSecKeyHash(secret_key, sha):
    return skycoin.SKY_cipher_TestSecKeyHash(secret_key, sha)

def AddressVerify(address, public_key):
    return skycoin.SKY_cipher_Address_Verify(address, public_key)

def DecodeBase58Address(cadena, address):
    return skycoin.SKY_cipher_DecodeBase58Address(cadena, address)

def AddressBytes(address):
    return skycoin.SKY_cipher_Address_Bytes(address)

def AddressString(address):
    return skycoin.SKY_cipher_Address_String(address)

def AddressFromBytes(byte, address):
    return skycoin.SKY_cipher_AddressFromBytes(byte, address)

def AddressBitcoinBytes(address):
    return skycoin.SKY_cipher_Address_BitcoinBytes(address)

def BitcoinAddressFromBytes(byte, address):
    return skycoin.SKY_cipher_BitcoinAddressFromBytes(byte, address)

def PubKeyHex(public_key):
    return skycoin.SKY_cipher_PubKey_Hex(public_key)

def BitcoinAddressFromPubkey(public_key):
    return skycoin.SKY_cipher_BitcoinAddressFromPubkey(public_key)

def SecKeyFromHex(cadena, secret_key):
    return skycoin.SKY_cipher_SecKeyFromHex(cadena, secret_key)

def BitcoinWalletImportFormatFromSeckey(secret_key):
    return skycoin.SKY_cipher_BitcoinWalletImportFormatFromSeckey(secret_key)

def SecKeyFromWalletImportFormat(wip_1, secret_key):
    return skycoin.SKY_cipher_SecKeyFromWalletImportFormat(wip_1, secret_key)

def SecKeyHex(secret_key):
    return skycoin.SKY_cipher_SecKey_Hex(secret_key)

def RandByte(rang):
    return skycoin.SKY_cipher_RandByte(rang)

def GenerateDeterministicKeyPair(data, public_key, secret_key):
    return skycoin.SKY_cipher_GenerateDeterministicKeyPair(data, public_key, secret_key)

def AddressNull(address):
    return skycoin.SKY_cipher_Address_Null(address)

def PubKeyVerify(public_key):
    return skycoin.SKY_cipher_PubKey_Verify(public_key)

def SecKeyVerify(secret_key):
    return skycoin.SKY_cipher_SecKey_Verify(secret_key)

def ECDH(public_key_2, secret_key_1):
    return skycoin.SKY_cipher_ECDH(public_key_2, secret_key_1)

def Sig():
    return skycoin.cipher_Sig()

def NewSig(data, sig):
    return skycoin.SKY_cipher_NewSig(data, sig)

def SignHash(sha_sum, secret_key_1, sig_1):
    return skycoin.SKY_cipher_SignHash(sha_sum, secret_key_1, sig_1)

def ChkSig(addres, sha_sum, sig_1):
    return skycoin.SKY_cipher_ChkSig(addres, sha_sum, sig_1)

def PubKeyFromSig(sig_1, sha_sum, public_key_2):
    return skycoin.SKY_cipher_PubKeyFromSig(sig_1, sha_sum, public_key_2)

def VerifySignature(public_key, sig_1, sha_sum_1):
    return skycoin.SKY_cipher_VerifySignature(public_key, sig_1, sha_sum_1)

def GenerateDeterministicKeyPairsSeed(seed, num):
    return skycoin.SKY_cipher_GenerateDeterministicKeyPairsSeed(seed, num)

def Ripemd160():
    return skycoin.cipher_Ripemd160()

def HashRipemd160(p0, p1):
    return skycoin.SKY_cipher_HashRipemd160(p0, p1)

def Ripemd160Set(h, b):
    return skycoin.SKY_cipher_Ripemd160_Set(h, b)

def SHA256Set(h, b):
    return skycoin.SKY_cipher_SHA256_Set(h, b)

def SHA256Hex(h):
    return skycoin.SKY_cipher_SHA256_Hex(h)

def SHA256FromHex(p0, p1):
    return skycoin.SKY_cipher_SHA256FromHex(p0, p1)

def DoubleSHA256(b, h):
    return skycoin.SKY_cipher_DoubleSHA256(b, h)

def AddSHA256(p0, p1, p2):
    return skycoin.SKY_cipher_AddSHA256(p0, p1, p2)

def SHA256Xor(p0, p1, p2):
    return skycoin.SKY_cipher_SHA256_Xor(p0, p1, p2)

def SHA256Null(p0):
    return skycoin.SKY_cipher_SHA256_Null(p0)

