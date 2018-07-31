import skycoin
from tests.utils.skyerror import error
from tests.utils import transutil
MaxUint64 = 0xFFFFFFFFFFFFFFFF
Million = 1000000
MaxUint16 = 0xFFFF


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
        handle, MaxUint16) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_ResetInputs(
        handle, MaxUint16) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_UpdateHeader(handle) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_Verify(handle) == error["SKY_ERROR"]
    # Duplicate inputs
    ux, s = transutil.makeUxOutWithSecret()
    handle, _ = transutil.makeTransactionFromUxOut(ux, s)
    h = skycoin.cipher_SHA256()
    assert skycoin.SKY_coin_Transaction_Get_Input_At(
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
    assert skycoin.SKY_coin_Transaction_Get_Output_At(
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
    assert skycoin.SKY_coin_Transaction_Get_Output_At(
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
    assert skycoin.SKY_coin_Transaction_Get_Output_At(
        handle, 0, pOutput) == error["SKY_OK"]
    pOutput.Coins = int(MaxUint64 - int(3e6))
    assert skycoin.SKY_coin_Transaction_PushOutput(
        handle, pOutput.Address, pOutput.Coins, pOutput.Hours) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_UpdateHeader(handle) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_Verify(handle) == error["SKY_ERROR"]
    # Output coins are not multiples of 1e6 (valid, decimal restriction is not enforced here)
    handle, _ = transutil.makeTransaction()
    assert skycoin.SKY_coin_Transaction_Get_Output_At(
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
    assert skycoin.SKY_coin_Transaction_Get_Output_At(
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
    assert skycoin.SKY_coin_Transaction_Push_Signature(
        handle, skycoin.cipher_Sig()) == error["SKY_OK"]
    seckeys = []
    seckeys.append(ux)
    assert skycoin.SKY_coin_Transaction_VerifyInput(
        handle, seckeys) == error["SKY_ERROR"]

    ux, s = transutil.makeUxOutWithSecret()
    handle, _ = transutil.makeTransactionFromUxOut(ux, s)
    sigs = skycoin.cipher_Sig()
    assert skycoin.SKY_coin_Transaction_Get_Signature_At(
        handle, 0, sigs) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_ResetSignatures(
        handle, 0) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_Push_Signature(
        handle, sigs) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_Push_Signature(
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
    assert skycoin.SKY_coin_Transaction_Set_Signature_At(
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
    ux, _ = transutil.makeUxOut()
    sha = skycoin.cipher_SHA256()
    assert skycoin.SKY_coin_UxOut_Hash(ux, sha) == error["SKY_OK"]
    _, r = skycoin.SKY_coin_Transaction_PushInput(handle, sha)
    assert r == 0
    _, count = skycoin.SKY_coin_Transaction_Get_Inputs_Count(handle)
    assert count == 1
    sha1 = skycoin.cipher_SHA256()
    skycoin.SKY_coin_Transaction_Get_Input_At(handle, 0, sha1)
    assert sha == sha1
    skycoin.SKY_coin_Transaction_ResetInputs(handle, 0)
    for _ in range(MaxUint16):
        err, _ = skycoin.SKY_coin_Transaction_PushInput(
            handle, skycoin.cipher_SHA256())
        assert err == error["SKY_OK"]
    ux, _ = transutil.makeUxOut()
    assert skycoin.SKY_coin_UxOut_Hash(ux, sha) == error["SKY_OK"]
    err, _ = skycoin.SKY_coin_Transaction_PushInput(handle, sha)
    assert err == error["SKY_ERROR"]


def test_TestTransactionPushOutput():
    handle = transutil.makeEmptyTransaction()
    a = transutil.makeAddress()
    assert skycoin.SKY_coin_Transaction_PushOutput(
        handle, a, 100, 150) == error["SKY_OK"]
    err, count = skycoin.SKY_coin_Transaction_Get_Outputs_Count(handle)
    assert err == error["SKY_OK"]
    assert count == 1
    pOut1 = skycoin.coin__TransactionOutput()
    pOut = skycoin.coin__TransactionOutput()
    pOut1.Address = a
    pOut1.Coins = 100
    pOut1.Hours = 150
    assert skycoin.SKY_coin_Transaction_Get_Output_At(
        handle, 0, pOut) == error["SKY_OK"]
    assert pOut == pOut1
    for i in range(1, 20):
        a = transutil.makeAddress()
        assert skycoin.SKY_coin_Transaction_PushOutput(
            handle, a, int(i * 100), int(i * 50)) == error["SKY_OK"]
        err, count = skycoin.SKY_coin_Transaction_Get_Outputs_Count(handle)
        assert err == error["SKY_OK"]
        assert count == int(i + 1)
        pOut1.Address = a
        pOut1.Coins = int(i * 100)
        pOut1.Hours = int(i * 150)
        assert skycoin.SKY_coin_Transaction_Get_Output_At(
            handle, i, pOut) == error["SKY_OK"]
        assert pOut == pOut
        i += 1


def test_TestTransactionSignInputs():
    handle = transutil.makeEmptyTransaction()
    # Panics if txns already signed
    sig = skycoin.cipher_Sig()
    assert skycoin.SKY_coin_Transaction_Push_Signature(
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
    err, count = skycoin.SKY_coin_Transaction_Get_Signatures_Count(handle)
    assert err == error["SKY_OK"]
    assert count == 0
    # Valid signing
    assert skycoin.SKY_coin_Transaction_HashInner(handle, h) == error["SKY_OK"]
    secKeys = []
    secKeys.append(s)
    secKeys.append(s2)
    assert skycoin.SKY_coin_Transaction_SignInputs(
        handle, secKeys) == error["SKY_OK"]
    err, count = skycoin.SKY_coin_Transaction_Get_Signatures_Count(handle)
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
    assert skycoin.SKY_coin_Transaction_Get_Input_At(
        handle, 0, txin0) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_Get_Input_At(
        handle, 1, txin1) == error["SKY_OK"]
    assert skycoin.SKY_cipher_AddSHA256(h, txin0, sha1) == error["SKY_OK"]
    assert skycoin.SKY_cipher_AddSHA256(h, txin1, sha2) == error["SKY_OK"]
    txsig0 = skycoin.cipher_Sig()
    txsig1 = skycoin.cipher_Sig()
    assert skycoin.SKY_coin_Transaction_Get_Signature_At(
        handle, 0, txsig0) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_Get_Signature_At(
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
    ux, _ = transutil.makeUxOut()
    h = skycoin.cipher_SHA256()
    h1 = skycoin.cipher_SHA256()
    assert skycoin.SKY_coin_UxOut_Hash(ux, h) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_Set_Input_At(
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
    assert skycoin.SKY_coin_Transaction_Get_Output_At(
        handle2, 0, pOut) == error["SKY_OK"]
    pOut.Address = a
    assert skycoin.SKY_coin_Transaction_Set_Output_At(
        handle2, 0, pOut) == error["SKY_OK"]
    assert tx != tx2
    assert skycoin.SKY_coin_Transaction_Get_Output_At(
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
    assert skycoin.SKY_coin_Transaction_Push_Signature(
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
    err, tx2 = skycoin.SKY_coin_Get_Transaction_Object(handle2)
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
        handle, transutil.makeAddress(), int(1e6), int(MaxUint64 - 700)) == error["SKY_OK"]
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
