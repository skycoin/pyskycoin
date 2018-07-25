import skycoin
from tests.utils.skyerror import error


def test_makeAddress():
    p = skycoin.cipher_PubKey()
    s = skycoin.cipher_SecKey()
    assert skycoin.SKY_cipher_GenerateKeyPair(p, s) == error["SKY_OK"]
    a = skycoin.cipher__Address()
    assert skycoin.SKY_cipher_AddressFromPubKey(p, a) == error["SKY_OK"]
    return a


def test_makeTransactionFromUxOut(ux, s):
    _, handle = skycoin.SKY_coin_Create_Transaction()
    h = skycoin.cipher_SHA256()
    assert skycoin.SKY_cipher_SecKey_Verify(s) == 0
    assert skycoin.SKY_coin_UxOut_Hash(ux, h) == error["SKY_OK"]
    err, r = skycoin.SKY_coin_Transaction_PushInput(handle, h)
    assert err == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_PushOutput(
        handle, test_makeAddress(), int(1e6), int(50)) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_PushOutput(
        handle, test_makeAddress(), int(5e6), int(50)) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_SignInputs(handle ) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_UpdateHeader(handle) == error["SKY_OK"]
    return handle


def test_makeUxBodyWithSecret():
    p = skycoin.cipher_PubKey()
    s = skycoin.cipher_SecKey()
    assert skycoin.SKY_cipher_GenerateKeyPair(p, s) == error["SKY_OK"]
    uxb = skycoin.coin__UxBody()
    err, b = skycoin.SKY_cipher_RandByte(128)
    assert err == error["SKY_OK"]
    h = skycoin.cipher_SHA256()
    assert skycoin.SKY_cipher_SumSHA256(b, h) == error["SKY_OK"]
    assert h.assignTo(uxb.SrcTransaction) == None
    a = skycoin.cipher__Address()
    assert skycoin.SKY_cipher_AddressFromPubKey(p, a) == error["SKY_OK"]
    uxb.Address = a
    uxb.Coins = int(1e6)
    uxb.Hours = int(100)
    return uxb, s


def makeUxOutWithSecret():
    body, sec = test_makeUxBodyWithSecret()
    uxo = skycoin.coin__UxOut()
    uxh = skycoin.coin__UxHead()
    uxh.Time = 100
    uxh.BkSeq = 2
    uxo.Head = uxh
    uxo.Body = body
    return uxo, sec


def makeTransaction():
    ux, s = makeUxOutWithSecret()
    return test_makeTransactionFromUxOut(ux, s)


def makeTransactions(n):
    _, handle = skycoin.SKY_coin_Create_Transactions()
    for i in range(n):
        thandle = makeTransaction()
        assert skycoin.SKY_coin_Transactions_Add(
            handle, thandle) == error["SKY_OK"]
    return handle


def copyTransaction(handle1, handle2):
    assert skycoin.SKY_coin_Transaction_Copy(
        handle1, handle2) == error["SKY_OK"]
    # _, txo = skycoin.SKY_coin_Get_Transaction_Object(handle2)
    return handle2
