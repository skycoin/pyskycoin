# import skycoin
from .libpy import *

def String2Hex(cadena):
    return skycoin.SKY_base58_String2Hex(cadena)

def Hex2Base58(cadena):
    return skycoin.SKY_base58_Hex2Base58(cadena)
