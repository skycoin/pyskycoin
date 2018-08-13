import skycoin
import tests.utils


def test_makeTestTransactions():
    err, transactions = skycoin.SKY_coin_Create_Transactions()
    assert err == skycoin.SKY_OK
    err, transaction = skycoin.SKY_coin_Create_Transaction()
    assert err == skycoin.SKY_OK
    assert skycoin.SKY_coin_Transactions_Add(
        transactions, transaction) == skycoin.SKY_OK
    return transactions


def test_makeNewBlock():
    transactions = test_makeTestTransactions()
    err, block = skycoin.SKY_coin_NewEmptyBlock(transactions)
    assert err == skycoin.SKY_OK
    err, pBlock = skycoin.SKY_coin_GetBlockObject(block)
    assert err == skycoin.SKY_OK
    pBlock.Head.Version = 0x02
    pBlock.Head.Time = 100
    pBlock.Head.BkSeq = 0
    pBlock.Head.Fee = 10
    err, body = skycoin.SKY_coin_GetBlockBody(block)
    assert err == skycoin.SKY_OK
    bodyhash = skycoin.cipher_SHA256()
    err = skycoin.SKY_coin_BlockBody_Hash(body, bodyhash)
    assert err == skycoin.SKY_OK


