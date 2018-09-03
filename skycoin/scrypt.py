from libpy import skycoin

def Key(p0, p1, p2, p3, p4, p5):
    return skycoin.SKY_scrypt_Key(p0, p1, p2, p3, p4, p5)