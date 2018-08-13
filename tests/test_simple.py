# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package
import skycoin


# Test with handles and strings
def test_loadconfig():
    err, old_coin = skycoin.SKY_cli_Getenv(b"COIN")
    assert err == skycoin.SKY_OK
    err = skycoin.SKY_cli_Setenv(b"COIN", b"foocoin")
    assert err == skycoin.SKY_OK
    err, configHandle = skycoin.SKY_cli_LoadConfig()
    assert err == skycoin.SKY_OK
    err, new_coin = skycoin.SKY_cli_Config_GetCoin(configHandle)
    assert err == skycoin.SKY_OK
    assert new_coin == b"foocoin"
    skycoin.SKY_handle_close(configHandle)
    err = skycoin.SKY_cli_Setenv(b"COIN", old_coin)
    assert err == skycoin.SKY_OK


# Test with slices as []byte
def test_Sha256XorEncrypt():
    err, data = skycoin.SKY_cipher_RandByte(32)
    assert err == skycoin.SKY_OK
    assert len(data) == 32
    pwd = b"pwd"
    err, encrypted = skycoin.SKY_encrypt_Sha256Xor_Encrypt(
        data, pwd)
    assert err == skycoin.SKY_OK
    err, decrypted = skycoin.SKY_encrypt_Sha256Xor_Decrypt(
        encrypted, pwd)
    assert err == skycoin.SKY_OK
    assert data == decrypted


# Test with struct and slices
def test_encrypt_ScryptChacha20poly1305Encrypt():
    encrypt_settings = skycoin.encrypt__ScryptChacha20poly1305()
    encrypt_settings.N = 2
    encrypt_settings.R = 8
    encrypt_settings.P = 1
    encrypt_settings.KeyLen = 32

    err, data = skycoin.SKY_cipher_RandByte(32)
    assert err == skycoin.SKY_OK
    assert len(data) == 32
    err, encrypted = skycoin.SKY_encrypt_ScryptChacha20poly1305_Encrypt(
        encrypt_settings, data, b"password")
    assert err == skycoin.SKY_OK
    err, decrypted = skycoin.SKY_encrypt_ScryptChacha20poly1305_Decrypt(
        encrypt_settings, encrypted, b"password")
    assert err == skycoin.SKY_OK
    assert data == decrypted


# Test with struct containing array
def test_cipherAddress():
    address = skycoin.cipher__Address()
    err = skycoin.SKY_cipher_DecodeBase58Address(
        b"2GgFvqoyk9RjwVzj8tqfcXVXB4orBwoc9qv", address)
    assert err == skycoin.SKY_OK

    err, byte = skycoin.SKY_cipher_Address_BitcoinBytes(address)
    assert err == skycoin.SKY_OK
    assert len(byte) > 0
    address2 = skycoin.cipher__Address()
    err = skycoin.SKY_cipher_BitcoinAddressFromBytes(byte, address2)
    assert err == skycoin.SKY_OK
    assert address == address2


# Test with array typedefs. Array typedefs were wrapped inside a struct
# Notice that the type used is cipher_PubKey instead of cipher__PubKey
def test_GenerateKeyPairs():
    err, data = skycoin.SKY_cipher_RandByte(32)
    assert err == skycoin.SKY_OK

    pubkey = skycoin.cipher_PubKey()
    seckey = skycoin.cipher_SecKey()

    err = skycoin.SKY_cipher_GenerateDeterministicKeyPair(
        data, pubkey, seckey)
    assert err == skycoin.SKY_OK

    address = skycoin.cipher__Address()
    err = skycoin.SKY_cipher_AddressFromPubKey(pubkey, address)
    assert err == skycoin.SKY_OK
    err = skycoin.SKY_cipher_Address_Verify(address, pubkey)
    assert err == skycoin.SKY_OK

    err, address_string = skycoin.SKY_cipher_Address_String(address)
    assert err == skycoin.SKY_OK
    address2 = skycoin.cipher__Address()
    err = skycoin.SKY_cipher_DecodeBase58Address(address_string, address2)
    assert err == skycoin.SKY_OK
    assert address == address2


def test_GenerateDeterministicKeyPairs():
    err, seed = skycoin.SKY_cipher_RandByte(32)
    assert err == skycoin.SKY_OK
    err, seckeys = skycoin.SKY_cipher_GenerateDeterministicKeyPairs(seed, 2)
    assert err == skycoin.SKY_OK
    length = len(seckeys)
    assert length == 2
    for seckey in seckeys:
        address = skycoin.cipher__Address()
        err = skycoin.SKY_cipher_AddressFromSecKey(seckey, address)
        assert err == skycoin.SKY_OK
        pubkey = skycoin.cipher_PubKey()
        err = skycoin.SKY_cipher_PubKeyFromSecKey(seckey, pubkey)
        assert err == skycoin.SKY_OK
        err = skycoin.SKY_cipher_PubKey_Verify(pubkey)
        assert err == skycoin.SKY_OK


def test_GenerateDeterministicKeyPairsSeed():
    err, seed = skycoin.SKY_cipher_RandByte(32)
    assert err == skycoin.SKY_OK
    err, newseed, seckeys = skycoin.SKY_cipher_GenerateDeterministicKeyPairsSeed(
        seed, 2)
    length = len(seckeys)
    assert length == 2


def test_Transaction():
    err, handle = skycoin.SKY_coin_Create_Transaction()
    assert err == skycoin.SKY_OK
    pubkey = skycoin.cipher_PubKey()
    seckey = skycoin.cipher_SecKey()
    err = skycoin.SKY_cipher_GenerateKeyPair(pubkey, seckey)
    assert err == skycoin.SKY_OK
    address = skycoin.cipher__Address()
    err = skycoin.SKY_cipher_AddressFromPubKey(pubkey, address)
    assert err == skycoin.SKY_OK
    err = skycoin.SKY_coin_Transaction_PushOutput(
        handle, address, 1000000, 100)
    assert err == skycoin.SKY_OK
    err, transaction = skycoin.SKY_coin_GetTransactionObject(handle)
    assert err == skycoin.SKY_OK
    assert transaction.Length >= 0
    skycoin.SKY_handle_close(handle)


def __feeCalculator(transaction):
    err, outCount = skycoin.SKY_coin_Transaction_GetOutputsCount(transaction)
    assert err == skycoin.SKY_OK
    if outCount > 0:
        output = skycoin.coin__TransactionOutput()
        err = skycoin.SKY_coin_Transaction_GetOutputAt(transaction, 0, output)
        assert err == skycoin.SKY_OK
        return 0, output.Hours
    return 0, 0


def __badFeeCalculator(transaction):
    return 1, 0


def test_Transactions():
    err, handleTransactions = skycoin.SKY_coin_Create_Transactions()
    assert err == skycoin.SKY_OK
    err, handleTransaction1 = skycoin.SKY_coin_Create_Transaction()
    assert err == skycoin.SKY_OK
    skycoin.SKY_coin_Transactions_Add(handleTransactions, handleTransaction1)
    err, handleTransaction2 = skycoin.SKY_coin_Create_Transaction()
    assert err == skycoin.SKY_OK
    pubkey = skycoin.cipher_PubKey()
    seckey = skycoin.cipher_SecKey()
    err = skycoin.SKY_cipher_GenerateKeyPair(pubkey, seckey)
    assert err == skycoin.SKY_OK
    address = skycoin.cipher__Address()
    err = skycoin.SKY_cipher_AddressFromPubKey(pubkey, address)
    assert err == skycoin.SKY_OK
    err = skycoin.SKY_coin_Transaction_PushOutput(
        handleTransaction2, address, 1000000, 100)
    assert err == skycoin.SKY_OK
    skycoin.SKY_coin_Transactions_Add(handleTransactions, handleTransaction2)
    err, fees = skycoin.SKY_coin_Transactions_Fees(
        handleTransactions, __feeCalculator)
    assert err == skycoin.SKY_OK
    assert fees == 100
    err, fees = skycoin.SKY_coin_Transactions_Fees(
        handleTransactions, __badFeeCalculator)
    assert err != 0
    skycoin.SKY_handle_close(handleTransaction1)
    skycoin.SKY_handle_close(handleTransaction2)
    skycoin.SKY_handle_close(handleTransactions)


def test_Transactions2():
    err, handleTransaction1 = skycoin.SKY_coin_Create_Transaction()
    assert err == skycoin.SKY_OK
    err, handleTransaction2 = skycoin.SKY_coin_Create_Transaction()
    assert err == skycoin.SKY_OK
    err, transaction1 = skycoin.SKY_coin_GetTransactionObject(
        handleTransaction1)
    assert err == skycoin.SKY_OK
    err, transaction2 = skycoin.SKY_coin_GetTransactionObject(
        handleTransaction2)
    assert err == skycoin.SKY_OK
    assert transaction1 == transaction2
    pubkey = skycoin.cipher_PubKey()
    seckey = skycoin.cipher_SecKey()
    err = skycoin.SKY_cipher_GenerateKeyPair(pubkey, seckey)
    assert err == skycoin.SKY_OK
    address = skycoin.cipher__Address()
    err = skycoin.SKY_cipher_AddressFromPubKey(pubkey, address)
    assert err == skycoin.SKY_OK
    err = skycoin.SKY_coin_Transaction_PushOutput(
        handleTransaction1, address, 1000000, 100)
    assert err == skycoin.SKY_OK
    assert not (transaction1 == transaction2)
    output = skycoin.coin__TransactionOutput()
    assert err == skycoin.SKY_OK
    err = skycoin.SKY_coin_Transaction_GetOutputAt(
        handleTransaction1, 0, output)
    skycoin.SKY_handle_close(handleTransaction1)
    skycoin.SKY_handle_close(handleTransaction2)


def test_SHA256NULL():
    sha256 = skycoin.cipher_SHA256()
    err, result = skycoin.SKY_cipher_SHA256_Null(sha256)
    assert err == skycoin.SKY_OK
    assert result == True


def test_Number():
    err, number = skycoin.SKY_secp256k1go_Number_Create()
    assert err == skycoin.SKY_OK
    err = skycoin.SKY_secp256k1go_Number_SetHex(
        number, b"6028b9e3a31c9e725fcbd7d5d16736aaaafcc9bf157dfb4be62bcbcf0969d488")
    assert err == skycoin.SKY_OK
    err, sig = skycoin.SKY_secp256k1go_Signature_Create()
    assert err == skycoin.SKY_OK
    err, r = skycoin.SKY_secp256k1go_Signature_GetR(sig)
    assert err == skycoin.SKY_OK
    err = skycoin.SKY_secp256k1go_Number_SetHex(
        r, b"6028b9e3a31c9e725fcbd7d5d16736aaaafcc9bf157dfb4be62bcbcf0969d488")
    assert err == skycoin.SKY_OK


def test_UxBody():
    uxbody = skycoin.coin__UxBody()
    uxbody.Address.Version = 45
    sha256 = skycoin.cipher_SHA256()
    x = sha256.toStr()
    sha256.assignFrom(uxbody.SrcTransaction)
    sha256.assignTo(uxbody.SrcTransaction)


def test_SecKeysList():
    seckeysList = []
    # Generate pubkeys and seckeys
    # then add seckeys to lists
    err, data = skycoin.SKY_cipher_RandByte(32)
    assert err == skycoin.SKY_OK
    pubkey = skycoin.cipher_PubKey()
    seckey = skycoin.cipher_SecKey()
    err = skycoin.SKY_cipher_GenerateDeterministicKeyPair(
        data, pubkey, seckey)
    assert err == skycoin.SKY_OK
    err, data = skycoin.SKY_cipher_RandByte(32)
    assert err == skycoin.SKY_OK
    seckeysList.append(seckey)
    pubkey = skycoin.cipher_PubKey()
    seckey = skycoin.cipher_SecKey()
    err = skycoin.SKY_cipher_GenerateDeterministicKeyPair(
        data, pubkey, seckey)
    assert err == skycoin.SKY_OK
    seckeysList.append(seckey)
    err, handleTransaction = skycoin.SKY_coin_Create_Transaction()
    assert err == skycoin.SKY_OK
    # Add as many inputs as keys
    sha256 = skycoin.cipher_SHA256()
    err, r = skycoin.SKY_coin_Transaction_PushInput(
        handleTransaction, sha256)
    assert err == skycoin.SKY_OK
    sha256 = skycoin.cipher_SHA256()
    err, r = skycoin.SKY_coin_Transaction_PushInput(
        handleTransaction, sha256)
    assert err == skycoin.SKY_OK
    skycoin.SKY_coin_Transaction_ResetSignatures(handleTransaction, 0)
    err = skycoin.SKY_coin_Transaction_SignInputs(
        handleTransaction, seckeysList)
    assert err == skycoin.SKY_OK
    skycoin.SKY_handle_close(handleTransaction)


def test_UxOutList_CoinsHoursSpending():
    million = 1000000
    uxInList = []
    in1 = skycoin.coin__UxOut()
    in1.Body.Coins = 10 * million
    in1.Body.Hours = 10
    uxInList.append(in1)
    in2 = skycoin.coin__UxOut()
    in2.Body.Coins = 15 * million
    in2.Body.Hours = 10
    uxInList.append(in2)
    uxOutList = []
    out1 = skycoin.coin__UxOut()
    out1.Body.Coins = 10 * million
    out1.Body.Hours = 11
    uxOutList.append(out1)
    out2 = skycoin.coin__UxOut()
    out2.Body.Coins = 10 * million
    out2.Body.Hours = 1
    uxOutList.append(out2)
    out3 = skycoin.coin__UxOut()
    out3.Body.Coins = 5 * million
    out3.Body.Hours = 0
    uxOutList.append(out3)
    err = skycoin.SKY_coin_VerifyTransactionCoinsSpending(
        uxInList, uxOutList)
    assert err == skycoin.SKY_OK
    err = skycoin.SKY_coin_VerifyTransactionHoursSpending(
        0, uxInList, uxOutList)
    assert err == skycoin.SKY_OK


def test_UxOutList_CreateUnspent():
    pubkey = skycoin.cipher_PubKey()
    seckey = skycoin.cipher_SecKey()
    address = skycoin.cipher__Address()
    skycoin.SKY_cipher_GenerateKeyPair(pubkey, seckey)
    err = skycoin.SKY_cipher_AddressFromPubKey(pubkey, address)
    assert err == skycoin.SKY_OK
    err, transactionHandle = skycoin.SKY_coin_Create_Transaction()
    assert err == skycoin.SKY_OK
    err = skycoin.SKY_coin_Transaction_PushOutput(
        transactionHandle, address, 11000000, 255)
    assert err == skycoin.SKY_OK
    bh = skycoin.coin__BlockHeader()
    bh.Time = 0
    bh.BkSeq = 1
    err, unspents = skycoin.SKY_coin_CreateUnspents(bh, transactionHandle)
    assert err == skycoin.SKY_OK
    assert len(unspents) == 1
    err, outputsCount = skycoin.SKY_coin_Transaction_GetOutputsCount(
        transactionHandle)
    assert err == skycoin.SKY_OK
    assert outputsCount == len(unspents)
    i = 0
    for unspent in unspents:
        assert unspent.Head.Time == bh.Time
        assert unspent.Head.BkSeq == bh.BkSeq
        output = skycoin.coin__TransactionOutput()
        skycoin.SKY_coin_Transaction_GetOutputAt(transactionHandle, i, output)
        assert unspent.Body.Coins == output.Coins
        assert unspent.Body.Hours == output.Hours
        hash = skycoin.cipher_SHA256()
        err = skycoin.SKY_coin_Transaction_Hash(transactionHandle, hash)
        assert err == skycoin.SKY_OK
        hash2 = skycoin.cipher_SHA256()
        hash2.assignFrom(unspent.Body.SrcTransaction)
        assert hash == hash2
        assert unspent.Body.Address == output.Address
        i += 1
    skycoin.SKY_handle_close(transactionHandle)


def test_Transaction_Hashes():
    err, handleTransactions = skycoin.SKY_coin_Create_Transactions()
    assert err == skycoin.SKY_OK
    err, handleTransaction1 = skycoin.SKY_coin_Create_Transaction()
    assert err == skycoin.SKY_OK
    skycoin.SKY_coin_Transactions_Add(handleTransactions, handleTransaction1)
    err, handleTransaction2 = skycoin.SKY_coin_Create_Transaction()
    assert err == skycoin.SKY_OK
    pubkey = skycoin.cipher_PubKey()
    seckey = skycoin.cipher_SecKey()
    address = skycoin.cipher__Address()
    error = skycoin.SKY_cipher_GenerateKeyPair(pubkey, seckey)
    assert error == 0
    error = skycoin.SKY_cipher_AddressFromPubKey(pubkey, address)
    assert error == 0
    error = skycoin.SKY_coin_Transaction_PushOutput(handleTransaction2, address, 11000000, 255)
    assert error == 0
    skycoin.SKY_coin_Transactions_Add(handleTransactions, handleTransaction2)
    err, hashesList = skycoin.SKY_coin_Transactions_Hashes(
        handleTransactions)
    assert err == skycoin.SKY_OK
    assert len(hashesList) == 2
    h1 = skycoin.cipher_SHA256()
    h2 = skycoin.cipher_SHA256()
    assert h1 == h2
    for hash in hashesList:
        h = skycoin.cipher_SHA256()
        assert not (h == hash)
    error = skycoin.SKY_coin_Transaction_Hash(handleTransaction1, h1)
    assert error == 0
    error = skycoin.SKY_coin_Transaction_Hash(handleTransaction1, h2)
    assert error == 0
    assert h1 == h2
    error = skycoin.SKY_coin_Transaction_Hash(handleTransaction2, h2)
    assert error == 0
    assert not (h1 == h2)
    
def test_coinUxArray_Sort():
    million = 1000000
    uxInList = []
    in1 = skycoin.coin__UxOut()
    in1.Body.Coins = 10 * million
    in1.Body.Hours = 10
    uxInList.append(in1)
    in2 = skycoin.coin__UxOut()
    in2.Body.Coins = 15 * million
    in2.Body.Hours = 10
    uxInList.append(in2)
    assert not (in1 == in2)
    error, sortedList = skycoin.SKY_coin_UxArray_Sort(uxInList)
    assert error == 0
    assert len(sortedList) == 2
    error, uxAddressOutHandle = skycoin.SKY_coin_NewAddressUxOuts(uxInList)
    assert error == 0
    address = skycoin.cipher__Address()
    error = skycoin.SKY_cipher_DecodeBase58Address(b"2GgFvqoyk9RjwVzj8tqfcXVXB4orBwoc9qv", address)
    assert error == 0
    error = skycoin.SKY_coin_AddressUxOuts_Set(uxAddressOutHandle, address, uxInList)
    assert error == 0
    error, uxList = skycoin.SKY_coin_AddressUxOuts_Get(uxAddressOutHandle, address)
    assert error == 0
    assert len(uxList) == 2
    error, keys = skycoin.SKY_coin_AddressUxOuts_Keys(uxAddressOutHandle)
    assert error == 0
    assert len(keys) > 0
    keyFound = False
    for key in keys:
        if key == address:
            keyFound = True
    assert keyFound
