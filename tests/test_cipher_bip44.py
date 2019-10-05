import skycoin
import tests.utils as utils


CoinTypeBitcoin = 0
CoinTypeBitcoinTestnet = 1
CoinTypeSkycoin = 8000
ExternalChainIndex = 0
ChangeChainIndex = 1
FirstHardenedChild = 0x80000000


def mustDefaultSeed():
    mnemonic = b'dizzy cigar grant ramp inmate uniform gold success able payment faith practice'
    passphrase = b''
    err, seed = skycoin.SKY_bip39_NewSeed(mnemonic, passphrase)
    err, strs = skycoin.SKY_base58_Hex2String(seed)
    assert strs == b'24e563fb095d766df3862c70432cc1b2210b24d232da69af7af09d2ec86d28782ce58035bae29994c84081836aebe36a9b46af1578262fefc53e37efbe94be57'
    return seed


def test_TestNewCoin():
    err, tmp = skycoin.SKY_cipher_RandByte(3)
    assert err == skycoin.SKY_OK
    err, coin = skycoin.SKY_bip44_NewCoin(tmp, CoinTypeBitcoin)
    assert err == skycoin.SKY_ErrInvalidSeedLength
    bad = mustDefaultSeed()
    err, coin = skycoin.SKY_bip44_NewCoin(bad, FirstHardenedChild)
    assert err == skycoin.SKY_ErrInvalidCoinType
    err, coin = skycoin.SKY_bip44_NewCoin(bad, FirstHardenedChild + 1)
    assert err == skycoin.SKY_ErrInvalidCoinType

    err, c = skycoin.SKY_bip44_NewCoin(bad, CoinTypeBitcoin)
    assert err == skycoin.SKY_OK

    err, account = skycoin.SKY_bip44_Coin_Account(c, 0)
    assert err == skycoin.SKY_OK
    err, acc_string = skycoin.SKY_bip44_Account_String(account)
    assert err == skycoin.SKY_OK
    assert acc_string == b'xprv9yKAFQtFghZSe4mfdpdqFm1WWmGeQbYMB4MSGUB85zbKGQgSxty4duZb8k6hNoHVd2UR7Y3QhWU3rS9wox9ewgVG7gDLyYTL4yzEuqUCjvF'
    err, privk = skycoin.SKY_bip44_Account_GetPrivateKey(account)
    assert err == skycoin.SKY_OK
    err, pubk = skycoin.SKY_bip32_PrivateKey_Publickey(privk)
    assert err == skycoin.SKY_OK
    err, pubk_string = skycoin.SKY_bip32_PublicKey_String(pubk)
    assert pubk_string == b'xpub6CJWevR9X57jrYr8jrAqctxF4o78p4GCYHH34rajeL8J9D1bWSHKBht4yzwiTQ4FP4HyQpx99iLxvU54rbEbcxBUgxzTGGudBVXb1N2gcHF'

    err, account = skycoin.SKY_bip44_Coin_Account(c, 1)
    assert err == skycoin.SKY_OK
    err, acc_string = skycoin.SKY_bip44_Account_String(account)
    assert err == skycoin.SKY_OK
    assert acc_string == b'xprv9yKAFQtFghZSgShGXkxHsYQfFaqMyutf3izng8tV4Tmp7gidQUPB8kCuv66yukidivM2oSaUvGus8ffnYvYKChB7DME2H2AvUq8LM2rXUzF'
    err, privk = skycoin.SKY_bip44_Account_GetPrivateKey(account)
    assert err == skycoin.SKY_OK
    err, pubk = skycoin.SKY_bip32_PrivateKey_Publickey(privk)
    assert err == skycoin.SKY_OK
    err, pubk_string = skycoin.SKY_bip32_PublicKey_String(pubk)
    assert err == skycoin.SKY_OK
    assert pubk_string == b'xpub6CJWevR9X57jtvmjdnVJEgMPocfrPNcWQwvPUXJ6coJnzV3mx1hRgYXPmQJh5vLQvrVCY8LtJB5xLLiPJVmpSwBe2yhonQLoQuSsCF8YPLN'

    err, _ = skycoin.SKY_bip44_Coin_Account(c, 0x80000000)
    assert err == skycoin.SKY_ErrInvalidAccount
    err, _ = skycoin.SKY_bip44_Coin_Account(c, 0x80000001)
    assert err == skycoin.SKY_ErrInvalidAccount

    err, external = skycoin.SKY_bip44_Account_External(account)
    assert err == skycoin.SKY_OK
    err, privk_string = skycoin.SKY_bip32_PrivateKey_String(external)
    assert err == skycoin.SKY_OK
    assert privk_string == b'xprv9zjsvjLiqSerDzbeRXPeXwz8tuQ7eRUABkgFAgLPHw1KzGKkgBhJhGaMYHM8j2KDXBZTCv4m19qjxrrD7gusrtdpZ7xzJywdXHaMZEjf3Uv'
    err, pubk = skycoin.SKY_bip32_PrivateKey_Publickey(external)
    assert err == skycoin.SKY_OK
    err, pubk_string = skycoin.SKY_bip32_PublicKey_String(pubk)
    assert err == skycoin.SKY_OK
    assert pubk_string == b'xpub6DjELEscfpD9SUg7XYveu5vsSwEc3tC1Yybqy4jzrGYJs4euDj1ZF4tqPZYvViMn9cvBobHyubuuh69PZ1szaBBx5oxPiQzD492B6C4QDHe'

    err, external0 = skycoin.SKY_bip32_PrivateKey_NewPublicChildKey(
        external, 0)
    assert err == skycoin.SKY_OK
    err, Key = skycoin.SKY_bip32_PublicKey_GetKey(external0)
    assert err == skycoin.SKY_OK
    err, KeyStr = skycoin.SKY_base58_Hex2String(Key)
    assert err == skycoin.SKY_OK
    assert KeyStr == b'034d36f3bcd74e19204e75b81b9c0726e41b799858b92bab73f4cd7498308c5c8b'

    err, external1 = skycoin.SKY_bip32_PrivateKey_NewPublicChildKey(
        external, 1)
    assert err == skycoin.SKY_OK
    err, Key1 = skycoin.SKY_bip32_PublicKey_GetKey(external1)
    assert err == skycoin.SKY_OK
    err, Key1Str = skycoin.SKY_base58_Hex2String(Key1)
    assert err == skycoin.SKY_OK
    assert Key1Str == b'02f7309e9f559d847ee9cc9ee144cfa490791e33e908fdbde2dade50a389408b01'

    err, change = skycoin.SKY_bip44_Account_Change(account)
    assert err == skycoin.SKY_OK
    err, privk_string = skycoin.SKY_bip32_PrivateKey_String(change)
    assert err == skycoin.SKY_OK
    assert privk_string == b'xprv9zjsvjLiqSerGzJyBrpZgCaGpQCeFDnZEuAV714WigmFyHT4nFLhZLeuHzLNE19PgkZeQ5Uf2pjFZjQTHbkugDbmw5TAPAvgo2jsaTnZo2A'
    err, pubk = skycoin.SKY_bip32_PrivateKey_Publickey(change)
    assert err == skycoin.SKY_OK
    err, pubk_string = skycoin.SKY_bip32_PublicKey_String(pubk)
    assert err == skycoin.SKY_OK
    assert pubk_string == b'xpub6DjELEscfpD9VUPSHtMa3LX1NS38egWQc865uPU8H2JEr5nDKnex78yP9GxhFr5cnCRgiQF1dkv7aR7moraPrv73KHwSkDaXdWookR1Sh9p'

    err, change0 = skycoin.SKY_bip32_PrivateKey_NewPublicChildKey(change, 0)
    assert err == skycoin.SKY_OK
    err, Key = skycoin.SKY_bip32_PublicKey_GetKey(change0)
    assert err == skycoin.SKY_OK
    err, KeyStr = skycoin.SKY_base58_Hex2String(Key)
    assert err == skycoin.SKY_OK
    assert KeyStr == b'026d3eb891e81ecabedfa8560166af383457aedaf172af9d57d00508faa5f57c4c'

    err, change1 = skycoin.SKY_bip32_PrivateKey_NewPublicChildKey(change, 1)
    assert err == skycoin.SKY_OK
    err, Key1 = skycoin.SKY_bip32_PublicKey_GetKey(change1)
    assert err == skycoin.SKY_OK
    err, Key1Str = skycoin.SKY_base58_Hex2String(Key1)
    assert err == skycoin.SKY_OK
    assert Key1Str == b'02681b301293fdf0292cd679b37d60b92a71b389fd994b2b57c8daf99532bfb4a5'
