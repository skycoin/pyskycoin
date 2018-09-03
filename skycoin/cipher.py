# from .libpy import *
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