import skycoin
from tests.utils.skyerror import error
import sys


def makeAddress():
    p = skycoin.cipher_PubKey()
    s = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(p, s)
    a = skycoin.cipher__Address()
    skycoin.SKY_cipher_AddressFromPubKey(p, a)
    return a


def makeTransactionFromUxOut(ux, s):
    _, handle = skycoin.SKY_coin_Create_Transaction()
    _, tx = skycoin.SKY_coin_Get_Transaction_Object(handle)
    h = skycoin.cipher_SHA256()
    skycoin.SKY_coin_UxOut_Hash(ux, h)
    skycoin.SKY_coin_Transaction_PushInput(tx, h)
    skycoin.SKY_coin_Transaction_PushOutput(tx, makeAddress(), 1e6, 50)
    skycoin.SKY_coin_Transaction_PushOutput(tx, makeAddress(), 5e6, 50)
    skycoin.SKY_coin_Transaction_SignInputs(tx, s)
    skycoin.SKY_coin_Transaction_UpdateHeader(tx)
    return tx


def makeUxBodyWithSecret():
    p = skycoin.cipher_PubKey()
    s = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(p, s)
    uxb = skycoin.coin__UxBody()
    _, b = skycoin.SKY_cipher_RandByte(128)
    h = skycoin.cipher_SHA256()
    err =skycoin.SKY_cipher_SumSHA256(b, h)
    uxb.SrcTransaction = h
    a = skycoin.cipher__Address()
    skycoin.SKY_cipher_AddressFromPubKey(p, a)
    uxb.Address = a
    uxb.Coins = 1e6
    uxb.Hours = 100
    return uxb, s


def makeUxOutWithSecret():
    body, sec = makeUxBodyWithSecret()
    uxo = skycoin.coin__UxOut()
    uxh = skycoin.coin__UxHead()
    uxh.Time = 100
    uxh.BkSeq = 2
    uxo.Head = uxh
    uxo.Body = body
    return uxo, sec


def makeTransaction():
    ux, s = makeUxOutWithSecret()
    return makeTransactionFromUxOut(ux, s)


def makeTransactions(n):
    _, handle = skycoin.SKY_coin_Create_Transactions()
    for i in range(n):
        thandle = makeTransaction()
        skycoin.SKY_coin_Transactions_Add(handle, thandle)
    return handle


def copyTransaction(handle1, handle2):
    assert skycoin.SKY_coin_Transaction_Copy(
        handle1, handle2) == error["SKY_OK"]
    _, txo = skycoin.SKY_coin_Get_Transaction_Object(handle2)
    return txo
