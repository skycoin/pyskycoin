import skycoin
import tests.utils
from tests.utils.transutil import makeUxBodyWithSecret, makeUxOutWithSecret

def test_TestUxBodyHash():
    uxb, _ = makeUxBodyWithSecret()
    hash_null = skycoin.cipher_SHA256()
    hashx  = skycoin.cipher_SHA256()
    assert skycoin.SKY_coin_UxBody_Hash(uxb, hashx) == skycoin.SKY_OK
    assert hashx != hash_null

def test_TestUxOutHash():
    uxb, _ = makeUxBodyWithSecret()
    uxo, _ = makeUxOutWithSecret()
    uxo.Body = uxb
    hash_body = skycoin.cipher_SHA256()
    hash_out  = skycoin.cipher_SHA256()
    assert skycoin.SKY_coin_UxBody_Hash(uxb, hash_body) == skycoin.SKY_OK
    assert skycoin.SKY_coin_UxOut_Hash(uxo, hash_out) == skycoin.SKY_OK
    assert hash_body == hash_out
    # Head should not affect hash
    uxh = skycoin.coin__UxHead()
    uxh.Time = 0
    uxh.BkSeq = 1
    uxo.Head = uxh
    assert skycoin.SKY_coin_UxOut_Hash(uxo, hash_out) == skycoin.SKY_OK
    assert hash_body == hash_out

def test_TestUxOutSnapshotHash():
    p = skycoin.cipher_PubKey()
    s = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(p, s)
    uxb = skycoin.coin__UxBody()
    _, b = skycoin.SKY_cipher_RandByte(128)
    h = skycoin.cipher_SHA256()
    assert skycoin.SKY_cipher_SumSHA256(b, h) == skycoin.SKY_OK
    uxb.SetSrcTransaction(h.toStr())
    a = skycoin.cipher__Address()
    skycoin.SKY_cipher_AddressFromPubKey(p, a)
    uxb.Address = a
    uxb.Coins = int(1e6)
    uxb.Hours = int(100)
    uxo = skycoin.coin__UxOut()
    uxh = skycoin.coin__UxHead()
    uxh.Time = 100
    uxh.BkSeq = 2
    uxo.Head = uxh
    uxo.Body = uxb
    hn = skycoin.cipher_SHA256()
    assert skycoin.SKY_coin_UxOut_SnapshotHash(uxo, hn) == skycoin.SKY_OK
    # snapshot hash should be dependent on every field in body and head
    # Head Time
    uxo_2 = uxo
    uxh.Time = 20
    uxo_2.Head = uxh
    hn_2 = skycoin.cipher_SHA256()
    assert skycoin.SKY_coin_UxOut_SnapshotHash(uxo_2, hn_2) == skycoin.SKY_OK
    assert hn != hn_2
    # Head BkSeq
    uxo_2 = uxo
    uxh.BkSeq = 4
    uxo_2.Head = uxh
    hn_2 = skycoin.cipher_SHA256()
    assert skycoin.SKY_coin_UxOut_SnapshotHash(uxo_2, hn_2) == skycoin.SKY_OK
    assert hn != hn_2
    # Body SetSrcTransaction
    uxo_2 = uxo
    uxb = skycoin.coin__UxBody()
    _, b = skycoin.SKY_cipher_RandByte(128)
    h = skycoin.cipher_SHA256()
    assert skycoin.SKY_cipher_SumSHA256(b, h) == skycoin.SKY_OK
    uxb.SetSrcTransaction(h.toStr())
    uxo_2.Body = uxb
    hn_2 = skycoin.cipher_SHA256()
    assert skycoin.SKY_coin_UxOut_SnapshotHash(uxo_2, hn_2) == skycoin.SKY_OK
    assert hn != hn_2
    # Body Address
    p_2 = skycoin.cipher_PubKey()
    s_2 = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(p_2, s_2)
    a_2 = skycoin.cipher__Address()
    skycoin.SKY_cipher_AddressFromPubKey(p_2, a_2)
    uxo_2 = uxo
    uxb = skycoin.coin__UxBody()
    uxb.Address = a_2
    uxo_2.Body = uxb
    hn_2 = skycoin.cipher_SHA256()
    assert skycoin.SKY_coin_UxOut_SnapshotHash(uxo_2, hn_2) == skycoin.SKY_OK
    assert hn != hn_2
    # Body Coins
    uxo_2 = uxo
    uxb = skycoin.coin__UxBody()
    uxb.Coins = int(2)
    uxo_2.Body = uxb
    hn_2 = skycoin.cipher_SHA256()
    assert skycoin.SKY_coin_UxOut_SnapshotHash(uxo_2, hn_2) == skycoin.SKY_OK
    assert hn != hn_2
    # Body Hours
    uxo_2 = uxo
    uxb = skycoin.coin__UxBody()
    uxb.Hours = int(2)
    uxo_2.Body = uxb
    hn_2 = skycoin.cipher_SHA256()
    assert skycoin.SKY_coin_UxOut_SnapshotHash(uxo_2, hn_2) == skycoin.SKY_OK
    assert hn != hn_2

def test_TestUxOutCoinHours():
    p = skycoin.cipher_PubKey()
    s = skycoin.cipher_SecKey()
    skycoin.SKY_cipher_GenerateKeyPair(p, s)
    uxb = skycoin.coin__UxBody()
    _, b = skycoin.SKY_cipher_RandByte(128)
    h = skycoin.cipher_SHA256()
    assert skycoin.SKY_cipher_SumSHA256(b, h) == skycoin.SKY_OK
    uxb.SetSrcTransaction(h.toStr())
    a = skycoin.cipher__Address()
    skycoin.SKY_cipher_AddressFromPubKey(p, a)
    uxb.Address = a
    uxb.Coins = int(1e6)
    uxb.Hours = int(100)
    uxo = skycoin.coin__UxOut()
    uxh = skycoin.coin__UxHead()
    uxh.Time = 100
    uxh.BkSeq = 2
    uxo.Head = uxh
    uxo.Body = uxb
    
    # Less than an hour passed
    now = uxh.Time + 100 
    err, hours =  skycoin.SKY_coin_UxOut_CoinHours(uxo, now)
    assert hours == uxh.Time
    assert err == skycoin.SKY_OK
    # 1 hours passed
    now = uxh.Time + 3600 
    err, hours =  skycoin.SKY_coin_UxOut_CoinHours(uxo, now)
    assert hours == uxh.Time + uxb.Coins / 1000000
    assert err == skycoin.SKY_OK
    # 6 hours passed
    now = uxh.Time + 3600 * 6
    err, hours =  skycoin.SKY_coin_UxOut_CoinHours(uxo, now)
    assert hours == uxh.Time + (uxb.Coins / 1000000) * 6
    assert err == skycoin.SKY_OK
    # Time is backwards (treated as no hours passed)
    now = uxh.Time // 2
    err, hours =  skycoin.SKY_coin_UxOut_CoinHours(uxo, now)
    assert hours == uxh.Time
    assert err == skycoin.SKY_OK
    # 1 hour has passed, output has 1.5 coins, should gain 1 coinhour
    uxb.Coins = 1500000
    now = uxh.Time + 3600 
    err, hours =  skycoin.SKY_coin_UxOut_CoinHours(uxo, now)
    assert hours == uxb.Hours + 1
    assert err == skycoin.SKY_OK
    # 2 hours have passed, output has 1.5 coins, should gain 3 coin hours
    uxb.Coins = 1500000
    uxo.Body = uxb
    now = uxh.Time + 3600 * 2
    err, hours =  skycoin.SKY_coin_UxOut_CoinHours(uxo, now)
    assert hours == uxb.Hours + 3
    assert err == skycoin.SKY_OK
    # 1 second has passed, output has 3600 coins, should gain 1 coin hour
    uxb.Coins = 3600000000
    uxo.Body = uxb
    now = uxh.Time + 1
    err, hours =  skycoin.SKY_coin_UxOut_CoinHours(uxo, now)
    assert hours == uxb.Hours + 1
    assert err == skycoin.SKY_OK
    # 1000000 hours minus 1 second have passed, output has 1 droplet, should gain 0 coin hour
    uxb.Coins = 1
    uxo.Body = uxb
    now = uxh.Time + 1000000 * 3600 - 1
    err, hours =  skycoin.SKY_coin_UxOut_CoinHours(uxo, now)
    assert hours == uxb.Hours
    assert err == skycoin.SKY_OK
    # 1000000 hours have passed, output has 1 droplet, should gain 1 coin hour
    uxb.Coins = 1
    uxo.Body = uxb
    now = uxh.Time + 1000000 * 3600
    err, hours =  skycoin.SKY_coin_UxOut_CoinHours(uxo, now)
    assert hours == uxb.Hours + 1
    assert err == skycoin.SKY_OK
    # No hours passed, using initial coin hours
    uxb.Coins = 1000000000
    uxb.Hours = 1000 * 1000
    uxo.Body = uxb
    now = uxh.Time
    err, hours =  skycoin.SKY_coin_UxOut_CoinHours(uxo, now)
    assert hours == uxb.Hours
    assert err == skycoin.SKY_OK
    # One hour passed, using initial coin hours
    now = uxh.Time + 3600
    err, hours =  skycoin.SKY_coin_UxOut_CoinHours(uxo, now)
    assert hours == uxb.Hours + 1000000000 / 1000000
    assert err == skycoin.SKY_OK
    # No hours passed and no hours to begin with0
    uxb.Hours = 0
    uxo.Body = uxb
    now = uxh.Time
    err, hours =  skycoin.SKY_coin_UxOut_CoinHours(uxo, now)
    assert hours == 0
    assert err == skycoin.SKY_OK
    # Centuries have passed, time-based calculation overflows uint64
    # when calculating the whole coin seconds
    uxb.Coins = 2000000
    uxo.Body = uxb
    now = 0xFFFFFFFFFFFFFFFF
    err, hours =  skycoin.SKY_coin_UxOut_CoinHours(uxo, now)
    assert err == skycoin.SKY_ERROR
    # Centuries have passed, time-based calculation overflows uint64
    # when calculating the droplet seconds
    uxb.Coins = 1500000
    uxo.Body = uxb
    now = 0xFFFFFFFFFFFFFFFF
    err, hours =  skycoin.SKY_coin_UxOut_CoinHours(uxo, now)
    assert err == skycoin.SKY_ERROR
    # Output would overflow if given more hours, has reached its limit
    uxb.Coins = 3600000000
    uxo.Body = uxb
    now = 0xFFFFFFFFFFFFFFFF
    err, hours =  skycoin.SKY_coin_UxOut_CoinHours(uxo, now)
    assert err == skycoin.SKY_ERROR