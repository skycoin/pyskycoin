# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package
import skycoin

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

def test_base58hex2base58():
	error, result = skycoin.SKY_base58_Hex2Base58("123X")
	assert error == 0
