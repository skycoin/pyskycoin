import skycoin
import tests.utils as utils


def makeTestTransactions():
    err, txns = skycoin.SKY_coin_Create_Transactions()
    assert err == skycoin.SKY_OK
    txn = utils.makeEmptyTransaction()
    assert skycoin.SKY_coin_Transactions_Add(txns, txn) == skycoin.SKY_OK
    return txns


def makeNewBlock(uxHash):
    transactions = makeTestTransactions()
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
    return skycoin.SKY_coin_NewBlock(block, 100 + 20, uxHash, transactions, utils.feeCalc)


def addTransactionToBlock(b):
    tx = utils.makeTransaction()
    b.Body.Transactions.append(tx)
    return tx


def test_TestNewBlock():
    txns = utils.makeTransactions(1)
    err, block = skycoin.SKY_coin_NewEmptyBlock(txns)
    assert err == skycoin.SKY_OK
    err, pBlock = skycoin.SKY_coin_GetBlockObject(block)
    assert err == skycoin.SKY_OK
    pBlock.Head.Version = 0x02
    pBlock.Head.Time = 100
    pBlock.Head.BkSeq = 98
    uxHash = utils.RandSHA256()
    err, _ = skycoin.SKY_coin_NewBlock(block, 133, uxHash, txns, utils.badFeeCalculator)
    assert err == skycoin.SKY_ERROR
    err, txns1 = skycoin.SKY_coin_Create_Transactions()
    assert err == skycoin.SKY_OK
    err, _ = skycoin.SKY_coin_NewBlock(block, 133, uxHash, txns1, utils.feeCalc)
    assert err == skycoin.SKY_ERROR
    fee = int(121)
    currentTime = int(133)
    err, b = skycoin.SKY_coin_NewBlock(block, currentTime, uxHash, txns, utils.fix121FeeCalculator)
    err, pBlock = skycoin.SKY_coin_GetBlockObject(b)
    assert err == skycoin.SKY_OK

def test_TestBlockHashHeader():
    uxHash= utils.RandSHA256()
    err, b = makeNewBlock(uxHash)
    assert err == skycoin.SKY_OK
    