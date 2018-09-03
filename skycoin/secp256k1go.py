# import skycoin
from .libpy import *

def NumberCreate():
    return skycoin.SKY_secp256k1go_Number_Create()

def XYZ():
    return skycoin.secp256k1go__XYZ()

def FieldSetHex(public_key, cadena):
    return skycoin.SKY_secp256k1go_Field_SetHex(public_key, cadena)

def NumberSetHex(num, cadena):
    return skycoin.SKY_secp256k1go_Number_SetHex(num, cadena)

def XYZECmult(public_keyj, pr, u2, u1):
    return skycoin.SKY_secp256k1go_XYZ_ECmult(public_keyj, pr, u2, u1)

def XYZEquals(pr, expres):
    return skycoin.SKY_secp256k1go_XYZ_Equals(pr, expres)

def Field():
    return skycoin.secp256k1go__Field()

def ECmultGen(pr, noce):
    return skycoin.SKY_secp256k1go_ECmultGen(pr, noce)

def FieldNormalize(p0):
    return skycoin.SKY_secp256k1go_Field_Normalize(p0)

def FieldEquals(p0, p1):
    return skycoin.SKY_secp256k1go_Field_Equals(p0, p1)