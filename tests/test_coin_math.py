import skycoin
import tests.utils


def test_TestAddUint64():
    err, n = skycoin.SKY_util_AddUint64(10, 11)
    assert err == skycoin.SKY_OK
    assert int(21) == n
    err, n = skycoin.SKY_util_AddUint64(int(0xFFFFFFFFFFFFFFFF), 1)
    assert err == skycoin.SKY_ErrUint64AddOverflow


class math_test:
    a = 0
    b = 0
    err = 0


def test_TestUint64ToInt64():
    cases = []
    values = math_test()
    cases.append(values)
    values.a = int(1)
    values.b = 1
    cases.append(values)
    values.a = int(0xFFFFFFFFFFFFFFFF)
    values.b = int(0xFFFFFFFFFFFFFFFF)
    values.err = skycoin.SKY_ErrUint64AddOverflow
    cases.append(values)
    values.a = int(0xFFFFFFFFFFFFFFFF)
    values.b = 0
    values.err = skycoin.SKY_ErrUint64AddOverflow
    cases.append(values)
    for val in cases:
        s = int(val.a)
        err, x = skycoin.SKY_util_Uint64ToInt64(s)
        if err != skycoin.SKY_OK:
            assert skycoin.SKY_ErrUint64AddOverflow == val.err
        else:
            assert val.b == x


def test_TestInt64ToUint64():
    cases = []
    values = math_test()
    cases.append(values)
    values.a = 1
    values.b = 1
    cases.append(values)
    values.a = int(-0xFFFFFFFFFFFFFFFF)
    values.b = int(0)
    values.err = skycoin.SKY_ErrUint64AddOverflow
    cases.append(values)
    values.a = int(-1)
    values.b = 0
    values.err = skycoin.SKY_ErrUint64AddOverflow
    cases.append(values)
    for val in cases:
        s = int(val.a)
        err, x = skycoin.SKY_util_Int64ToUint64(s)
        if err != skycoin.SKY_OK:
            assert skycoin.SKY_ErrUint64AddOverflow == val.err
        else:
            assert val.b == x
