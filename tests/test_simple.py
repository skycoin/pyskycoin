# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package
import skycoin

#Test with handles and strings
def test_loadconfig():
	error, old_coin = skycoin.SKY_cli_Getenv("COIN")
	assert error == 0
	error = skycoin.SKY_cli_Setenv("COIN", "foocoin")
	assert error == 0
	error, configHandle = skycoin.SKY_cli_LoadConfig()
	assert error == 0
	error, new_coin = skycoin.SKY_cli_Config_GetCoin( configHandle )
	assert error == 0
	assert new_coin == "foocoin"
	skycoin.SKY_handle_close( configHandle )
	assert True
	error = skycoin.SKY_cli_Setenv("COIN", old_coin)
	assert error == 0

#Test with slices as []byte
def test_Sha256XorEncrypt():
	encrypt = skycoin.encrypt__Sha256Xor()
	error, data = skycoin.SKY_cipher_RandByte(32)
	assert error == 0
	assert len( data ) == 32
	pwd = "pwd"
	error, encrypted = skycoin.SKY_encrypt_Sha256Xor_Encrypt( encrypt, data, pwd )
	assert error == 0
	error, decrypted = skycoin.SKY_encrypt_Sha256Xor_Decrypt( encrypt, encrypted, pwd )
	assert error == 0
	assert data == decrypted

#Test with struct and slices
def test_encrypt_ScryptChacha20poly1305Encrypt():
	encrypt_settings = skycoin.encrypt__ScryptChacha20poly1305()
	encrypt_settings.N = 2
	encrypt_settings.R = 8
	encrypt_settings.P = 1
	encrypt_settings.KeyLen = 32

	error, data = skycoin.SKY_cipher_RandByte(32)
	assert error == 0
	assert len( data ) == 32
	error, encrypted = skycoin.SKY_encrypt_ScryptChacha20poly1305_Encrypt(encrypt_settings, data, "password")
	assert error == 0
	error, decrypted = skycoin.SKY_encrypt_ScryptChacha20poly1305_Decrypt(encrypt_settings, encrypted, "password")
	assert error == 0
	assert data == decrypted

#Test with struct containing array
def test_cipherAddress():
	address = skycoin.cipher__Address()
	error = skycoin.SKY_cipher_DecodeBase58Address("2GgFvqoyk9RjwVzj8tqfcXVXB4orBwoc9qv", address)
	assert error == 0
	error, bytes = skycoin.SKY_cipher_Address_BitcoinBytes(address)
	assert error == 0
	assert len( bytes ) > 0
	address2 = skycoin.cipher__Address()
	error = skycoin.SKY_cipher_BitcoinAddressFromBytes( bytes, address2 )
	assert error == 0
	assert address.isEqual(address2)

#Test with array typedefs. Array typedefs were wrapped inside a struct
#Notice that the type used is cipher_PubKey instead of cipher__PubKey
def test_GenerateKeyPairs():
	error, data = skycoin.SKY_cipher_RandByte(32)
	assert error == 0
	pubkey = skycoin.cipher_PubKey()
	seckey = skycoin.cipher_SecKey()
	error = skycoin.SKY_cipher_GenerateDeterministicKeyPair(data, pubkey, seckey)
	assert error == 0
	address = skycoin.cipher__Address()
	error = skycoin.SKY_cipher_AddressFromPubKey(pubkey, address)
	assert error == 0
	error = skycoin.SKY_cipher_Address_Verify(address, pubkey)
	assert error == 0
	error, address_string = skycoin.SKY_cipher_Address_String( address )
	assert error == 0
	address2 = skycoin.cipher__Address()
	error = skycoin.SKY_cipher_DecodeBase58Address( address_string, address2 )
	assert error == 0
	assert address.isEqual(address2)

def test_GenerateDeterministicKeyPairs():
	error, seed = skycoin.SKY_cipher_RandByte(32)
	assert error == 0
	secKeys = skycoin.cipher_SecKeys()
	secKeys.allocate(2)
	error = skycoin.SKY_cipher_GenerateDeterministicKeyPairs(seed, 2, secKeys)
	assert error == 0
	length = secKeys.count
	assert length == 2
	secKey = secKeys.getAt(0)
	address = skycoin.cipher__Address()
	error = skycoin.SKY_cipher_AddressFromSecKey(secKey, address)
	assert error == 0
	secKey = secKeys.getAt(1)
	address = skycoin.cipher__Address()
	error = skycoin.SKY_cipher_AddressFromSecKey(secKey, address)
	assert error == 0
	secKeys.release()


def test_GenerateDeterministicKeyPairsSeed():
	error, seed = skycoin.SKY_cipher_RandByte(32)
	assert error == 0
	secKeys = skycoin.cipher_SecKeys()
	secKeys.allocate(2)
	error, newseed = skycoin.SKY_cipher_GenerateDeterministicKeyPairsSeed(seed, 2, secKeys)
	assert error == 0
	assert secKeys.count == 2
	secKeys.release()

