from .libpy import *

def CreateTransactions():
    return skycoin.SKY_coin_Create_Transactions()

def TransactionsAdd(txns, txn):
    return skycoin.SKY_coin_Transactions_Add(txns, txn)

def NewEmptyBlock(transactions):
    return skycoin.SKY_coin_NewEmptyBlock(transactions)

def GetBlockObject(block):
    return skycoin.SKY_coin_GetBlockObject(block)

def GetBlockBody(block):
    return skycoin.SKY_coin_GetBlockBody(block)

def BlockBodyHash(body, bodyhash):
    return skycoin.SKY_coin_BlockBody_Hash(body, bodyhash)

def NewBlock( p0, p1, p2, p3, p4):
    return skycoin.SKY_coin_NewBlock( p0, p1, p2, p3, p4)

def BlockHashHeader(block, hash1):
    return skycoin.SKY_coin_Block_HashHeader(block, hash1)

def BlockHeaderHash(Head, hash2):
    return skycoin.SKY_coin_BlockHeader_Hash(Head, hash2)

def BlockHashBody(block, hash1):
    return skycoin.SKY_coin_Block_HashBody(block, hash1)

def NewGenesisBlock(address, genCoins, genTime):
    return skycoin.SKY_coin_NewGenesisBlock(address, genCoins, genTime)

def BlockHeaderBytes(head):
    return skycoin.SKY_coin_BlockHeader_Bytes(head)

def TransactionPushOutput(handle, address, p0, p1):
    return skycoin.SKY_coin_Transaction_PushOutput(handle, address, p0, p1)

def UxOut():
    return skycoin.coin__UxOut()

def BlockHeader():
    return skycoin.coin__BlockHeader()

def CreateUnspent(bh, handle, index, ux):
    return skycoin.SKY_coin_CreateUnspent(bh, handle, index, ux)

def CreateUnspents(bh, txn):
    return skycoin.SKY_coin_CreateUnspents(bh, txn)

def TransactionsGetAt(handle, p1):
    return skycoin.SKY_coin_Transactions_GetAt(handle, p1)

def GetTransactionObject(tx1):
    return skycoin.SKY_coin_GetTransactionObject(tx1)

def CreateTransaction():
    return skycoin.SKY_coin_Create_Transaction()

def UxOutHash(ux, h):
    return skycoin.SKY_coin_UxOut_Hash(ux, h)

def TransactionPushInput(handle, h):
    return skycoin.SKY_coin_Transaction_PushInput(handle, h)

def TransactionSignInputs(handle, secKeys):
    return skycoin.SKY_coin_Transaction_SignInputs(handle, secKeys)

def TransactionUpdateHeader(handle):
    return skycoin.SKY_coin_Transaction_UpdateHeader(handle)

def UxBody():
    return skycoin.coin__UxBody()

def UxHead():
    return skycoin.coin__UxHead()

def Transaction():
    return skycoin.coin__Transaction()

def TransactionsLength(handle):
    return skycoin.SKY_coin_Transactions_Length(handle)

def TransactionCopy(handle):
    return skycoin.SKY_coin_Transaction_Copy(handle)

def TransactionVerify(handle2):
    return skycoin.coin_Transaction_Verify(handle2)

def AddUint64(p0, p1):
    return skycoin.SKY_coin_AddUint64(p0, p1)

def Uint64ToInt64(s):
    return skycoin.SKY_coin_Uint64ToInt64(s)

def Int64ToUint64(s):
    return skycoin.SKY_coin_Int64ToUint64(s)

def SHA256():
    return skycoin.cipher_SHA256()

def UxBodyHash(uxb, hashx):
    return skycoin.SKY_coin_UxBody_Hash(uxb, hashx)

def UxOutSnapshotHash(uxo, hn):
    return skycoin.SKY_coin_UxOut_SnapshotHash(uxo, hn) 

def UxOutCoinHours(uxo, now):
    return skycoin.SKY_coin_UxOut_CoinHours(uxo, now)

def UxArrayCoins(uxa):
    return skycoin.SKY_coin_UxArray_Coins(uxa)

def UxArrayCoinHours(uxa, num):
    return skycoin.SKY_coin_UxArray_CoinHours(uxa, num)

def UxArrayHashes(uxa):
    return skycoin.SKY_coin_UxArray_Hashes(uxa)

def UxArrayHasDupes(uxa):
    return skycoin.SKY_coin_UxArray_HasDupes(uxa)

def UxArraySub(uxc, uxa):
    return skycoin.SKY_coin_UxArray_Sub(uxc, uxa)

def UxArrayLess(uxa, p0, p1):
    return skycoin.SKY_coin_UxArray_Less(uxa, p0, p1)

def UxArraySwap(uxa, p0, p1):
    return skycoin.SKY_coin_UxArray_Swap(uxa, p0, p1)

def NewAddressUxOuts(uxa):
    return skycoin.SKY_coin_NewAddressUxOuts(uxa)

def AddressUxOutsKeys(uxH):
    return skycoin.SKY_coin_AddressUxOuts_Keys(uxH)

def AddressUxOutsSet(uxH,uxa_Body_Address,ux_2):
    return skycoin.SKY_coin_AddressUxOuts_Set(uxH,uxa_Body_Address,ux_2)