import skycoin

def test_success():
	old_coin, error = skycoin.SKY_cli_Getenv("COIN")
	assert error == 0
	print old_coin
	error = skycoin.SKY_cli_Setenv("COIN", "foocoin")
	assert error == 0
	new_coin, error = skycoin.SKY_cli_Getenv("COIN")
	assert error == 0
	print new_coin
	error = skycoin.SKY_cli_Setenv("COIN", old_coin)
	assert error == 0
	r, error = skycoin.SKY_file_UserHome()
	print r
test_success()
