from .libpy import *

def UncompressedPubkeyFromSeckey(privkey):
    return skycoin.SKY_secp256k1_UncompressedPubkeyFromSeckey(privkey)

def GenerateKeyPair():
    return skycoin.SKY_secp256k1_GenerateKeyPair()

def Sign(msg, seckey):
    return skycoin.SKY_secp256k1_Sign(msg, seckey)

def VerifyPubkey(pub_key):
    return skycoin.SKY_secp256k1_VerifyPubkey(pub_key)

def RecoverPubkey(msg, sig):
    return skycoin.SKY_secp256k1_RecoverPubkey(msg, sig)

def VerifySeckey(sec_key):
    return skycoin.SKY_secp256k1_VerifySeckey(sec_key)

def VerifySignature(hashs, sig, pub_key):
    return skycoin.SKY_secp256k1_VerifySignature(hashs, sig, pub_key)

def RandByte(num):
    return skycoin.SKY_secp256k1_RandByte(num)

def DeterministicKeyPairIterator(seed):
    return skycoin.SKY_secp256k1_DeterministicKeyPairIterator(seed)

def GenerateDeterministicKeyPair(seed):
    return skycoin.SKY_secp256k1_GenerateDeterministicKeyPair(seed)

def Secp256k1Hash(_hash):
    return skycoin.SKY_secp256k1_Secp256k1Hash(_hash)

def ECDH(pub_key, sec_key):
    return skycoin.SKY_secp256k1_ECDH(pub_key, sec_key)

def PubkeyFromSeckey(sec_key):
    return skycoin.SKY_secp256k1_PubkeyFromSeckey(sec_key)