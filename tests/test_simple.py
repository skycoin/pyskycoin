# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package
import skycoin

def test_success():
	old_coin, error = skycoin.SKY_cli_Getenv("COIN")
	assert error == 0
	error = skycoin.SKY_cli_Setenv("COIN", "foocoin")
	assert error == 0
	configHandle, error = skycoin.SKY_cli_LoadConfig()
	assert error == 0
	new_coin, error = skycoin.SKY_cli_Config_GetCoin( configHandle )
	assert error == 0
	assert new_coin == "foocoin"
	skycoin.SKY_handle_close( configHandle )
	assert True
	error = skycoin.SKY_cli_Setenv("COIN", old_coin)
	assert error == 0

'''
def test_success():
	result = skycoin.SKY_file_InitDataDir("test")
	print result
	
	s1 = skycoin.GoString()
	s1.p = "test"
	s1.n = 4
	s2 = skycoin.GoString_()
	result = skycoin.SKY_file_InitDataDir(s1, s2)
	
	print s2.p
	print result
	assert True
'''
