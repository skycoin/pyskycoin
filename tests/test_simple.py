# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package
import skycoin
import sys

# Test with handles and strings
def test_loadconfig():
    error, old_coin = skycoin.SKY_cli_Getenv(b"COIN")
    assert error == 0
    error = skycoin.SKY_cli_Setenv(b"COIN", b"foocoin")
    assert error == 0
    error, configHandle = skycoin.SKY_cli_LoadConfig()
    assert error == 0
    error, new_coin = skycoin.SKY_cli_Config_GetCoin(configHandle)
    assert error == 0
    assert new_coin == b"foocoin"
    skycoin.SKY_handle_close(configHandle)
    error = skycoin.SKY_cli_Setenv(b"COIN", old_coin)
    assert error == 0


# Test with slices as []byte
def test_Sha256XorEncrypt():
    error, data = skycoin.SKY_cipher_RandByte(32)
    assert error == 0
    assert len(data) == 32
    pwd = b"pwd"
    error, encrypted = skycoin.SKY_encrypt_Sha256Xor_Encrypt(
            data, pwd)
    assert error == 0
    error, decrypted = skycoin.SKY_encrypt_Sha256Xor_Decrypt(
            encrypted, pwd)
    assert error == 0
    assert data == decrypted


# Test with struct and slices
def test_encrypt_ScryptChacha20poly1305Encrypt():
    encrypt_settings = skycoin.encrypt__ScryptChacha20poly1305()
    encrypt_settings.N = 2
    encrypt_settings.R = 8
    encrypt_settings.P = 1
    encrypt_settings.KeyLen = 32

    error, data = skycoin.SKY_cipher_RandByte(32)
    assert error == 0
    assert len(data) == 32
    error, encrypted = skycoin.SKY_encrypt_ScryptChacha20poly1305_Encrypt(
            encrypt_settings, data, b"password")
    assert error == 0
    error, decrypted = skycoin.SKY_encrypt_ScryptChacha20poly1305_Decrypt(
            encrypt_settings, encrypted, b"password")
    assert error == 0
    assert data == decrypted


# Test with struct containing array
def test_cipherAddress():
    address = skycoin.cipher__Address()
    error = skycoin.SKY_cipher_DecodeBase58Address(
            b"2GgFvqoyk9RjwVzj8tqfcXVXB4orBwoc9qv", address)
    assert error == 0
    
    error, bytes = skycoin.SKY_cipher_Address_BitcoinBytes(address)
    assert error == 0
    assert len(bytes) > 0
    address2 = skycoin.cipher__Address()
    error = skycoin.SKY_cipher_BitcoinAddressFromBytes(bytes, address2)
    assert error == 0
    assert address == address2



# Test with array typedefs. Array typedefs were wrapped inside a struct
# Notice that the type used is cipher_PubKey instead of cipher__PubKey
def test_GenerateKeyPairs():
    error, data = skycoin.SKY_cipher_RandByte(32)
    assert error == 0
    
    pubkey = skycoin.cipher_PubKey()
    seckey = skycoin.cipher_SecKey()
    
    error = skycoin.SKY_cipher_GenerateDeterministicKeyPair(
            data, pubkey, seckey)
    assert error == 0
    
    address = skycoin.cipher__Address()
    error = skycoin.SKY_cipher_AddressFromPubKey(pubkey, address)
    assert error == 0
    error = skycoin.SKY_cipher_Address_Verify(address, pubkey)
    assert error == 0
    
    error, address_string = skycoin.SKY_cipher_Address_String(address)
    assert error == 0
    address2 = skycoin.cipher__Address()
    error = skycoin.SKY_cipher_DecodeBase58Address(address_string, address2)
    assert error == 0
    assert address == address2
    

def test_GenerateDeterministicKeyPairs():
    error, seed = skycoin.SKY_cipher_RandByte(32)
    assert error == 0
    error, seckeys = skycoin.SKY_cipher_GenerateDeterministicKeyPairs(seed, 2)
    assert error == 0
    length = len(seckeys)
    assert length == 2
    for seckey in seckeys:
        address = skycoin.cipher__Address()
        error = skycoin.SKY_cipher_AddressFromSecKey(seckey, address)
        assert error == 0
        pubkey = skycoin.cipher_PubKey()
        error = skycoin.SKY_cipher_PubKeyFromSecKey(seckey, pubkey)
        assert error == 0
        error = skycoin.SKY_cipher_PubKey_Verify(pubkey)
        assert error == 0


def test_GenerateDeterministicKeyPairsSeed():
    error, seed = skycoin.SKY_cipher_RandByte(32)
    assert error == 0
    error, newseed, seckeys = \
            skycoin.SKY_cipher_GenerateDeterministicKeyPairsSeed(seed, 2)
    length = len(seckeys)
    assert length == 2

def test_Transaction():
	error, handle = skycoin.SKY_coin_Create_Transaction()
	assert error == 0
	pubkey = skycoin.cipher_PubKey()
	seckey = skycoin.cipher_SecKey()
	error  = skycoin.SKY_cipher_GenerateKeyPair(pubkey, seckey)
	assert error == 0
	address = skycoin.cipher__Address()
	error = skycoin.SKY_cipher_AddressFromPubKey(pubkey, address)
	assert error == 0
	error = skycoin.SKY_coin_Transaction_PushOutput(handle, address, 1000000, 100)
	assert error == 0
	error, transaction = skycoin.SKY_coin_Get_Transaction_Object(handle)
	assert error == 0
	assert transaction.Length >= 0
	skycoin.SKY_handle_close(handle)
	
	
def __feeCalculator(transaction):
	error, outCount = skycoin.SKY_coin_Transaction_Get_Outputs_Count(transaction)
	assert error == 0
	if outCount > 0:
		output = skycoin.coin__TransactionOutput()
		error = skycoin.SKY_coin_Transaction_Get_Output_At(transaction, 0, output )
		assert error == 0
		return 0, output.Hours
	return 0, 0	
	
def __badFeeCalculator(transaction):
	return 1, 0
	
def test_Transactions():
	error, handleTransactions = skycoin.SKY_coin_Create_Transactions()
	assert error == 0
	error, handleTransaction1 = skycoin.SKY_coin_Create_Transaction()
	assert error == 0
	skycoin.SKY_coin_Transactions_Add(handleTransactions, handleTransaction1)
	error, handleTransaction2 = skycoin.SKY_coin_Create_Transaction()
	assert error == 0
	pubkey = skycoin.cipher_PubKey()
	seckey = skycoin.cipher_SecKey()
	error  = skycoin.SKY_cipher_GenerateKeyPair(pubkey, seckey)
	assert error == 0
	address = skycoin.cipher__Address()
	error = skycoin.SKY_cipher_AddressFromPubKey(pubkey, address)
	assert error == 0
	error = skycoin.SKY_coin_Transaction_PushOutput(handleTransaction2, address, 1000000, 100)
	assert error == 0
	skycoin.SKY_coin_Transactions_Add(handleTransactions, handleTransaction2)
	error, fees = skycoin.SKY_coin_Transactions_Fees(handleTransactions, __feeCalculator)
	assert error == 0
	assert fees == 100
	error, fees = skycoin.SKY_coin_Transactions_Fees(handleTransactions, __badFeeCalculator)
	assert error != 0
	skycoin.SKY_handle_close(handleTransaction1)
	skycoin.SKY_handle_close(handleTransaction2)
	skycoin.SKY_handle_close(handleTransactions)
	
def test_Transactions2():
	error, handleTransaction1 = skycoin.SKY_coin_Create_Transaction()
	assert error == 0
	error, handleTransaction2 = skycoin.SKY_coin_Create_Transaction()
	assert error == 0
	error, transaction1 = skycoin.SKY_coin_Get_Transaction_Object(handleTransaction1)
	assert error == 0
	error, transaction2 = skycoin.SKY_coin_Get_Transaction_Object(handleTransaction2)
	assert error == 0
	assert transaction1 == transaction2
	pubkey = skycoin.cipher_PubKey()
	seckey = skycoin.cipher_SecKey()
	error  = skycoin.SKY_cipher_GenerateKeyPair(pubkey, seckey)
	assert error == 0
	address = skycoin.cipher__Address()
	error = skycoin.SKY_cipher_AddressFromPubKey(pubkey, address)
	assert error == 0
	error = skycoin.SKY_coin_Transaction_PushOutput(handleTransaction1, address, 1000000, 100)
	assert error == 0
	assert not (transaction1 == transaction2)
	output = skycoin.coin__TransactionOutput()
	assert error == 0
	error = skycoin.SKY_coin_Transaction_Get_Output_At(handleTransaction1, 0, output)
	skycoin.SKY_handle_close(handleTransaction1)
	skycoin.SKY_handle_close(handleTransaction2)
	
	
def test_SHA256NULL():
	sha256 = skycoin.cipher_SHA256()
	error, result = skycoin.SKY_cipher_SHA256_Null(sha256)
	assert error == 0
	assert result == True
	
def test_Number():
	error, number = skycoin.SKY_secp256k1go_Number_Create()
	assert error == 0
	error = skycoin.SKY_secp256k1go_Number_SetHex( number, b"6028b9e3a31c9e725fcbd7d5d16736aaaafcc9bf157dfb4be62bcbcf0969d488" )
	assert error == 0
	error, sig = skycoin.SKY_secp256k1go_Signature_Create()
	assert error == 0
	error, r = skycoin.SKY_secp256k1go_Signature_Get_R(sig)
	assert error == 0
	error = skycoin.SKY_secp256k1go_Number_SetHex( r, b"6028b9e3a31c9e725fcbd7d5d16736aaaafcc9bf157dfb4be62bcbcf0969d488" )
	assert error == 0
	
def test_UxBody():
	uxbody = skycoin.coin__UxBody()
	uxbody.Address.Version = 45
	sha256 = skycoin.cipher_SHA256()
	x = sha256.toStr()
	sha256.assignFrom( uxbody.SrcTransaction )
	sha256.assignTo( uxbody.SrcTransaction )

def test_SecKeysList():
	seckeysList = []    
	#Generate pubkeys and seckeys
	#then add seckeys to lists
	error, data = skycoin.SKY_cipher_RandByte(32)
	assert error == 0
	pubkey = skycoin.cipher_PubKey()
	seckey = skycoin.cipher_SecKey()
	error = skycoin.SKY_cipher_GenerateDeterministicKeyPair(
		    data, pubkey, seckey)
	assert error == 0	
	error, data = skycoin.SKY_cipher_RandByte(32)
	assert error == 0
	seckeysList.append(seckey)
	pubkey = skycoin.cipher_PubKey()
	seckey = skycoin.cipher_SecKey()
	error = skycoin.SKY_cipher_GenerateDeterministicKeyPair(
		    data, pubkey, seckey)
	assert error == 0	
	seckeysList.append(seckey)
	error, handleTransaction = skycoin.SKY_coin_Create_Transaction()
	assert error == 0	
	#Add as many inputs as keys
	sha256 = skycoin.cipher_SHA256()
	error, r = skycoin.SKY_coin_Transaction_PushInput(handleTransaction, sha256)
	assert error == 0
	sha256 = skycoin.cipher_SHA256()
	error, r = skycoin.SKY_coin_Transaction_PushInput(handleTransaction, sha256)
	assert error == 0
	skycoin.SKY_coin_Transaction_ResetSignatures(handleTransaction, 0)
	error = skycoin.SKY_coin_Transaction_SignInputs(handleTransaction, seckeysList)
	assert error == 0
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
	error = skycoin.SKY_coin_VerifyTransactionCoinsSpending(uxInList, uxOutList)
	assert error == 0
	error = skycoin.SKY_coin_VerifyTransactionHoursSpending(0, uxInList, uxOutList)
	assert error == 0

def test_UxOutList_CreateUnspent():
	pubkey = skycoin.cipher_PubKey()
	seckey = skycoin.cipher_SecKey()
	address = skycoin.cipher__Address()
	error = skycoin.SKY_cipher_GenerateKeyPair(pubkey, seckey)
	assert error == 0
	error = skycoin.SKY_cipher_AddressFromPubKey(pubkey, address)
	assert error == 0
	error, transactionHandle = skycoin.SKY_coin_Create_Transaction()
	assert error == 0
	error = skycoin.SKY_coin_Transaction_PushOutput(transactionHandle, address, 11000000, 255)
	assert error == 0
	bh = skycoin.coin__BlockHeader()
	bh.Time = 0
	bh.BkSeq = 1
	error,  unspents = skycoin.SKY_coin_CreateUnspents(bh, transactionHandle)
	assert error == 0
	assert len(unspents) == 1
	error, outputsCount = skycoin.SKY_coin_Transaction_Get_Outputs_Count(transactionHandle)
	assert error == 0
	assert outputsCount == len(unspents)
	i = 0
	for unspent in unspents:
		assert unspent.Head.Time == bh.Time
		assert unspent.Head.BkSeq == bh.BkSeq
		output = skycoin.coin__TransactionOutput()
		skycoin.SKY_coin_Transaction_Get_Output_At(transactionHandle, i, output)
		assert unspent.Body.Coins == output.Coins
		assert unspent.Body.Hours == output.Hours
		hash = skycoin.cipher_SHA256()
		error = skycoin.SKY_coin_Transaction_Hash(transactionHandle, hash)
		assert error == 0
		hash2 = skycoin.cipher_SHA256()
		hash2.assignFrom(unspent.Body.SrcTransaction)
		assert hash == hash2
		assert unspent.Body.Address == output.Address
		i += 1
	skycoin.SKY_handle_close(transactionHandle)
		
def test_VerifyInput():
	million = 1000000
	error, transactionHandle = skycoin.SKY_coin_Create_Transaction()	
	uxInList = []
	in1 = skycoin.coin__UxOut()
	in1.Body.Coins = 10 * million
	in1.Body.Hours = 10
	uxInList.append(in1)
	in2 = skycoin.coin__UxOut()
	in2.Body.Coins = 15 * million
	in2.Body.Hours = 10
	uxInList.append(in2)	
	error, coins = skycoin.SKY_coin_UxArray_Coins(uxInList)
	assert error == 0
	assert coins == 25 * million
	error = skycoin.SKY_coin_Transaction_VerifyInput(transactionHandle, uxInList)	
