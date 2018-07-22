import skycoin
from tests.utils.skyerror import error


def test_TestAddUint64():
    err, n = skycoin.SKY_coin_AddUint64(10, 11)
    assert err == error["SKY_OK"]
    assert int(21) == n
    err, n = skycoin.SKY_coin_AddUint64(int(0xFFFFFFFFFFFFFFFF), 1)
    assert err == error["SKY_ErrUint64AddOverflow"]


class math_test:
    a = 0
    b = 0
    err = "SKY_OK"


def test_TestUint64ToInt64():
    cases = []
    values = math_test()
    cases.append(values)
    values.a = int(1)
    values.b = 1
    cases.append(values)
    values.a = int(0xFFFFFFFFFFFFFFFF)
    values.b = int(0xFFFFFFFFFFFFFFFF)
    values.err = "SKY_ErrUint64OverflowsInt64"
    cases.append(values)
    values.a = int(0xFFFFFFFFFFFFFFFF)
    values.b = 0
    values.err = "SKY_ErrUint64OverflowsInt64"
    cases.append(values)
    for val in cases:
        s = int(val.a)
        err, x = skycoin.SKY_coin_Uint64ToInt64(s)
        if err != error["SKY_OK"]:
            assert error["SKY_ErrUint64OverflowsInt64"] == error[val.err]
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
    values.err = "SKY_ErrInt64UnderflowsUint64"
    cases.append(values)
    values.a = int(-1)
    values.b = 0
    values.err = "SKY_ErrInt64UnderflowsUint64"
    cases.append(values)
    for val in cases:
        s = int(val.a)
        err, x = skycoin.SKY_coin_Int64ToUint64(s)
        if err != error["SKY_OK"]:
            assert error["SKY_ErrInt64UnderflowsUint64"] == error[val.err]
        else:
            assert val.b == x
