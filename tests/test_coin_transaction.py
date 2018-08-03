import skycoin
from tests.utils.skyerror import error
from tests.utils import transutil


def test_TestTransactionVerify():
    # Mismatch header hash
    handle, tx = transutil.makeTransaction()
    h = skycoin.cipher_SHA256()
    h.assignTo(tx.InnerHash)
    assert skycoin.SKY_coin_Transaction_Verify(handle) == error["SKY_ERROR"]
    # No inputs
    handle, tx = transutil.makeTransaction()
    assert skycoin.SKY_coin_Transaction_ResetInputs(
        handle, 0) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_UpdateHeader(handle) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_Verify(handle) == error["SKY_ERROR"]
    # No outputs
    handle, _ = transutil.makeTransaction()
    assert skycoin.SKY_coin_Transaction_ResetOutputs(
        handle, 0) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_UpdateHeader(handle) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_Verify(handle) == error["SKY_ERROR"]
    # Invalid number of Sigs
    handle, _ = transutil.makeTransaction()
    assert skycoin.SKY_coin_Transaction_ResetSignatures(
        handle, 0) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_UpdateHeader(handle) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_Verify(handle) == error["SKY_ERROR"]
    assert skycoin.SKY_coin_Transaction_ResetSignatures(
        handle, 20) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_UpdateHeader(handle) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_Verify(handle) == error["SKY_ERROR"]
    # Too many sigs & inputs
    handle, _ = transutil.makeTransaction()
    assert skycoin.SKY_coin_Transaction_ResetSignatures(
        handle, transutil.MaxUint16) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_ResetInputs(
        handle, transutil.MaxUint16) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_UpdateHeader(handle) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_Verify(handle) == error["SKY_ERROR"]
    # Duplicate inputs
    ux, s = transutil.makeUxOutWithSecret()
    handle, _ = transutil.makeTransactionFromUxOut(ux, s)
    h = skycoin.cipher_SHA256()
    assert skycoin.SKY_coin_Transaction_GetInputAt(
        handle, 0, h) == error["SKY_OK"]
    err, _ = skycoin.SKY_coin_Transaction_PushInput(handle, h)
    assert err == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_ResetSignatures(
        handle, 0) == error["SKY_OK"]
    secKeys = []
    secKeys.append(s)
    secKeys.append(s)
    assert skycoin.SKY_coin_Transaction_SignInputs(
        handle, secKeys) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_UpdateHeader(handle) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_Verify(handle) == error["SKY_ERROR"]
    # Duplicate outputs
    handle, _ = transutil.makeTransaction()
    pOutput = skycoin.coin__TransactionOutput()
    assert skycoin.SKY_coin_Transaction_GetOutputAt(
        handle, 0, pOutput) == error["SKY_OK"]
    pOutput.Address = skycoin.cipher__Address()
    assert skycoin.SKY_coin_Transaction_ResetOutputs(
        handle, 0) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_PushOutput(
        handle, pOutput.Address, pOutput.Coins, pOutput.Hours) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_PushOutput(
        handle, pOutput.Address, pOutput.Coins, pOutput.Hours) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_UpdateHeader(handle) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_Verify(handle) == error["SKY_ERROR"]
    # Output coins are 0
    handle, _ = transutil.makeTransaction()
    assert skycoin.SKY_coin_Transaction_GetOutputAt(
        handle, 0, pOutput) == error["SKY_OK"]
    pOutput.Coins = 0
    assert skycoin.SKY_coin_Transaction_ResetOutputs(
        handle, 0) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_PushOutput(
        handle, pOutput.Address, pOutput.Coins, pOutput.Hours) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_UpdateHeader(handle) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_Verify(handle) == error["SKY_ERROR"]
    # Output coin overflow
    handle, _ = transutil.makeTransaction()
    assert skycoin.SKY_coin_Transaction_GetOutputAt(
        handle, 0, pOutput) == error["SKY_OK"]
    pOutput.Coins = int(transutil.MaxUint64 - int(3e6))
    assert skycoin.SKY_coin_Transaction_PushOutput(
        handle, pOutput.Address, pOutput.Coins, pOutput.Hours) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_UpdateHeader(handle) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_Verify(handle) == error["SKY_ERROR"]
    # Output coins are not multiples of 1e6 (valid, decimal restriction is not enforced here)
    handle, _ = transutil.makeTransaction()
    assert skycoin.SKY_coin_Transaction_GetOutputAt(
        handle, 0, pOutput) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_ResetOutputs(
        handle, 0) == error["SKY_OK"]
    pOutput.Coins += 10
    assert skycoin.SKY_coin_Transaction_PushOutput(
        handle, pOutput.Address, pOutput.Coins, pOutput.Hours) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_UpdateHeader(handle) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_ResetSignatures(
        handle, 0) == error["SKY_OK"]
    p = skycoin.cipher_PubKey()
    s = skycoin.cipher_SecKey()
    assert skycoin.SKY_cipher_GenerateKeyPair(p, s) == error["SKY_OK"]
    secKeys = []
    secKeys.append(s)
    assert skycoin.SKY_coin_Transaction_SignInputs(
        handle, secKeys) == error["SKY_OK"]
    assert int(pOutput.Coins % int(1e6)) != int(0)
    assert skycoin.SKY_coin_Transaction_Verify(handle) == error["SKY_OK"]
    # Valid
    handle, _ = transutil.makeTransaction()
    assert skycoin.SKY_coin_Transaction_GetOutputAt(
        handle, 0, pOutput) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_ResetOutputs(
        handle, 0) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_PushOutput(
        handle, pOutput.Address, int(10e6), pOutput.Hours) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_PushOutput(
        handle, pOutput.Address, int(1e6), pOutput.Hours) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_UpdateHeader(handle) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_Verify(handle) == error["SKY_OK"]


def test_TestTransactionVerifyInput():
    # Invalid uxIn args
    handle, _ = transutil.makeTransaction()
    seckeys = []
    assert skycoin.SKY_coin_Transaction_VerifyInput(
        handle, seckeys) == error["SKY_ERROR"]
    seckeys = []
    seckeys.append(skycoin.coin__UxOut())
    seckeys.append(skycoin.coin__UxOut())
    seckeys.append(skycoin.coin__UxOut())
    assert skycoin.SKY_coin_Transaction_VerifyInput(
        handle, seckeys) == error["SKY_ERROR"]

    # tx.In != tx.Sigs
    ux, s = transutil.makeUxOutWithSecret()
    handle, _ = transutil.makeTransactionFromUxOut(ux, s)
    assert skycoin.SKY_coin_Transaction_ResetSignatures(
        handle, 0) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_PushSignature(
        handle, skycoin.cipher_Sig()) == error["SKY_OK"]
    seckeys = []
    seckeys.append(ux)
    assert skycoin.SKY_coin_Transaction_VerifyInput(
        handle, seckeys) == error["SKY_ERROR"]

    ux, s = transutil.makeUxOutWithSecret()
    handle, _ = transutil.makeTransactionFromUxOut(ux, s)
    sigs = skycoin.cipher_Sig()
    assert skycoin.SKY_coin_Transaction_GetSignatureAt(
        handle, 0, sigs) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_ResetSignatures(
        handle, 0) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_PushSignature(
        handle, sigs) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_PushSignature(
        handle, skycoin.cipher_Sig()) == error["SKY_OK"]
    seckeys = []
    seckeys.append(ux)
    assert skycoin.SKY_coin_Transaction_VerifyInput(
        handle, seckeys) == error["SKY_ERROR"]

    # tx.InnerHash != tx.HashInner()
    ux, s = transutil.makeUxOutWithSecret()
    handle, tx = transutil.makeTransactionFromUxOut(ux, s)
    skycoin.cipher_SHA256().assignTo(tx.InnerHash)
    seckeys = []
    seckeys.append(ux)
    assert skycoin.SKY_coin_Transaction_VerifyInput(
        handle, seckeys) == error["SKY_ERROR"]

    # tx.In does not match uxIn hashes
    ux, s = transutil.makeUxOutWithSecret()
    handle, tx = transutil.makeTransactionFromUxOut(ux, s)
    seckeys = []
    seckeys.append(skycoin.coin__UxOut())
    assert skycoin.SKY_coin_Transaction_VerifyInput(
        handle, seckeys) == error["SKY_ERROR"]
    # Invalid signature
    ux, s = transutil.makeUxOutWithSecret()
    handle, tx = transutil.makeTransactionFromUxOut(ux, s)
    sigs = skycoin.cipher_Sig()
    assert skycoin.SKY_coin_Transaction_SetSignatureAt(
        handle, 0, sigs) == error["SKY_OK"]
    seckeys = []
    seckeys.append(ux)
    assert skycoin.SKY_coin_Transaction_VerifyInput(
        handle, seckeys) == error["SKY_ERROR"]

    # Valid
    ux, s = transutil.makeUxOutWithSecret()
    handle, tx = transutil.makeTransactionFromUxOut(ux, s)
    seckeys = []
    seckeys.append(ux)
    assert skycoin.SKY_coin_Transaction_VerifyInput(
        handle, seckeys) == error["SKY_OK"]


def test_TestTransactionPushInput():
    handle = transutil.makeEmptyTransaction()
    ux = transutil.makeUxOut()
    sha = skycoin.cipher_SHA256()
    assert skycoin.SKY_coin_UxOut_Hash(ux, sha) == error["SKY_OK"]
    _, r = skycoin.SKY_coin_Transaction_PushInput(handle, sha)
    assert r == 0
    _, count = skycoin.SKY_coin_Transaction_GetInputsCount(handle)
    assert count == 1
    sha1 = skycoin.cipher_SHA256()
    skycoin.SKY_coin_Transaction_GetInputAt(handle, 0, sha1)
    assert sha == sha1
    skycoin.SKY_coin_Transaction_ResetInputs(handle, 0)
    for _ in range(transutil.MaxUint16):
        err, _ = skycoin.SKY_coin_Transaction_PushInput(
            handle, skycoin.cipher_SHA256())
        assert err == error["SKY_OK"]
    ux = transutil.makeUxOut()
    assert skycoin.SKY_coin_UxOut_Hash(ux, sha) == error["SKY_OK"]
    err, _ = skycoin.SKY_coin_Transaction_PushInput(handle, sha)
    assert err == error["SKY_ERROR"]


def test_TestTransactionPushOutput():
    handle = transutil.makeEmptyTransaction()
    a = transutil.makeAddress()
    assert skycoin.SKY_coin_Transaction_PushOutput(
        handle, a, 100, 150) == error["SKY_OK"]
    err, count = skycoin.SKY_coin_Transaction_GetOutputsCount(handle)
    assert err == error["SKY_OK"]
    assert count == 1
    pOut1 = skycoin.coin__TransactionOutput()
    pOut = skycoin.coin__TransactionOutput()
    pOut1.Address = a
    pOut1.Coins = 100
    pOut1.Hours = 150
    assert skycoin.SKY_coin_Transaction_GetOutputAt(
        handle, 0, pOut) == error["SKY_OK"]
    assert pOut == pOut1
    for i in range(1, 20):
        a = transutil.makeAddress()
        assert skycoin.SKY_coin_Transaction_PushOutput(
            handle, a, int(i * 100), int(i * 50)) == error["SKY_OK"]
        err, count = skycoin.SKY_coin_Transaction_GetOutputsCount(handle)
        assert err == error["SKY_OK"]
        assert count == int(i + 1)
        pOut1.Address = a
        pOut1.Coins = int(i * 100)
        pOut1.Hours = int(i * 150)
        assert skycoin.SKY_coin_Transaction_GetOutputAt(
            handle, i, pOut) == error["SKY_OK"]
        assert pOut == pOut
        i += 1


def test_TestTransactionSignInputs():
    handle = transutil.makeEmptyTransaction()
    # Panics if txns already signed
    sig = skycoin.cipher_Sig()
    assert skycoin.SKY_coin_Transaction_PushSignature(
        handle, sig) == error["SKY_OK"]
    secKeys = []
    secKeys.append(skycoin.cipher_SecKey())
    assert skycoin.SKY_coin_Transaction_SignInputs(
        handle, secKeys) == error["SKY_ERROR"]
    # Panics if not enough keys
    handle = transutil.makeEmptyTransaction()
    ux, s = transutil.makeUxOutWithSecret()
    h = skycoin.cipher_SHA256()
    assert skycoin.SKY_coin_UxOut_Hash(ux, h) == error["SKY_OK"]
    err, _ = skycoin.SKY_coin_Transaction_PushInput(handle, h)
    assert err == error["SKY_OK"]
    ux2, s2 = transutil.makeUxOutWithSecret()
    assert skycoin.SKY_coin_UxOut_Hash(ux2, h) == error["SKY_OK"]
    err, _ = skycoin.SKY_coin_Transaction_PushInput(handle, h)
    assert err == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_PushOutput(
        handle, transutil.makeAddress(), 40, 80) == error["SKY_OK"]
    err, count = skycoin.SKY_coin_Transaction_GetSignaturesCount(handle)
    assert err == error["SKY_OK"]
    assert count == 0
    # Valid signing
    assert skycoin.SKY_coin_Transaction_HashInner(handle, h) == error["SKY_OK"]
    secKeys = []
    secKeys.append(s)
    secKeys.append(s2)
    assert skycoin.SKY_coin_Transaction_SignInputs(
        handle, secKeys) == error["SKY_OK"]
    err, count = skycoin.SKY_coin_Transaction_GetSignaturesCount(handle)
    assert err == error["SKY_OK"]
    assert count == 2
    h2 = skycoin.cipher_SHA256()
    assert skycoin.SKY_coin_Transaction_HashInner(
        handle, h2) == error["SKY_OK"]
    assert h == h2
    p = skycoin.cipher_PubKey()
    assert skycoin.SKY_cipher_PubKeyFromSecKey(s, p) == error["SKY_OK"]
    a = skycoin.cipher__Address()
    a2 = skycoin.cipher__Address()
    assert skycoin.SKY_cipher_AddressFromPubKey(p, a) == error["SKY_OK"]
    assert skycoin.SKY_cipher_PubKeyFromSecKey(s2, p) == error["SKY_OK"]
    assert skycoin.SKY_cipher_AddressFromPubKey(p, a2) == error["SKY_OK"]
    sha1 = skycoin.cipher_SHA256()
    sha2 = skycoin.cipher_SHA256()
    txin0 = skycoin.cipher_SHA256()
    txin1 = skycoin.cipher_SHA256()
    assert skycoin.SKY_coin_Transaction_GetInputAt(
        handle, 0, txin0) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_GetInputAt(
        handle, 1, txin1) == error["SKY_OK"]
    assert skycoin.SKY_cipher_AddSHA256(h, txin0, sha1) == error["SKY_OK"]
    assert skycoin.SKY_cipher_AddSHA256(h, txin1, sha2) == error["SKY_OK"]
    txsig0 = skycoin.cipher_Sig()
    txsig1 = skycoin.cipher_Sig()
    assert skycoin.SKY_coin_Transaction_GetSignatureAt(
        handle, 0, txsig0) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_GetSignatureAt(
        handle, 1, txsig1) == error["SKY_OK"]
    assert skycoin.SKY_cipher_ChkSig(a, sha1, txsig0) == error["SKY_OK"]
    assert skycoin.SKY_cipher_ChkSig(a2, sha2, txsig1) == error["SKY_OK"]
    assert skycoin.SKY_cipher_ChkSig(a, h, txsig1) == error["SKY_ERROR"]
    assert skycoin.SKY_cipher_ChkSig(a2, h, txsig0) == error["SKY_ERROR"]


def test_TestTransactionHash():
    handle, _ = transutil.makeTransaction()
    h = skycoin.cipher_SHA256()
    h2 = skycoin.cipher_SHA256()
    assert skycoin.SKY_coin_Transaction_Hash(handle, h) == error["SKY_OK"]
    assert h != h2
    assert skycoin.SKY_coin_Transaction_HashInner(
        handle, h2) == error["SKY_OK"]
    assert h != h2


def test_TestTransactionUpdateHeader():
    handle, tx = transutil.makeTransaction()
    h = skycoin.cipher_SHA256()
    h1 = skycoin.cipher_SHA256()
    h2 = skycoin.cipher_SHA256()
    assert skycoin.SKY_coin_Transaction_HashInner(handle, h) == error["SKY_OK"]
    skycoin.cipher_SHA256().assignTo(tx.InnerHash)
    assert skycoin.SKY_coin_Transaction_UpdateHeader(handle) == error["SKY_OK"]
    h1.assignFrom(tx.InnerHash)
    assert skycoin.SKY_coin_Transaction_HashInner(
        handle, h2) == error["SKY_OK"]
    assert h1 != skycoin.cipher_SHA256()
    assert h1 == h
    assert h1 == h2


def test_TestTransactionHashInner():
    handle, tx = transutil.makeTransaction()
    h = skycoin.cipher_SHA256()
    assert skycoin.SKY_coin_Transaction_HashInner(handle, h) == error["SKY_OK"]
    assert h != skycoin.cipher_SHA256()

    #  If tx.In is changed, hash should change
    handle2, tx2 = transutil.copyTransaction(handle)
    ux = transutil.makeUxOut()
    h = skycoin.cipher_SHA256()
    h1 = skycoin.cipher_SHA256()
    assert skycoin.SKY_coin_UxOut_Hash(ux, h) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_SetInputAt(
        handle2, 0, h) == error["SKY_OK"]
    assert tx != tx2
    assert skycoin.SKY_coin_UxOut_Hash(ux, h1) == error["SKY_OK"]
    assert h == h1
    assert skycoin.SKY_coin_Transaction_HashInner(handle, h) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_HashInner(
        handle2, h1) == error["SKY_OK"]
    assert h != h1

    # If tx.Out is changed, hash should change
    handle2, tx2 = transutil.copyTransaction(handle)
    a = transutil.makeAddress()
    a2 = skycoin.cipher__Address()
    pOut = skycoin.coin__TransactionOutput()
    assert skycoin.SKY_coin_Transaction_GetOutputAt(
        handle2, 0, pOut) == error["SKY_OK"]
    pOut.Address = a
    assert skycoin.SKY_coin_Transaction_SetOutputAt(
        handle2, 0, pOut) == error["SKY_OK"]
    assert tx != tx2
    assert skycoin.SKY_coin_Transaction_GetOutputAt(
        handle2, 0, pOut) == error["SKY_OK"]
    assert pOut.Address == a
    sha1 = skycoin.cipher_SHA256()
    sha2 = skycoin.cipher_SHA256()
    assert skycoin.SKY_coin_Transaction_HashInner(
        handle, sha1) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_HashInner(
        handle2, sha2) == error["SKY_OK"]
    assert sha1 != sha2

    # If tx.Head is changed, hash should not change
    handle2, tx2 = transutil.copyTransaction(handle)
    sig = skycoin.cipher_Sig()
    assert skycoin.SKY_coin_Transaction_PushSignature(
        handle, sig) == error["SKY_OK"]
    sha1 = skycoin.cipher_SHA256()
    sha2 = skycoin.cipher_SHA256()
    assert skycoin.SKY_coin_Transaction_HashInner(
        handle, sha1) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_HashInner(
        handle2, sha2) == error["SKY_OK"]
    assert sha1 == sha2


def test_TestTransactionSerialization():
    handle, tx = transutil.makeTransaction()
    err, b = skycoin.SKY_coin_Transaction_Serialize(handle)
    assert err == error["SKY_OK"]
    err, handle2 = skycoin.SKY_coin_TransactionDeserialize(b)
    assert err == error["SKY_OK"]
    err, tx2 = skycoin.SKY_coin_GetTransactionObject(handle2)
    assert err == error["SKY_OK"]
    assert tx == tx2
    # Invalid deserialization
    err, _ = skycoin.SKY_coin_MustTransactionDeserialize(bytes(0x04))
    assert err == error["SKY_ERROR"]


def test_TestTransactionOutputHours():
    handle = transutil.makeEmptyTransaction()
    assert skycoin.SKY_coin_Transaction_PushOutput(
        handle, transutil.makeAddress(), int(1e6), 100) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_PushOutput(
        handle, transutil.makeAddress(), int(1e6), 200) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_PushOutput(
        handle, transutil.makeAddress(), int(1e6), 500) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_PushOutput(
        handle, transutil.makeAddress(), int(1e6), 0) == error["SKY_OK"]
    err, hours = skycoin.SKY_coin_Transaction_OutputHours(handle)
    assert err == error["SKY_OK"]
    assert hours == 800

    assert skycoin.SKY_coin_Transaction_PushOutput(
        handle, transutil.makeAddress(), int(1e6), int(transutil.MaxUint64 - 700)) == error["SKY_OK"]
    err, _ = skycoin.SKY_coin_Transaction_OutputHours(handle)
    assert err == error["SKY_ERROR"]


def test_TestTransactionsSize():
    handle = transutil.makeTransactions(10)
    size = 0
    for i in range(10):
        err, tx = skycoin.SKY_coin_Transactions_GetAt(handle, i)
        assert err == error["SKY_OK"]
        err, b = skycoin.SKY_coin_Transaction_Serialize(tx)
        size += len(b)
        i += 1

    assert size != 0
    err, sizetx = skycoin.SKY_coin_Transactions_Size(handle)
    assert err == error["SKY_OK"]
    assert sizetx == size


def test_TestTransactionsHashes():
    handle = transutil.makeTransactions(4)
    err, hashes = skycoin.SKY_coin_Transactions_Hashes(handle)
    assert err == error["SKY_OK"]
    len_hashes = len(hashes)
    assert len_hashes == 4
    for i in range(len_hashes):
        err, tx = skycoin.SKY_coin_Transactions_GetAt(handle, i)
        assert err == error["SKY_OK"]
        h = skycoin.cipher_SHA256()
        assert skycoin.SKY_coin_Transaction_Hash(tx, h) == error["SKY_OK"]
        assert h == hashes[i]
        i += 1


def test_TestTransactionsTruncateBytesTo():
    handles = transutil.makeTransactions(10)
    trunc = 0
    for i in range(5):
        err, handle = skycoin.SKY_coin_Transactions_GetAt(handles, i)
        assert err == error["SKY_OK"]
        err, count = skycoin.SKY_coin_Transaction_Size(handle)
        assert err == error["SKY_OK"]
        trunc += count
        i += 1
    # Trucating halfway
    err, tnxs2 = skycoin.SKY_coin_Transactions_TruncateBytesTo(handles, trunc)
    assert err == error["SKY_OK"]
    err, len_tnxs2 = skycoin.SKY_coin_Transactions_Length(tnxs2)
    assert err == error["SKY_OK"]
    assert len_tnxs2 == 5
    err, count = skycoin.SKY_coin_Transactions_Size(tnxs2)
    assert err == error["SKY_OK"]
    assert count == trunc

    # Stepping into next boundary has same cutoff, must exceed
    trunc += 1
    err, txns2 = skycoin.SKY_coin_Transactions_TruncateBytesTo(handles, trunc)
    assert err == error["SKY_OK"]
    err, count = skycoin.SKY_coin_Transactions_Length(tnxs2)
    assert err == error["SKY_OK"]
    assert count == 5
    err, count = skycoin.SKY_coin_Transactions_Size(tnxs2)
    assert err == error["SKY_OK"]
    assert count == int(trunc - 1)

    # Moving to 1 before next level
    err, tnxs_5 = skycoin.SKY_coin_Transactions_GetAt(handles, 5)
    assert err == error["SKY_OK"]
    err, count = skycoin.SKY_coin_Transaction_Size(tnxs_5)
    assert err == error["SKY_OK"]
    trunc += int(count - 2)
    err, txns2 = skycoin.SKY_coin_Transactions_TruncateBytesTo(handles, trunc)
    assert err == error["SKY_OK"]
    err, count = skycoin.SKY_coin_Transactions_Length(txns2)
    assert err == error["SKY_OK"]
    assert count == 5
    err, count = skycoin.SKY_coin_Transactions_Size(txns2)
    assert err == error["SKY_OK"]
    err, count_tnxs5 = skycoin.SKY_coin_Transaction_Size(tnxs_5)
    assert err == error["SKY_OK"]
    assert int(trunc - count_tnxs5 + 1) == count

    # Moving to next level
    trunc += 1
    err, txns2 = skycoin.SKY_coin_Transactions_TruncateBytesTo(handles, trunc)
    assert err == error["SKY_OK"]
    err, count = skycoin.SKY_coin_Transactions_Length(txns2)
    assert err == error["SKY_OK"]
    assert count == 6
    err, count = skycoin.SKY_coin_Transactions_Size(txns2)
    assert err == error["SKY_OK"]
    assert count == trunc

    # Truncating to full available amt
    err, trunc = skycoin.SKY_coin_Transactions_Size(handles)
    assert err == error["SKY_OK"]
    err, txns2 = skycoin.SKY_coin_Transactions_TruncateBytesTo(handles, trunc)
    assert err == error["SKY_OK"]
    assert err == error["SKY_OK"]
    err, count = skycoin.SKY_coin_Transactions_Size(txns2)
    assert err == error["SKY_OK"]
    assert count == trunc
    assert transutil.equalTransactions(handles, txns2) == error["SKY_OK"]

    # Truncating over amount
    trunc += 1
    err, txns2 = skycoin.SKY_coin_Transactions_TruncateBytesTo(handles, trunc)
    assert transutil.equalTransactions(handles, txns2) == error["SKY_OK"]
    err, count = skycoin.SKY_coin_Transactions_Size(handles)
    assert err == error["SKY_OK"]
    assert count == int(trunc - 1)

    # Truncating to 0
    trunc = 0
    err, txns2 = skycoin.SKY_coin_Transactions_TruncateBytesTo(handles, 0)
    assert err == error["SKY_OK"]
    err, count = skycoin.SKY_coin_Transactions_Length(txns2)
    assert err == error["SKY_OK"]
    assert count == 0
    err, count = skycoin.SKY_coin_Transactions_Size(txns2)
    assert err == error["SKY_OK"]
    assert count == trunc


class ux():
    coins = 0
    hours = 0


class cases():
    name = ""
    inUxs = []
    outUxs = []
    err = error["SKY_OK"]
    headTime = 0


def test_TestVerifyTransactionCoinsSpending():
    case = []
    inu1 = ux()
    tests1 = cases
    tests1.name = "Input coins overflow"
    tests1.err = error["SKY_ERROR"]
    inu1.coins = int(transutil.MaxUint64 - int(1e6) + 1)
    inu1.hours = 10
    tests1.inUxs.append(inu1)
    inu1.coins = int(1e6)
    inu1.hours = 0
    tests1.inUxs.append(inu1)
    case.append(tests1)

    tests2 = cases
    inu2 = ux
    tests2.name = "Output coins overflow"
    tests2.err = error["SKY_ERROR"]
    inu2.coins = int(10e6)
    inu2.hours = 10
    tests2.inUxs.append(inu2)
    inu2.coins = int(transutil.MaxUint64 - 10e6 + 1)
    inu2.hours = 0
    tests2.outUxs.append(inu2)
    inu2.coins = int(20e6)
    inu2.hours = 1
    tests2.outUxs.append(inu2)
    case.append(tests2)

    tests3 = cases
    inu3 = ux
    tests3.name = "Insufficient coins"
    tests3.err = error["SKY_ERROR"]
    inu3.coins = int(10e6)
    inu3.hours = int(10)
    tests3.inUxs.append(inu3)
    inu3.coins = int(15e6)
    inu3.hours = int(10)
    tests3.inUxs.append(inu3)
    inu3.coins = int(20e6)
    inu3.hours = int(1)
    tests3.outUxs.append(inu3)
    inu3.coins = int(10e6)
    inu3.hours = int(1)
    tests3.outUxs.append(inu3)
    case.append(tests3)

    tests4 = cases
    inu4 = ux
    tests4.name = "Destroyed coins"
    tests4.err = error["SKY_ERROR"]
    inu4.coins = int(10e6)
    inu4.hours = int(10)
    tests4.inUxs.append(inu4)
    inu4.coins = int(15e6)
    inu4.hours = int(10)
    tests4.inUxs.append(inu4)
    inu4.coins = int(5e6)
    inu4.hours = int(1)
    tests4.outUxs.append(inu4)
    inu4.coins = int(10e6)
    inu4.hours = int(1)
    tests4.outUxs.append(inu4)
    case.append(tests4)

    tests5 = cases
    inu5 = ux
    tests5.name = "valid"

    inu5.coins = int(10e6)
    inu5.hours = int(10)
    tests5.inUxs.append(inu5)
    inu5.coins = int(15e6)
    inu5.hours = int(10)
    tests5.inUxs.append(inu5)

    inu5.coins = int(10e6)
    inu5.hours = int(11)
    tests5.outUxs.append(inu5)
    inu5.coins = int(10e6)
    inu5.hours = int(1)
    tests5.outUxs.append(inu5)
    inu5.coins = int(5e6)
    inu5.hours = int(0)
    tests5.outUxs.append(inu5)
    case.append(tests5)

    for tc in case:
        uxIn = []
        uxOut = []
        for ch in tc.inUxs:
            puxIn = skycoin.coin__UxOut()
            puxIn.Body.Coins = ch.coins
            puxIn.Body.Hours = ch.hours
            uxIn.append(puxIn)
        for ch in tc.outUxs:
            puxOut = skycoin.coin__UxOut()
            puxOut.Body.Coins = ch.coins
            puxOut.Body.Hours = ch.hours
            uxOut.append(puxOut)
        assert skycoin.SKY_coin_VerifyTransactionCoinsSpending(
            uxIn, uxOut) == tc.err


def test_TestVerifyTransactionHoursSpending():
    case = []
    # Case #1
    case1 = cases()
    case1.name = "Input hours overflow"
    ux1_1 = ux()
    ux1_1.coins = int(3e6)
    ux1_1.hours = int(transutil.MaxUint64 - int(1e6) + 1)
    case1.inUxs.append(ux1_1)
    ux1_2 = ux()
    ux1_2.coins = int(1e6)
    ux1_2.hours = int(1e6)
    case1.inUxs.append(ux1_2)
    case1.err = error["SKY_ERROR"]
    case.append(case1)

    # Case #2
    case2 = cases()
    case2.name = "Insufficient coin hours"
    case2.err = error["SKY_ERROR"]
    ux2_1 = ux()
    ux2_1.coins = int(10e6)
    ux2_1.hours = 10
    case2.inUxs.append(ux2_1)
    ux2_2 = ux()
    ux2_2.coins = int(15e6)
    ux2_2.hours = 10
    case2.inUxs.append(ux2_2)
    ox2_1 = ux()
    ox2_1.coins = int(15e6)
    ox2_1.hours = 10
    case2.outUxs.append(ox2_1)
    ox2_2 = ux()
    ox2_2.coins = int(10e6)
    ox2_2.hours = 11
    case2.outUxs.append(ox2_2)
    case.append(case2)

    # Case #3
    case3 = cases()
    case3.name = "coin hours time calculation overflow"
    case3.err = error["SKY_ERROR"]
    case3.headTime = transutil.MaxUint64
    ux3_1 = ux()
    ux3_1.coins = int(10e6)
    ux3_1.hours = 10
    case3.inUxs.append(ux3_1)
    ux3_2 = ux()
    ux3_2.coins = int(15e6)
    ux3_2.hours = 10
    case3.inUxs.append(ux3_2)
    ox3_1 = ux()
    ox3_1.coins = int(10e6)
    ox3_1.hours = 11
    case3.outUxs.append(ox3_1)
    ox3_2 = ux()
    ox3_2.coins = int(10e6)
    ox3_2.hours = 1
    case3.outUxs.append(ox3_2)
    ox3_3 = ux()
    ox3_3.coins = int(5e6)
    ox3_3.hours = 0
    case3.outUxs.append(ox3_3)
    case.append(case3)

    # Case #4
    case4 = cases()
    case4.name = "Invalid (coin hours overflow when adding earned hours, which is treated as 0, and now enough coin hours)"
    case4.err = error["SKY_ERROR"]
    case4.headTime = int(1e6)
    ux4_1 = ux()
    ux4_1.coins = int(10e6)
    ux4_1.hours = transutil.MaxUint64
    case4.inUxs.append(ux4_1)
    ox4_1 = ux()
    ox4_1.coins = int(10e6)
    ox4_1.hours = 1
    case4.outUxs.append(ox4_1)

    # Case #5
    case5 = cases()
    case5.name = "Valid (coin hours overflow when adding earned hours, which is treated as 0, but not sending any hours)"
    case5.headTime = int(1e6)
    ux5_1 = ux()
    ux5_1.coins = int(10e6)
    ux5_1.hours = transutil.MaxUint64
    case5.inUxs.append(ux5_1)
    ox5_1 = ux()
    ox5_1.coins = int(10e6)
    ox5_1.hours = 0
    case5.outUxs.append(ox5_1)
    case.append(case5)

    # Case #6
    case6 = cases()
    case6.err = error["SKY_OK"]
    case6.name = "Valid (base inputs have insufficient coin hours, but have sufficient after adjusting coinhours by headTime)"
    case6.headTime = 1492707255
    ux6_1 = ux()
    ux6_1.coins = int(10e6)
    ux6_1.hours = 10
    case6.inUxs.append(ux6_1)
    ux6_2 = ux()
    ux6_2.coins = int(15e6)
    ux6_2.hours = 10
    case6.inUxs.append(ux6_2)
    ox6_1 = ux()
    ox6_1.coins = int(15e6)
    ox6_1.hours = 10
    case6.outUxs.append(ox6_1)
    ox6_2 = ux()
    ox6_2.coins = int(10e6)
    ox6_2.hours = 11
    case6.outUxs.append(ox6_2)
    case.append(case6)

    # Case #7
    case7 = cases()
    case7.name = "valid"
    ux7_1 = ux()
    ux7_1.coins = int(10e6)
    ux7_1.hours = 10
    case7.inUxs.append(ux7_1)
    ux7_2 = ux()
    ux7_2.coins = int(15e6)
    ux7_2.hours = 10
    case7.inUxs.append(ux7_2)
    ox7_1 = ux()
    ox7_1.coins = int(10e6)
    ox7_1.hours = 11
    case7.outUxs.append(ox7_1)
    ox7_2 = ux()
    ox7_2.coins = int(10e6)
    ox7_2.hours = 1
    case7.outUxs.append(ox7_2)
    ox7_3 = ux()
    ox7_3.coins = int(5e6)
    ox7_3.hours = 0
    case7.outUxs.append(ox7_3)
    case.append(case7)

    for tc in case:
        uxIn = []
        uxOut = []
        for ch in tc.inUxs:
            puxIn = skycoin.coin__UxOut()
            puxIn.Body.Coins = ch.coins
            puxIn.Body.Hours = ch.hours
            uxIn.append(puxIn)
        for ch in tc.outUxs:
            puxOut = skycoin.coin__UxOut()
            puxOut.Body.Coins = ch.coins
            puxOut.Body.Hours = ch.hours
            uxOut.append(puxOut)
        print(tc.name)
        assert skycoin.SKY_coin_VerifyTransactionHoursSpending(
            tc.headTime, uxIn, uxOut) == tc.err


def calc(transactions):
    return 0, 1


def test_TestTransactionsFees():
    txns = transutil.makeTransactions(0)
    # Nil txns
    err, fee = skycoin.SKY_coin_Transactions_Fees(
        txns, calc)
    assert err == error["SKY_OK"]
    assert fee == 0

    # 2 transactions, calc() always returns 1
    txn = transutil.makeEmptyTransaction()
    assert skycoin.SKY_coin_Transactions_Add(txns, txn) == error["SKY_OK"]
    txn1 = transutil.makeEmptyTransaction()
    assert skycoin.SKY_coin_Transactions_Add(txns, txn1) == error["SKY_OK"]
    err, fee = skycoin.SKY_coin_Transactions_Fees(
        txns, calc)
    assert err == error["SKY_OK"]
    assert fee == 2
