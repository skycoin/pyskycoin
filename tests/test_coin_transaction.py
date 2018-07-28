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
    handle, _ = transutil.test_makeTransactionFromUxOut(ux, s)
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
    handle, _ = transutil.test_makeTransactionFromUxOut(ux, s)
    assert skycoin.SKY_coin_Transaction_ResetSignatures(
        handle, 0) == error["SKY_OK"]
    assert skycoin.SKY_coin_Transaction_Push_Signature(
        handle, skycoin.cipher_Sig()) == error["SKY_OK"]
    seckeys = []
    seckeys.append(ux)
    assert skycoin.SKY_coin_Transaction_VerifyInput(
        handle, seckeys) == error["SKY_ERROR"]

    ux, s = transutil.makeUxOutWithSecret()
    handle, _ = transutil.test_makeTransactionFromUxOut(ux, s)
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
    handle, tx = transutil.test_makeTransactionFromUxOut(ux, s)
    skycoin.cipher_SHA256().assignTo(tx.InnerHash)
    seckeys = []
    seckeys.append(ux)
    assert skycoin.SKY_coin_Transaction_VerifyInput(
        handle, seckeys) == error["SKY_ERROR"]

    # tx.In does not match uxIn hashes
    ux, s = transutil.makeUxOutWithSecret()
    handle, tx = transutil.test_makeTransactionFromUxOut(ux, s)
    seckeys = []
    seckeys.append(skycoin.coin__UxOut())
    assert skycoin.SKY_coin_Transaction_VerifyInput(
        handle, seckeys) == error["SKY_ERROR"]
    # Invalid signature
    ux, s = transutil.makeUxOutWithSecret()
    handle, tx = transutil.test_makeTransactionFromUxOut(ux, s)
    sigs = skycoin.cipher_Sig()
    assert skycoin.SKY_coin_Transaction_Set_Signature_At(
        handle, 0, sigs) == error["SKY_OK"]
    seckeys = []
    seckeys.append(ux)
    assert skycoin.SKY_coin_Transaction_VerifyInput(
        handle, seckeys) == error["SKY_ERROR"]

    # Valid
    ux, s = transutil.makeUxOutWithSecret()
    handle, tx = transutil.test_makeTransactionFromUxOut(ux, s)
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
    a = transutil.test_makeAddress()
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
        a = transutil.test_makeAddress()
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
