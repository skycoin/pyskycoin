import skycoin
import tests.utils as utils
import time


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
    err, pBlockHeader = skycoin.SKY_coin_Block_GetBlockHeader(block)
    assert err == skycoin.SKY_OK
    err = skycoin.SKY_coin_BlockHeader_SetTime(pBlockHeader, 100)
    assert err == skycoin.SKY_OK
    err = skycoin.SKY_coin_BlockHeader_SetBkSeq(pBlockHeader, 0)
    assert err == skycoin.SKY_OK
    err = skycoin.SKY_coin_BlockHeader_SetVersion(pBlockHeader, 0x02)
    assert err == skycoin.SKY_OK
    err = skycoin.SKY_coin_BlockHeader_SetFee(pBlockHeader, 10)
    assert err == skycoin.SKY_OK
    err, body = skycoin.SKY_coin_GetBlockBody(block)
    assert err == skycoin.SKY_OK
    return skycoin.SKY_coin_NewBlock(block, int(100 + 200), uxHash, transactions, utils.feeCalc)


def addTransactionToBlock(b):
    tx = utils.makeTransaction()
    b.Body.Transactions.append(tx)
    return tx


def test_TestNewBlock():
    txns = makeTestTransactions()
    err, block = skycoin.SKY_coin_NewEmptyBlock(txns)
    assert err == skycoin.SKY_OK
    err, pBlock = skycoin.SKY_coin_GetBlockObject(block)
    assert err == skycoin.SKY_OK
    pBlock.Head.Version = 0x02
    pBlock.Head.Time = 100
    pBlock.Head.BkSeq = 98
    uxHash = utils.RandSHA256()
    err, _ = skycoin.SKY_coin_NewBlock(
        block, 133, uxHash, txns, utils.badFeeCalculator)
    assert err != skycoin.SKY_OK
    err, txns1 = skycoin.SKY_coin_Create_Transactions()
    assert err == skycoin.SKY_OK
    err, _ = skycoin.SKY_coin_NewBlock(
        block, 133, uxHash, txns1, utils.feeCalc)
    assert err != skycoin.SKY_OK
    fee = int(121)
    currentTime = int(133)
    err, b = skycoin.SKY_coin_NewBlock(
        block, currentTime, uxHash, txns, utils.fix121FeeCalculator)
    assert err == skycoin.SKY_OK
    err, pBlock = skycoin.SKY_coin_GetBlockObject(b)
    assert err == skycoin.SKY_OK


def test_TestBlockHashHeader():
    uxHash = utils.RandSHA256()
    err, block = makeNewBlock(uxHash)
    assert err == skycoin.SKY_OK
    err, pBlock = skycoin.SKY_coin_GetBlockObject(block)
    assert err == skycoin.SKY_OK
    hash1 = skycoin.cipher_SHA256()
    hash2 = skycoin.cipher_SHA256()
    err = skycoin.SKY_coin_Block_HashHeader(block, hash1)
    assert err == skycoin.SKY_OK
    err, blockheader = skycoin.SKY_coin_Block_GetBlockHeader(block)
    err = skycoin.SKY_coin_BlockHeader_Hash(blockheader, hash2)
    assert err == skycoin.SKY_OK
    assert hash1.toStr() == hash2.toStr()
    hash2 = skycoin.cipher_SHA256()
    assert hash1 != hash2


def test_TestBlockHashBody():
    uxHash = utils.RandSHA256()
    err, block = makeNewBlock(uxHash)
    assert err == skycoin.SKY_OK
    err, pBlock = skycoin.SKY_coin_GetBlockObject(block)
    assert err == skycoin.SKY_OK

    hash1 = skycoin.cipher_SHA256()
    hash2 = skycoin.cipher_SHA256()
    err = skycoin.SKY_coin_Block_HashBody(block, hash1)
    assert err == skycoin.SKY_OK
    err, blockBody = skycoin.SKY_coin_GetBlockBody(block)
    assert err == skycoin.SKY_OK
    err = skycoin.SKY_coin_BlockBody_Hash(blockBody, hash2)
    assert err == skycoin.SKY_OK
    assert hash1 == hash2


def test_TestNewGenesisBlock():
    pubkey = skycoin.cipher_PubKey()
    seckey = skycoin.cipher_SecKey()
    genTime = 1000
    genCoins = int(1000 * 1000 * 1000)
    genCoinHours = int(1000 * 1000)

    err, pubkey, seckey, address = utils.makeKeysAndAddress()
    assert err == skycoin.SKY_OK
    err, block = skycoin.SKY_coin_NewGenesisBlock(address, genCoins, genTime)
    assert err == skycoin.SKY_OK
    err, pBlock = skycoin.SKY_coin_GetBlockObject(block)
    assert err == skycoin.SKY_OK

    nullHash = skycoin.cipher_SHA256()
    err, pHead = skycoin.SKY_coin_BlockHeader_Bytes(pBlock.Head)
    assert err == skycoin.SKY_OK
    assert nullHash.compareToString(str(pHead))
    assert genTime == pBlock.Head.Time
    assert 0 == pBlock.Head.BkSeq
    assert 0 == pBlock.Head.Version
    assert 0 == pBlock.Head.Fee


class testcase:
    index = 0
    failure = 0


def test_TestCreateUnspent():
    err, pubkey, seckey, address = utils.makeKeysAndAddress()
    assert err == skycoin.SKY_OK
    hash1 = skycoin.cipher_SHA256()
    handle = utils.makeEmptyTransaction()
    err = skycoin.SKY_coin_Transaction_PushOutput(
        handle, address, 11000000, 255)
    assert err == skycoin.SKY_OK
    bh = skycoin.coin__BlockHeader()
    bh.Time = 0
    bh.BkSeq = 1
    t = []
    tc1 = testcase()
    t.append(tc1)
    tc2 = testcase()
    tc2.index = 10
    tc2.failure = skycoin.SKY_ERROR
    t.append(tc2)
    ux = skycoin.coin__UxOut()
    tests_count = len(t)
    for i in range(tests_count):
        err = skycoin.SKY_coin_CreateUnspent(bh, handle, t[i].index, ux)
        if t[i].failure == skycoin.SKY_ERROR:
            pass
        assert bh.Time == ux.Head.Time
        assert bh.BkSeq == ux.Head.BkSeq


def test_TestCreateUnspents():
    err, pubkey, seckey, address = utils.makeKeysAndAddress()
    assert err == skycoin.SKY_OK
    hash1 = skycoin.cipher_SHA256()
    txn = utils.makeEmptyTransaction()
    err = skycoin.SKY_coin_Transaction_PushOutput(
        txn, address, int(11e6), int(255))
    assert err == skycoin.SKY_OK
    bh = skycoin.coin__BlockHeader()
    bh.Time = 0
    bh.BkSeq = 1
    err, uxouts = skycoin.SKY_coin_CreateUnspents(bh, txn)
    assert err == skycoin.SKY_OK
    assert err == skycoin.SKY_OK
    assert len(uxouts) == 1
