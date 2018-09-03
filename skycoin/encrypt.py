from libpy import skycoin

def Sha256XorEncrypt(data, cadena):
    return skycoin.SKY_encrypt_Sha256Xor_Encrypt(data, cadena)

def Sha256XorDecrypt(p0, p1):
    return skycoin.SKY_encrypt_Sha256Xor_Decrypt(p0, p1)

def ScryptChacha20poly1305():
    return skycoin.encrypt__ScryptChacha20poly1305()

def ScryptChacha20poly1305Encrypt(crypt, plaintext, passwd):
    return skycoin.SKY_encrypt_ScryptChacha20poly1305_Encrypt(crypt, plaintext, passwd)

def ScryptChacha20poly1305Decrypt(crypt, encrypto, password):
    return skycoin.SKY_encrypt_ScryptChacha20poly1305_Decrypt(crypt, encrypto, password)