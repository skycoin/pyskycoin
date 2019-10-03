import skycoin

MaxUint64 = 0xFFFFFFFFFFFFFFFF
Million = 1000000
MaxUint16 = 0xFFFF


def makecipher_PubKeyAndcipher_SecKey():
    p = skycoin.cipher_PubKey()
    s = skycoin.cipher_SecKey()
    err = skycoin.SKY_cipher_GenerateKeyPair(p, s)
    return p, s


def makeAddress():
    p, s = makecipher_PubKeyAndcipher_SecKey()
    a = skycoin.cipher__Address()
    assert skycoin.SKY_cipher_AddressFromPubKey(p, a) == skycoin.SKY_OK
    return a


def makeTransactionFromUxOut(ux, s):
    _, handle = skycoin.SKY_coin_Create_Transaction()
    _, tx = skycoin.SKY_coin_GetTransactionObject(handle)
    h = skycoin.cipher_SHA256()
    assert skycoin.SKY_cipher_SecKey_Verify(s) == skycoin.SKY_OK
    assert skycoin.SKY_coin_UxOut_Hash(ux, h) == skycoin.SKY_OK
    r = skycoin.SKY_coin_Transaction_PushInput(handle, h)
    assert skycoin.SKY_coin_Transaction_PushOutput(
        handle, makeAddress(), int(1e6), int(50)) == skycoin.SKY_OK
    assert skycoin.SKY_coin_Transaction_PushOutput(
        handle, makeAddress(), int(5e6), int(50)) == skycoin.SKY_OK
    secKeys = []
    secKeys.append(s)
    assert skycoin.SKY_coin_Transaction_SignInputs(
        handle, secKeys) == skycoin.SKY_OK
    assert skycoin.SKY_coin_Transaction_UpdateHeader(handle) == skycoin.SKY_OK
    return handle, tx


def makeUxBodyWithSecret():
    p = skycoin.cipher_PubKey()
    s = skycoin.cipher_SecKey()
    assert skycoin.SKY_cipher_GenerateKeyPair(p, s) == skycoin.SKY_OK
    uxb = skycoin.coin__UxBody()
    err, b = skycoin.SKY_cipher_RandByte(128)
    assert err == skycoin.SKY_OK
    h = skycoin.cipher_SHA256()
    assert skycoin.SKY_cipher_SumSHA256(b, h) == skycoin.SKY_OK
    assert h.assignTo(uxb.SrcTransaction) == None
    a = skycoin.cipher__Address()
    assert skycoin.SKY_cipher_AddressFromPubKey(p, a) == skycoin.SKY_OK
    uxb.Address = a
    uxb.Coins = int(1e6)
    uxb.Hours = int(100)
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
        thandle, _ = makeTransaction()
        assert skycoin.SKY_coin_Transactions_Add(
            handle, thandle) == skycoin.SKY_OK
    err, count = skycoin.SKY_coin_Transactions_Length(handle)
    assert err == skycoin.SKY_OK
    assert count == n
    return handle


def copyTransaction(handle):
    handle2 = skycoin.coin__Transaction()
    err, handle2 = skycoin.SKY_coin_Transaction_Copy(
        handle)
    assert err == skycoin.SKY_OK
    assert skycoin.SKY_coin_Transaction_Verify(handle2) == skycoin.SKY_OK
    err, ptx = skycoin.SKY_coin_GetTransactionObject(handle2)
    assert err == skycoin.SKY_OK
    return handle2, ptx


def makeEmptyTransaction():
    _, handle = skycoin.SKY_coin_Create_Transaction()
    return handle


def makeUxOut():
    pOut, _ = makeUxOutWithSecret()
    return pOut


def equalTransactions(handle1, handle2):
    err, size1 = skycoin.SKY_coin_Transactions_Length(handle1)
    assert err == skycoin.SKY_OK
    err, size2 = skycoin.SKY_coin_Transactions_Length(handle2)
    assert err == skycoin.SKY_OK
    if size1 != size2:
        return 1

    for i in range(int(size1 - 1)):
        err, tx1 = skycoin.SKY_coin_Transactions_GetAt(handle1, i)
        assert err == skycoin.SKY_OK
        err, tx2 = skycoin.SKY_coin_Transactions_GetAt(handle2, i)
        assert err == skycoin.SKY_OK
        err, tx1_obj = skycoin.SKY_coin_GetTransactionObject(tx1)
        assert err == skycoin.SKY_OK
        err, tx2_obj = skycoin.SKY_coin_GetTransactionObject(tx2)
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
    err, sha = skycoin.SKY_cipher_RandByte(128)
    assert err == skycoin.SKY_OK
    sh = skycoin.cipher_SHA256()
    err = skycoin.SKY_cipher_SumSHA256(sha, sh)
    assert err == skycoin.SKY_OK
    return sh


def makeKeysAndAddress():
    ppubkey = skycoin.cipher_PubKey()
    pseckey = skycoin.cipher_SecKey()
    err = skycoin.SKY_cipher_GenerateKeyPair(ppubkey, pseckey)
    assert err == skycoin.SKY_OK
    paddress = skycoin.cipher__Address()
    err = skycoin.SKY_cipher_AddressFromPubKey(ppubkey, paddress)
    assert err == skycoin.SKY_OK
    return err, ppubkey, pseckey, paddress


def isPrivateKeyEq(handle1, handle2):
    err, Version1 = skycoin.SKY_bip32_PrivateKey_GetVersion(handle1)
    assert err == skycoin.SKY_OK
    err, Version2 = skycoin.SKY_bip32_PrivateKey_GetVersion(handle2)
    assert err == skycoin.SKY_OK
    if(Version1 != Version2):
        print("Version not equal\n")
        return 0

    err, Depth1 = skycoin.SKY_bip32_PrivateKey_GetDepth(handle1)
    assert err == skycoin.SKY_OK
    err, Depth2 = skycoin.SKY_bip32_PrivateKey_GetDepth(handle2)
    assert err == skycoin.SKY_OK
    if(Depth1 != Depth2):

        print("Depth not equal ,", Depth1, "and ", Depth2, "\n")
        return 0

    err, ParentFingerprint1 = skycoin.SKY_bip32_PrivateKey_GetParentFingerprint(
        handle1)
    assert err == skycoin.SKY_OK
    err, ParentFingerprint2 = skycoin.SKY_bip32_PrivateKey_GetParentFingerprint(
        handle2)
    assert err == skycoin.SKY_OK
    if(ParentFingerprint1 != ParentFingerprint2):
        print("ParentFingerprint not equal \n")
        return 0

    err, childNumber1 = skycoin.SKY_bip32_PrivateKey_ChildNumber(handle1)
    assert err == skycoin.SKY_OK
    err, childNumber2 = skycoin.SKY_bip32_PrivateKey_ChildNumber(handle2)
    assert err == skycoin.SKY_OK
    if(childNumber1 != childNumber2):
        print("childNumber not equal\n")
        return 0

    err, ChainCode1 = skycoin.SKY_bip32_PrivateKey_GetChainCode(handle1)
    assert err == skycoin.SKY_OK
    err, ChainCode2 = skycoin.SKY_bip32_PrivateKey_GetChainCode(handle2)
    assert err == skycoin.SKY_OK
    if(ChainCode1 != ChainCode2):
        print("ChainCode not equal\n")
        return 0

    err, Key1 = skycoin.SKY_bip32_PrivateKey_GetKey(handle1)
    assert err == skycoin.SKY_OK
    err, Key2 = skycoin.SKY_bip32_PrivateKey_GetKey(handle2)
    assert err == skycoin.SKY_OK
    if(Key1 != Key2):
        print("Key not equal\n")
        return 0

    return 1


def isPublicKeyEq(handle1, handle2):
    err, Version1 = skycoin.SKY_bip32_PublicKey_GetVersion(handle1)
    assert err == skycoin.SKY_OK
    err, Version2 = skycoin.SKY_bip32_PublicKey_GetVersion(handle2)
    assert err == skycoin.SKY_OK
    if(Version1 != Version2):
        print("Version not equal\n")
        return 0

    err, Depth1 = skycoin.SKY_bip32_PublicKey_GetDepth(handle1)
    assert err == skycoin.SKY_OK
    err, Depth2 = skycoin.SKY_bip32_PublicKey_GetDepth(handle2)
    assert err == skycoin.SKY_OK
    if(Depth1 != Depth2):
        print("Depth not equal \n")
        return 0

    err, ParentFingerprint1 = skycoin.SKY_bip32_PublicKey_GetParentFingerprint(
        handle1)
    assert err == skycoin.SKY_OK
    err, ParentFingerprint2 = skycoin.SKY_bip32_PublicKey_GetParentFingerprint(
        handle2)
    assert err == skycoin.SKY_OK
    if(ParentFingerprint1 != ParentFingerprint2):
        print("ParentFingerprint not equal \n")
        return 0

    err, childNumber1 = skycoin.SKY_bip32_PublicKey_ChildNumber(handle1)
    assert err == skycoin.SKY_OK
    err, childNumber2 = skycoin.SKY_bip32_PublicKey_ChildNumber(handle2)
    assert err == skycoin.SKY_OK
    if(childNumber1 != childNumber2):
        print("childNumber not equal\n")
        return 0

    err, ChainCode1 = skycoin.SKY_bip32_PublicKey_GetChainCode(handle1)
    assert err == skycoin.SKY_OK
    err, ChainCode2 = skycoin.SKY_bip32_PublicKey_GetChainCode(handle2)
    assert err == skycoin.SKY_OK
    if(ChainCode1 != ChainCode2):
        print("ChainCode not equal\n")
        return 0

    err, Key1 = skycoin.SKY_bip32_PublicKey_GetKey(handle1)
    assert err == skycoin.SKY_OK
    err, Key2 = skycoin.SKY_bip32_PublicKey_GetKey(handle2)
    assert err == skycoin.SKY_OK
    if(Key1 != Key2):
        print("Key not equal\n")
        return 0

    return 1
