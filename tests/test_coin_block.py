import skycoin
import tests.utils as utils


def makeTestTransactions():
    err, txns = skycoin.coin.CreateTransactions()
    assert err == skycoin.SKY_OK
    txn = utils.makeEmptyTransaction()
    err = skycoin.coin.TransactionsAdd(txns, txn)
    assert err == skycoin.SKY_OK
    return txns


def makeNewBlock(uxHash):
    bodyhash = skycoin.cipher.SHA256()
    transactions = makeTestTransactions()
    err, block = skycoin.coin.NewEmptyBlock(transactions)
    assert err == skycoin.SKY_OK
    err, pBlock = skycoin.coin.GetBlockObject(block)
    assert err == skycoin.SKY_OK
    pBlock.Head.Version = 0x02
    pBlock.Head.Time = 100
    pBlock.Head.BkSeq = 0
    pBlock.Head.Fee = 10
    err, body = skycoin.coin.GetBlockBody(block)
    assert err == skycoin.SKY_OK
    err = skycoin.coin.BlockBodyHash(body, bodyhash)
    assert err == skycoin.SKY_OK
    return skycoin.coin.NewBlock(block, int(100 + 200), uxHash, transactions, utils.feeCalc)


def addTransactionToBlock(b):
    tx = utils.makeTransaction()
    b.Body.Transactions.append(tx)
    return tx


def test_TestNewBlock():
    txns = makeTestTransactions()
    err, block = skycoin.coin.NewEmptyBlock(txns)
    assert err == skycoin.SKY_OK
    err, pBlock = skycoin.coin.GetBlockObject(block)
    assert err == skycoin.SKY_OK
    pBlock.Head.Version = 0x02
    pBlock.Head.Time = 100
    pBlock.Head.BkSeq = 98
    uxHash = utils.RandSHA256()
    err, _ = skycoin.coin.NewBlock(block, 133, uxHash, txns, utils.badFeeCalculator)
    assert err == skycoin.SKY_ERROR
    err, txns1 = skycoin.coin.CreateTransactions()
    assert err == skycoin.SKY_OK
    err, _ = skycoin.coin.NewBlock(block, 133, uxHash, txns1, utils.feeCalc)
    assert err == skycoin.SKY_ERROR
    currentTime = int(133)
    err, b = skycoin.coin.NewBlock(block, currentTime, uxHash, txns, utils.fix121FeeCalculator)
    assert err == skycoin.SKY_OK
    err, pBlock = skycoin.coin.GetBlockObject(b)
    assert err == skycoin.SKY_OK


def test_TestBlockHashHeader():
    uxHash = utils.RandSHA256()
    err, block = makeNewBlock(uxHash)
    assert err == skycoin.SKY_OK
    err, pBlock = skycoin.coin.GetBlockObject(block)
    assert err == skycoin.SKY_OK
    hash1 = skycoin.cipher.SHA256()
    hash2 = skycoin.cipher.SHA256()
    err = skycoin.coin.BlockHashHeader(block, hash1)
    assert err == skycoin.SKY_OK
    err = skycoin.coin.BlockHeaderHash(pBlock.Head, hash2)
    assert err == skycoin.SKY_OK
    assert hash1.toStr() == hash2.toStr()
    hash2 = skycoin.cipher.SHA256()
    assert hash1 != hash2


def test_TestBlockHashBody():
    uxHash = utils.RandSHA256()
    err, block = makeNewBlock(uxHash)
    assert err == skycoin.SKY_OK
    err, pBlock = skycoin.coin.GetBlockObject(block)
    assert err == skycoin.SKY_OK

    hash1 = skycoin.cipher.SHA256()
    hash2 = skycoin.cipher.SHA256()
    err = skycoin.coin.BlockHashBody(block, hash1)
    assert err == skycoin.SKY_OK
    err, blockBody = skycoin.coin.GetBlockBody(block)
    assert err == skycoin.SKY_OK
    err = skycoin.coin.BlockBodyHash(blockBody, hash2)
    assert err == skycoin.SKY_OK
    assert hash1 == hash2


def test_TestNewGenesisBlock():
    pubkey = skycoin.cipher.PubKey()
    seckey = skycoin.cipher.SecKey()
    genTime = 1000
    genCoins = int(1000 * 1000 * 1000)
    genCoinHours = int(1000 * 1000)
    err , pubkey, seckey, address = utils.makeKeysAndAddress()
    assert err == skycoin.SKY_OK
    err , block = skycoin.coin.NewGenesisBlock(address, genCoins, genTime)
    assert err == skycoin.SKY_OK
    err, pBlock = skycoin.coin.GetBlockObject(block)
    assert err == skycoin.SKY_OK

    nullHash = skycoin.cipher.SHA256()
    err, pHead = skycoin.coin.BlockHeaderBytes(pBlock.Head)
    assert err == skycoin.SKY_OK
    assert nullHash.compareToString(str(pHead))
    assert genTime == pBlock.Head.Time
    assert 0 == pBlock.Head.BkSeq
    assert 0 == pBlock.Head.Version
    assert 0 == pBlock.Head.Fee


class testcase:
    index = 0
    failure = skycoin.SKY_OK


def test_TestCreateUnspent():
    err, pubkey, seckey, address = utils.makeKeysAndAddress()
    assert err == skycoin.SKY_OK
    hash1 = skycoin.cipher.SHA256()
    handle = utils.makeEmptyTransaction()
    err = skycoin.coin.TransactionPushOutput(handle, address, 11000000, 255)
    assert err == skycoin.SKY_OK
    bh = skycoin.coin.BlockHeader()
    bh.Time = 0
    bh.BkSeq = 1
    t = []
    tc1 = testcase()
    t.append(tc1)
    tc2 = testcase()
    tc2.index = 10
    tc2.failure = skycoin.SKY_ERROR
    t.append(tc2)
    ux = skycoin.coin.UxOut()
    tests_count = len(t)
    for i in range(tests_count):
        err = skycoin.coin.CreateUnspent(bh, handle, t[i].index, ux)
        if t[i].failure == skycoin.SKY_ERROR :
            pass
        assert bh.Time == ux.Head.Time
        assert bh.BkSeq == ux.Head.BkSeq


def test_TestCreateUnspents():
    err, pubkey, seckey, address = utils.makeKeysAndAddress()
    assert err == skycoin.SKY_OK
    hash1 = skycoin.cipher.SHA256()
    txn = utils.makeEmptyTransaction()
    err = skycoin.coin.TransactionPushOutput(txn, address, int(11e6), int(255))
    assert err == skycoin.SKY_OK
    bh = skycoin.coin.BlockHeader()
    bh.Time = 0
    bh.BkSeq = 1
    err , uxouts = skycoin.coin.CreateUnspents(bh, txn)
    assert err == skycoin.SKY_OK
    assert err == skycoin.SKY_OK
    assert len(uxouts) == 1

