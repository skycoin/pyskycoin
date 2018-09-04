import skycoin

MaxUint64 = 0xFFFFFFFFFFFFFFFF
Million = 1000000
MaxUint16 = 0xFFFF


def makeAddress():
    p = skycoin.cipher.PubKey()
    s = skycoin.cipher.SecKey()
    assert skycoin.cipher.GenerateKeyPair(p, s) == skycoin.SKY_OK
    a = skycoin.cipher.Address()
    assert skycoin.cipher.AddressFromPubKey(p, a) == skycoin.SKY_OK
    return a


def makeTransactionFromUxOut(ux, s):
    _, handle = skycoin.coin.CreateTransaction()
    _, tx = skycoin.coin.GetTransactionObject(handle)
    h = skycoin.cipher.SHA256()
    err = skycoin.cipher.SecKeyVerify(s)
    assert err == skycoin.SKY_OK
    err = skycoin.coin.UxOutHash(ux, h)
    assert err == skycoin.SKY_OK
    err, _ = skycoin.coin.TransactionPushInput(handle, h)
    assert err == skycoin.SKY_OK
    err = skycoin.coin.TransactionPushOutput(handle, makeAddress(), int(1e6), int(50))
    assert err == skycoin.SKY_OK
    err = skycoin.coin.TransactionPushOutput(handle, makeAddress(), int(5e6), int(50))
    assert err == skycoin.SKY_OK
    secKeys = []
    secKeys.append(s)
    err = skycoin.coin.TransactionSignInputs(handle, secKeys)
    assert err == skycoin.SKY_OK
    err = skycoin.coin.TransactionUpdateHeader(handle)
    assert err == skycoin.SKY_OK
    return handle, tx


def makeUxBodyWithSecret():
    p = skycoin.cipher.PubKey()
    s = skycoin.cipher.SecKey()
    assert skycoin.cipher.GenerateKeyPair(p, s) == skycoin.SKY_OK
    uxb = skycoin.coin.UxBody()
    err, b = skycoin.cipher.RandByte(128)
    assert err == skycoin.SKY_OK
    h = skycoin.cipher.SHA256()
    assert skycoin.cipher.SumSHA256(b, h) == skycoin.SKY_OK
    assert h.assignTo(uxb.SrcTransaction) == None
    a = skycoin.cipher.Address()
    assert skycoin.cipher.AddressFromPubKey(p, a) == skycoin.SKY_OK
    uxb.Address = a
    uxb.Coins = int(1e6)
    uxb.Hours = int(100)
    return uxb, s


def makeUxOutWithSecret():
    body, sec = makeUxBodyWithSecret()
    uxo = skycoin.coin.UxOut()
    uxh = skycoin.coin.UxHead()
    uxh.Time = 100
    uxh.BkSeq = 2
    uxo.Head = uxh
    uxo.Body = body
    return uxo, sec


def makeTransaction():
    ux, s = makeUxOutWithSecret()
    return makeTransactionFromUxOut(ux, s)


def makeTransactions(n):
    _, handle = skycoin.coin.CreateTransactions()
    for _ in range(n):
        thandle, _ = makeTransaction()
        err = skycoin.coin.TransactionsAdd(handle, thandle)
        assert err == skycoin.SKY_OK
    err, count = skycoin.coin.TransactionsLength(handle)
    assert err == skycoin.SKY_OK
    assert count == n
    return handle


def copyTransaction(handle):
    err, handle2 = skycoin.coin.TransactionCopy(handle)
    assert err == skycoin.SKY_OK
    err = skycoin.coin.TransactionVerify(handle2)
    assert err == skycoin.SKY_OK
    err, ptx = skycoin.coin.GetTransactionObject(handle2)
    assert err == skycoin.SKY_OK
    return handle2, ptx


def makeEmptyTransaction():
    _, handle = skycoin.coin.CreateTransaction()
    return handle


def makeUxOut():
    pOut, _ = makeUxOutWithSecret()
    return pOut


def equalTransactions(handle1, handle2):
    err, size1 = skycoin.coin.TransactionsLength(handle1)
    assert err == skycoin.SKY_OK
    err, size2 = skycoin.coin.TransactionsLength(handle2)
    assert err == skycoin.SKY_OK
    if size1 != size2:
        return 1

    for i in range(int(size1 - 1)):
        err, tx1 = skycoin.coin.TransactionsGetAt(handle1, i)
        assert err == skycoin.SKY_OK
        err, tx2 = skycoin.coin.TransactionsGetAt(handle2, i)
        assert err == skycoin.SKY_OK
        err, tx1_obj = skycoin.coin.GetTransactionObject(tx1)
        assert err == skycoin.SKY_OK
        err, tx2_obj = skycoin.coin.GetTransactionObject(tx2)
        assert err == skycoin.SKY_OK
        assert tx1_obj == tx2_obj
        i += 1

    return 0


def badFeeCalculator(transaction):
    return skycoin.SKY_ERROR, 0


def calc(transaction):
    return 0, 1


def feeCalc(transaction):
    return skycoin.SKY_OK, 0


def overflowCalc(transaction):
    return 0, MaxUint64
    return 1, 0


def fix121FeeCalculator(transaction):
    return skycoin.SKY_OK, 121


def makeUxBody():
    return makeUxBodyWithSecret()[0]


def make_UxOut():
    return makeUxOutWithSecret()[0]


def makeUxArray(n):
    lista = []
    for _ in range(n):
        lista.append(make_UxOut())
    return lista


def err_CoinHours_Overflow(p0):
    if MaxUint16 < p0:
        return 67108864


def RandSHA256():
    err, sha = skycoin.cipher.RandByte(128)
    assert err == skycoin.SKY_OK
    sh = skycoin.cipher.SHA256()
    err = skycoin.cipher.SumSHA256(sha, sh)
    assert err == skycoin.SKY_OK
    return sh


def makeKeysAndAddress():
    ppubkey = skycoin.cipher.PubKey()
    pseckey = skycoin.cipher.SecKey()
    err = skycoin.cipher.GenerateKeyPair(ppubkey, pseckey)
    assert err == skycoin.SKY_OK
    paddress = skycoin.cipher.Address()
    err = skycoin.cipher.AddressFromPubKey(ppubkey, paddress)
    assert err == skycoin.SKY_OK
    return err, ppubkey, pseckey, paddress