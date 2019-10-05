import skycoin
import tests.utils as utils


class tmpstruct:
    s = "",
    n = 0,
    e = 0

    def __init__(self, _s, _n, _e=0):
        self.e = _e
        self.s = _s
        self.n = _n


def test_TestFromString():
    cases = []
    cases.append(tmpstruct(b"0", 0))
    cases.append(tmpstruct(b"0.", 0))
    cases.append(tmpstruct(b"0.0", 0))
    cases.append(tmpstruct(b"0.000000", 0))
    cases.append(tmpstruct(b"0.0000000", 0))
    cases.append(tmpstruct(b"0.0000001", 0, skycoin.SKY_ErrTooManyDecimals))
    cases.append(tmpstruct(b"0.000001", 1))
    cases.append(tmpstruct(b"0.0000010", 1))
    cases.append(tmpstruct(b"1", int(1e6)))
    cases.append(tmpstruct(b"1.000001", int(1e6 + 1)))
    cases.append(tmpstruct(b"-1", 0, skycoin.SKY_ErrNegativeValue))
    cases.append(tmpstruct(b"10000", int(1e4 * 1e6)))
    cases.append(tmpstruct(b"123456789.123456", int(123456789123456)))
    cases.append(tmpstruct(b"123.000456", int(123000456)))
    cases.append(tmpstruct(b"100SKY", 0, skycoin.SKY_ERROR))
    cases.append(tmpstruct(b"", 0, skycoin.SKY_ERROR))
    cases.append(tmpstruct(b"999999999999999999999999999999999999999999", 0, skycoin.SKY_ErrTooLarge))
    cases.append(tmpstruct(b"9223372036854.775807", 9223372036854775807))
    cases.append(tmpstruct(b"-9223372036854.775807", 0, skycoin.SKY_ErrNegativeValue))
    cases.append(tmpstruct(b"9223372036854775808", 0, skycoin.SKY_ErrTooLarge))
    cases.append(tmpstruct(b"9223372036854775807.000001", 0, skycoin.SKY_ErrTooLarge))
    cases.append(tmpstruct(b"9223372036854775807", 0, skycoin.SKY_ErrTooLarge))
    cases.append(tmpstruct(b"9223372036854775806.000001", 0, skycoin.SKY_ErrTooLarge))
    cases.append(tmpstruct(b"1.1", int(1e6 + 1e5)))
    cases.append(tmpstruct(b"1.01", int(1e6 + 1e4)))
    cases.append(tmpstruct(b"1.001", int(1e6 + 1e3)))
    cases.append(tmpstruct(b"1.0001", int(1e6 + 1e2)))
    cases.append(tmpstruct(b"1.00001", int(1e6 + 1e1)))
    cases.append(tmpstruct(b"1.000001", int(1e6 + 1e0)))
    cases.append(tmpstruct(b"1.0000001", 0, skycoin.SKY_ErrTooManyDecimals))

    for i  in range(len(cases)):
        tc = cases[i]
        err, n = skycoin.SKY_droplet_FromString(tc.s)

        if tc.e == skycoin.SKY_OK:
            assert tc.e == err
            assert tc.n == n
        else:
            assert tc.e == err
            assert 0 == n


def test_TestToString():
    cases = []
    cases.append(tmpstruct(b"0.000000", 0))
    cases.append(tmpstruct(b"0.000001", 1))
    cases.append(tmpstruct(b"1.000000", int(1e6)))
    cases.append(tmpstruct(b"0.100100", 100100))
    cases.append(tmpstruct(b"1.001000", 1001000))
    cases.append(tmpstruct(b"0.000999", 999))
    cases.append(tmpstruct(b"999.000000", 999000000))
    cases.append(tmpstruct(b"123.000456", 123000456))
    cases.append(tmpstruct(b"", 9223372036854775808, skycoin.SKY_ErrTooLarge))

    for tcc in cases:
        tc = tcc
        err, s = skycoin.SKY_droplet_ToString(tc.n)

        if tc.e == skycoin.SKY_OK:
            assert tc.s == s
        else:
            assert tc.e == err
            assert None == s
