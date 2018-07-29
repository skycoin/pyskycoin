import skycoin
from tests.utils.skyerror import error


def test_makeTestTransactions():
    err, transactions = skycoin.SKY_coin_Create_Transactions()
    assert err == error["SKY_OK"]
    err, transaction = skycoin.SKY_coin_Create_Transaction()
    assert err == error["SKY_OK"]
    assert skycoin.SKY_coin_Transactions_Add(
        transactions, transaction) == error["SKY_OK"]
    return transactions


def test_makeNewBlock():
    transactions = test_makeTestTransactions()
    err, block = skycoin.SKY_coin_NewEmptyBlock(transactions)
    assert err == error["SKY_OK"]
    err, pBlock = skycoin.SKY_coin_GetBlockObject(block)
    assert err == error["SKY_OK"]
    pBlock.Head.Version = 0x02
    pBlock.Head.Time = 100
    pBlock.Head.BkSeq = 0
    pBlock.Head.Fee = 10
    err, body = skycoin.SKY_coin_GetBlockBody(block)
    assert err == error["SKY_OK"]
    bodyhash = skycoin.cipher_SHA256()
    err = skycoin.SKY_coin_BlockBody_Hash(body, bodyhash)
    assert err == error["SKY_OK"]


