import skycoin
import tests.utils as utils


def makeNewBlock(uxHash):
    transactions = utils.makeTransactions(1)
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
    return skycoin.SKY_coin_NewBlock(pBlock, 100 + 20, uxHash, transactions, utils.badFeeCalculator)

def addTransactionToBlock(b):
    tx = utils.makeTransaction()
    b.Body.Transactions.append(tx)
    return tx

def test_TestNewBlock():
    pass

    
    


