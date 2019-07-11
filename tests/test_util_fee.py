import skycoin
import tests.utils as utils


class verifyTxFeeTestCase:
    inputHours = 0
    outputHours = 0
    err = 0

    def __init__(self, _inputHours, _outputHours, _err=0):
        self.inputHours = _inputHours
        self.outputHours = _outputHours
        self.err = _err


def test_TestVerifyTransactionFee():
    burnFactor2verifyTxFeeTestCase = []

    burnFactor2verifyTxFeeTestCase.append(
        verifyTxFeeTestCase(0, 0, skycoin.SKY_ErrTxnNoFee))
    burnFactor2verifyTxFeeTestCase.append(
        verifyTxFeeTestCase(1, 0, skycoin.SKY_OK))
    burnFactor2verifyTxFeeTestCase.append(
        verifyTxFeeTestCase(1, 1, skycoin.SKY_ErrTxnNoFee))
    burnFactor2verifyTxFeeTestCase.append(
        verifyTxFeeTestCase(2, 0, skycoin.SKY_OK))
    burnFactor2verifyTxFeeTestCase.append(
        verifyTxFeeTestCase(2, 1, skycoin.SKY_OK))
    burnFactor2verifyTxFeeTestCase.append(
        verifyTxFeeTestCase(2, 2, skycoin.SKY_ErrTxnNoFee))
    burnFactor2verifyTxFeeTestCase.append(
        verifyTxFeeTestCase(3, 0, skycoin.SKY_OK))
    burnFactor2verifyTxFeeTestCase.append(
        verifyTxFeeTestCase(3, 1, skycoin.SKY_OK))
    burnFactor2verifyTxFeeTestCase.append(
        verifyTxFeeTestCase(3, 2, skycoin.SKY_ErrTxnInsufficientFee))
    burnFactor2verifyTxFeeTestCase.append(
        verifyTxFeeTestCase(3, 3, skycoin.SKY_ErrTxnNoFee))
    burnFactor2verifyTxFeeTestCase.append(
        verifyTxFeeTestCase(4, 0, skycoin.SKY_OK))
    burnFactor2verifyTxFeeTestCase.append(
        verifyTxFeeTestCase(4, 1, skycoin.SKY_OK))
    burnFactor2verifyTxFeeTestCase.append(
        verifyTxFeeTestCase(4, 2, skycoin.SKY_OK))
    burnFactor2verifyTxFeeTestCase.append(
        verifyTxFeeTestCase(4, 3, skycoin.SKY_ErrTxnInsufficientFee))
    burnFactor2verifyTxFeeTestCase.append(
        verifyTxFeeTestCase(4, 4, skycoin.SKY_ErrTxnNoFee))
    addr = utils.makeAddress()
    emptyTxn = utils.makeEmptyTransaction()
    err, hours = skycoin.SKY_coin_Transaction_OutputHours(emptyTxn)
    assert err == skycoin.SKY_OK
    assert 0 == hours

    #  A txn with no outputs hours and no coinhours burn fee is valid
    err = skycoin.SKY_fee_VerifyTransactionFee(emptyTxn, 0, 2)
    assert err == skycoin.SKY_ErrTxnNoFee

    # A txn with no outputs hours but with a coinhours burn fee is valid
    err = skycoin.SKY_fee_VerifyTransactionFee(emptyTxn, 100, 2)
    assert err == skycoin.SKY_OK

    txn = utils.makeEmptyTransaction()
    addr = utils.makeAddress()
    err = skycoin.SKY_coin_Transaction_PushOutput(txn, addr, 0, int(1e6))
    assert err == skycoin.SKY_OK
    err = skycoin.SKY_coin_Transaction_PushOutput(txn, addr, 0, int(3e6))
    assert err == skycoin.SKY_OK

    err, hours = skycoin.SKY_coin_Transaction_OutputHours(txn)
    assert err == skycoin.SKY_OK
    assert hours == int(4e6)

    # A txn with insufficient net coinhours burn fee is invalid
    err = skycoin.SKY_fee_VerifyTransactionFee(txn, 0, 2)
    assert err == skycoin.SKY_ErrTxnNoFee

    err = skycoin.SKY_fee_VerifyTransactionFee(txn, 1, 2)
    assert err == skycoin.SKY_ErrTxnInsufficientFee

    # A txn with sufficient net coinhours burn fee is valid
    err, hours = skycoin.SKY_coin_Transaction_OutputHours(txn)
    assert err == skycoin.SKY_OK
    err = skycoin.SKY_fee_VerifyTransactionFee(txn, hours, 2)
    assert err == skycoin.SKY_OK
    err, hours = skycoin.SKY_coin_Transaction_OutputHours(txn)
    assert err == skycoin.SKY_OK
    err = skycoin.SKY_fee_VerifyTransactionFee(txn, hours * 10, 2)
    assert err == skycoin.SKY_OK

    # fee + hours overflows
    err = skycoin.SKY_fee_VerifyTransactionFee(
        txn, utils.MaxUint64 - int(3e6), 2)
    assert err == skycoin.SKY_ERROR

    # txn has overflowing output hours
    err = skycoin.SKY_coin_Transaction_PushOutput(
        txn, addr, 0, int(utils.MaxUint64 - 1e6 - 3e6 + 1))
    assert err == skycoin.SKY_OK
    err = skycoin.SKY_fee_VerifyTransactionFee(txn, 10, 2)
    assert err == skycoin.SKY_ERROR

    cases = burnFactor2verifyTxFeeTestCase

    for tc in cases:
        txn = utils.makeEmptyTransaction()
        err = skycoin.SKY_coin_Transaction_PushOutput(
            txn, addr, 0, tc.outputHours)
        assert tc.inputHours >= tc.outputHours
        err = skycoin.SKY_fee_VerifyTransactionFee(
            txn, int(tc.inputHours - tc.outputHours), 2)
        assert tc.err == err


class requiredFeeTestCase:
    hours = 0
    fee = 0

    def __init__(self, _hours, _fee):
        self.hours = _hours
        self.fee = _fee


def test_TestRequiredFee():

    burnFactor2RequiredFeeTestCases = []

    burnFactor2RequiredFeeTestCases.append(requiredFeeTestCase(0, 0))
    burnFactor2RequiredFeeTestCases.append(requiredFeeTestCase(1, 1))
    burnFactor2RequiredFeeTestCases.append(requiredFeeTestCase(2, 1))
    burnFactor2RequiredFeeTestCases.append(requiredFeeTestCase(3, 2))
    burnFactor2RequiredFeeTestCases.append(requiredFeeTestCase(4, 2))
    burnFactor2RequiredFeeTestCases.append(requiredFeeTestCase(5, 3))
    burnFactor2RequiredFeeTestCases.append(requiredFeeTestCase(6, 3))
    burnFactor2RequiredFeeTestCases.append(requiredFeeTestCase(7, 4))
    burnFactor2RequiredFeeTestCases.append(requiredFeeTestCase(998, 499))
    burnFactor2RequiredFeeTestCases.append(requiredFeeTestCase(999, 500))
    burnFactor2RequiredFeeTestCases.append(requiredFeeTestCase(1000, 500))
    burnFactor2RequiredFeeTestCases.append(requiredFeeTestCase(1001, 501))
    cases = burnFactor2RequiredFeeTestCases

    for tc in cases:
        err, fee = skycoin.SKY_fee_RequiredFee(tc.hours, 2)
        assert err == skycoin.SKY_OK
        assert tc.fee == fee
        err, remainingHours = skycoin.SKY_fee_RemainingHours(tc.hours, 2)
        assert err == skycoin.SKY_OK
        assert ((tc.hours - fee) == remainingHours)


class uxInput:
    time = 0
    coins = 0
    hours = 0

    def __init__(self, _time, _coins, _hours):
        self.hours = _hours
        self.time = _time
        self.coins = _coins


class tmpstruct:
    name = ""
    out = []
    ins = []
    headTime = 0
    fee = 0
    err = 0

    def __init__(self):
        self.name = ""
        self.out = []
        self.ins = []
        self.headTime = 0
        self.fee = 0
        self.err = 0


def test_TestTransactionFee():
    headTime = int(1000)
    nextTime = int(headTime + 3600)  # 1 hour later

    cases = []
    #  Test case with one output, one input
    case1 = tmpstruct()
    case1.fee = 5
    case1.headTime = 1000
    case1.out = [5]
    case1.ins.append(uxInput(headTime, 10e6, 10))
    cases.append(case1)

    # Test case with multiple outputs, multiple inputs
    case2 = tmpstruct()
    case2.fee = 0
    case2.headTime = 1000
    case2.out = [5, 7, 3]
    case2.ins.append(uxInput(headTime, int(10e6), 10))
    case2.ins.append(uxInput(headTime, int(10e6), 5))
    cases.append(case2)
    # # Test case with multiple outputs, multiple inputs, and some inputs have more CoinHours once adjusted for HeadTime
    case3 = tmpstruct()
    case3.fee = 8
    case3.headTime = 1000
    case3.out.append(5)
    case3.out.append(10)
    case3.ins.append(uxInput(nextTime, 10e6, 10))
    case3.ins.append(uxInput(nextTime, 8e6, 5))
    # Test case with insufficient coin hours
    case4 = tmpstruct()
    case4.err = skycoin.SKY_ErrTxnInsufficientCoinHours
    case4.out.append(5)
    case4.out.append(10)
    case4.out.append(1)
    case4.ins.append(uxInput(headTime, 10e6, 10))
    case4.ins.append(uxInput(headTime, 8e6, 5))
    # Test case with overflowing input hours
    case5 = tmpstruct()
    case5.err = skycoin.SKY_ERROR
    case5.out.append(0)
    case5.ins.append(uxInput(headTime, 10e6, 10))
    case5.ins.append(uxInput(headTime, 10e6, utils.MaxUint64 - 9))
    case5.headTime = 1000
    # Test case with overflowing output hours
    case6 = tmpstruct()
    case6.err = skycoin.SKY_ERROR
    case6.out.append(0)
    case6.out.append(10)
    case6.out.append(utils.MaxUint64 - 9)
    case6.ins.append(uxInput(headTime, 10e6, 10))
    case6.ins.append(uxInput(headTime, 10e6, 100))
    case6.headTime = 1000
    addr = utils.makeAddress()
    for j in range(len(cases)):
        tc = cases[j]
        tx = utils.makeEmptyTransaction()
        for h in tc.out:
            err = skycoin.SKY_coin_Transaction_PushOutput(tx, addr, 0, h)
            assert err == skycoin.SKY_OK

        inUxs = utils.makeUxArray(len(tc.ins))
        for i in range(len(tc.ins)):
            b = tc.ins[i]
            inUxs[i].Head.Time = b.time
            inUxs[i].Body.Coins = int(b.coins)
            inUxs[i].Body.Hours = int(b.hours)
        err, fee = skycoin.SKY_fee_TransactionFee(tx, int(tc.headTime), inUxs)
        assert err == tc.err
        assert tc.fee == fee
