import skycoin
import tests.utils
import ctypes


class StrTmp():
    a = 0
    b = ctypes.c_uint32(0)
    err = 0

    def __init__(self, a, b, err=0):
        self.a = a
        self.b = b
        self.err = err


def test_Test64BitIntToUint32():
    cases = []
    cases.append(StrTmp((1 << 32), 0, skycoin.SKY_ErrIntOverflowsUint32))
    cases.append(StrTmp((1 << 32 - 2), (1 << 32 - 2)))
    for tc in cases:
        err, x = skycoin.SKY_util_IntToUint32(tc.a)
        if err != skycoin.SKY_OK:
            assert tc.err == err
        else:
            assert ctypes.c_uint32(tc.b).value == ctypes.c_uint32(x).value
