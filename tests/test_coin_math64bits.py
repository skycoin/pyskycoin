import skycoin
import tests.utils
import ctypes


class StrTmp():
    a = 0
    b = ctypes.c_uint32(0)
    err = skycoin.SKY_OK

    def __init__(self, a, b, err=skycoin.SKY_OK):
        self.a = a
        self.b = b
        self.err = err


cases = []

cases.append(StrTmp((1 << 32), 0, skycoin.SKY_ErrIntOverflowsUint32))
cases.append(StrTmp((1 << 32 - 1), (1 << 32 - 1)))


def test_Test64BitIntToUint32():
    for tc in cases:
        err, x = skycoin.SKY_coin_IntToUint32(tc.a)
        if err != skycoin.SKY_OK:
            assert tc.err == err
        else:
            assert ctypes.c_uint32(tc.b).value == ctypes.c_uint32(x).value
