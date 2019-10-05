import skycoin
import tests.utils as utils

def test_TestUxBodyHash():
    uxb, _ = utils.makeUxBodyWithSecret()
    hash_null = skycoin.cipher_SHA256()
    hashx  = skycoin.cipher_SHA256()
    assert skycoin.SKY_coin_UxBody_Hash(uxb, hashx) == skycoin.SKY_OK
    assert hashx != hash_null


def test_TestUxOutHash():
    uxb, _ = utils.makeUxBodyWithSecret()
    uxo, _ = utils.makeUxOutWithSecret()
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
    err, hours = skycoin.SKY_coin_UxOut_CoinHours(uxo, now)
    assert hours == uxh.Time
    assert err == skycoin.SKY_OK
    # 1 hours passed
    now = uxh.Time + 3600
    err, hours = skycoin.SKY_coin_UxOut_CoinHours(uxo, now)
    assert hours == uxh.Time + uxb.Coins / 1000000
    assert err == skycoin.SKY_OK
    # 6 hours passed
    now = uxh.Time + 3600 * 6
    err, hours = skycoin.SKY_coin_UxOut_CoinHours(uxo, now)
    assert hours == uxh.Time + (uxb.Coins / 1000000) * 6
    assert err == skycoin.SKY_OK
    # Time is backwards (treated as no hours passed)
    now = uxh.Time // 2
    err, hours = skycoin.SKY_coin_UxOut_CoinHours(uxo, now)
    assert hours == uxh.Time
    assert err == skycoin.SKY_OK
    # 1 hour has passed, output has 1.5 coins, should gain 1 coinhour
    uxb.Coins = 1500000
    now = uxh.Time + 3600
    err, hours = skycoin.SKY_coin_UxOut_CoinHours(uxo, now)
    assert hours == uxb.Hours + 1
    assert err == skycoin.SKY_OK
    # 2 hours have passed, output has 1.5 coins, should gain 3 coin hours
    uxb.Coins = 1500000
    uxo.Body = uxb
    now = uxh.Time + 3600 * 2
    err, hours = skycoin.SKY_coin_UxOut_CoinHours(uxo, now)
    assert hours == uxb.Hours + 3
    assert err == skycoin.SKY_OK
    # 1 second has passed, output has 3600 coins, should gain 1 coin hour
    uxb.Coins = 3600000000
    uxo.Body = uxb
    now = uxh.Time + 1
    err, hours = skycoin.SKY_coin_UxOut_CoinHours(uxo, now)
    assert hours == uxb.Hours + 1
    assert err == skycoin.SKY_OK
    # 1000000 hours minus 1 second have passed, output has 1 droplet, should gain 0 coin hour
    uxb.Coins = 1
    uxo.Body = uxb
    now = uxh.Time + 1000000 * 3600 - 1
    err, hours = skycoin.SKY_coin_UxOut_CoinHours(uxo, now)
    assert hours == uxb.Hours
    assert err == skycoin.SKY_OK
    # 1000000 hours have passed, output has 1 droplet, should gain 1 coin hour
    uxb.Coins = 1
    uxo.Body = uxb
    now = uxh.Time + 1000000 * 3600
    err, hours = skycoin.SKY_coin_UxOut_CoinHours(uxo, now)
    assert hours == uxb.Hours + 1
    assert err == skycoin.SKY_OK
    # No hours passed, using initial coin hours
    uxb.Coins = 1000000000
    uxb.Hours = 1000 * 1000
    uxo.Body = uxb
    now = uxh.Time
    err, hours = skycoin.SKY_coin_UxOut_CoinHours(uxo, now)
    assert hours == uxb.Hours
    assert err == skycoin.SKY_OK
    # One hour passed, using initial coin hours
    now = uxh.Time + 3600
    err, hours = skycoin.SKY_coin_UxOut_CoinHours(uxo, now)
    assert hours == uxb.Hours + 1000000000 / 1000000
    assert err == skycoin.SKY_OK
    # No hours passed and no hours to begin with0
    uxb.Hours = 0
    uxo.Body = uxb
    now = uxh.Time
    err, hours = skycoin.SKY_coin_UxOut_CoinHours(uxo, now)
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


def test_TestUxArrayCoins():
    uxa = utils.makeUxArray(4)
    for x in uxa:
        x.Body.Coins = utils.Million
    err, coins = skycoin.SKY_coin_UxArray_Coins(uxa)
    assert coins == int(4e6)
    assert err == skycoin.SKY_OK
    uxa[2].Body.Coins = int(utils.MaxUint64 - int(1e6))
    err, _ = skycoin.SKY_coin_UxArray_Coins(uxa)
    assert err == skycoin.SKY_ERROR


def ux_Array_CoinsHours(uxa, now=0, slic=0):
    result = 0
    for x in uxa[slic:]:
        err, time = skycoin.SKY_coin_UxOut_CoinHours(x, now)
        result += time
        assert err == skycoin.SKY_OK
    return result


def test_TestUxArrayCoinHours():
    uxa = utils.makeUxArray(4)
    assert skycoin.SKY_coin_UxArray_CoinHours(uxa, 0)[1] == 400
    # 1 hour later
    assert skycoin.SKY_coin_UxArray_CoinHours(
        uxa, uxa[0].Head.Time + 3600)[1] == 404
    # 1.5 hours later
    assert skycoin.SKY_coin_UxArray_CoinHours(
        uxa, uxa[0].Head.Time + 3600 + 1800)[1] == 404
    # 2 hour later
    assert skycoin.SKY_coin_UxArray_CoinHours(
        uxa, uxa[0].Head.Time + 3600 + 4600)[1] == 408

    uxa[2].Head.Time = utils.MaxUint64 - 100
    # assert skycoin.SKY_coin_UxArray_CoinHours(uxa, utils.MaxUint64 - 100)[1] == skycoin.SKY_OK
    value = skycoin.SKY_coin_UxArray_CoinHours(uxa, uxa[2].Head.Time)[1]
    assert utils.err_CoinHours_Overflow(
        value) == skycoin.SKY_ErrAddEarnedCoinHoursAdditionOverflow
    value = skycoin.SKY_coin_UxArray_CoinHours(uxa, 1000000000000)[1]
    assert utils.err_CoinHours_Overflow(
        value) == skycoin.SKY_ErrAddEarnedCoinHoursAdditionOverflow


def test_TestUxArrayHashArray():
    uxa = utils.makeUxArray(4)
    sha = skycoin.cipher_SHA256()
    err, hashs = skycoin.SKY_coin_UxArray_Hashes(uxa)
    assert err == skycoin.SKY_OK
    assert len(hashs) == len(uxa)
    skycoin.SKY_coin_UxOut_Hash(uxa[0], sha)
    print(sha)
    print(uxa[0])
    assert hashs[0] == sha
    for i in range(len(hashs)):
        assert skycoin.SKY_coin_UxOut_Hash(uxa[i], sha) == 0
        assert sha == hashs[i]


def test_TestUxArrayHasDupes():
    uxa = utils.makeUxArray(4)
    err, hasDupes = skycoin.SKY_coin_UxArray_HasDupes(uxa)
    assert err == skycoin.SKY_OK
    assert hasDupes == 0
    uxa[0] = uxa[1]
    err, hasDupes = skycoin.SKY_coin_UxArray_HasDupes(uxa)
    assert err == skycoin.SKY_OK
    assert hasDupes == 1


def test_TestUxArraySub():
    uxa = utils.makeUxArray(4)
    uxb = utils.makeUxArray(4)
    uxc = uxa[:1]
    for ux in uxb:
        uxc.append(ux)
    for ux in uxa[1:2]:
        uxc.append(ux)
    err, uxd = skycoin.SKY_coin_UxArray_Sub(uxc, uxa)
    assert err == skycoin.SKY_OK
    assert len(uxd) == len(uxb)
    err, uxd = skycoin.SKY_coin_UxArray_Sub(uxc, uxb)
    assert err == skycoin.SKY_OK
    assert len(uxd) == 2
    assert uxd == uxa[:2]
    # No intersection
    err, uxd = skycoin.SKY_coin_UxArray_Sub(uxa, uxb)
    assert uxd == uxa
    err, uxd = skycoin.SKY_coin_UxArray_Sub(uxb, uxa)
    assert uxd == uxb


def manualUxArrayIsSorted(uxa):
    sha_1 = skycoin.cipher_SHA256()
    sha_2 = skycoin.cipher_SHA256()
    isSorte = True
    for i in range(len(uxa) - 1):
        assert skycoin.SKY_coin_UxOut_Hash(uxa[i], sha_1) == skycoin.SKY_OK
        assert skycoin.SKY_coin_UxOut_Hash(uxa[i + 1], sha_2) == skycoin.SKY_OK
        if sha_1 > sha_2:
            isSorte = False
    return isSorte


def isUxArraySorted(uxa):
    n = len(uxa)
    prev = uxa
    current = prev
    current += 1
    hash_1 = skycoin.cipher_SHA256()
    hash_2 = skycoin.cipher_SHA256()
    prevHash = None
    currentHash = None
    result = int()
    for i in n:
        if(prevHash == None):
            result = skycoin.SKY_coin_UxOut_Hash(prev, hash_1)
            assert result == skycoin.SKY_OK
            prevHash = hash_1
        if currentHash == None:
            currentHash = hash_2
            result = skycoin.SKY_coin_UxOut_Hash(current, currentHash)
            assert result == skycoin.SKY_OK
        if prevHash.__eq__(currentHash) > 0:
            return 0
        if i % 2 != 0:
            prevHash = hash_2
            currentHash = hash_1
        else:
            prevHash = hash_1
            currentHash = hash_2
        prev += 1
        current += 1
    return 1


def test_TestUxArrayLen():
    uxa = utils.makeUxArray(4)
    assert len(uxa) == 4


def test_TestUxArrayLess():
    uxa = utils.makeUxArray(2)
    err, hasha = skycoin.SKY_coin_UxArray_Hashes(uxa)
    assert err == skycoin.SKY_OK and len(hasha) == len(uxa)
    err, _ = skycoin.SKY_coin_UxArray_Less(uxa, 0, 1)
    assert err == skycoin.SKY_OK
    err, _ = skycoin.SKY_coin_UxArray_Less(uxa, 1, 0)
    assert err == skycoin.SKY_OK

def test_TestUxArraySwap():
    uxa = utils.makeUxArray(2)
    uxx = utils.make_UxOut()
    uxy = utils.make_UxOut()
    uxa[0] = uxx
    uxa[1] = uxy
    err = skycoin.SKY_coin_UxArray_Swap(uxa, 0, 1)
    assert err == skycoin.SKY_OK
    uxa[0] = uxy
    uxa[1] = uxx
    err = skycoin.SKY_coin_UxArray_Swap(uxa, 0, 1)
    assert err == skycoin.SKY_OK
    uxa[0] = uxx
    uxa[1] = uxy
    err = skycoin.SKY_coin_UxArray_Swap(uxa, 0, 1)
    assert err == skycoin.SKY_OK
    uxa[1] = uxx
    uxa[0] = uxy

def test_TestAddressUxOutsKeys():
    uxa = utils.makeUxArray(3)
    err, uxH = skycoin.SKY_coin_NewAddressUxOuts(uxa)
    assert err == skycoin.SKY_OK
    # keys = []
    err ,keys = skycoin.SKY_coin_AddressUxOuts_Keys(uxH)
    assert err == skycoin.SKY_OK
    assert len(keys) == 3
    for k in keys:
        assert k == uxa[0].Body.Address or k == uxa[1].Body.Address or k == uxa[2].Body.Address

def test_TestAddressUxOutsSub():
    uxa = utils.makeUxArray(4)
    empty = utils.makeUxArray(0)
    err, uxH_1 = skycoin.SKY_coin_NewAddressUxOuts(empty)
    assert err == skycoin.SKY_OK
    err, uxH_2 = skycoin.SKY_coin_NewAddressUxOuts(empty)
    assert err == skycoin.SKY_OK
    uxa[1].Body.Address = uxa[0].Body.Address
    ux_2 = uxa[:2]
    err = skycoin.SKY_coin_AddressUxOuts_Set(uxH_1,uxa[0].Body.Address,ux_2)
    assert err == skycoin.SKY_OK
    ux_3 = [uxa[2]]
    err = skycoin.SKY_coin_AddressUxOuts_Set(uxH_1,uxa[2].Body.Address, ux_3)
    assert err == skycoin.SKY_OK
    ux_4 = [uxa[3]]
    err = skycoin.SKY_coin_AddressUxOuts_Set(uxH_1,uxa[3].Body.Address,ux_4)
    assert err == skycoin.SKY_OK

    ux_5 = [uxa[0]]
    err = skycoin.SKY_coin_AddressUxOuts_Set(uxH_2,uxa[0].Body.Address,ux_5)
    assert err == skycoin.SKY_OK
    ux_6 = [uxa[2]]
    err = skycoin.SKY_coin_AddressUxOuts_Set(uxH_2,uxa[2].Body.Address,ux_6)
    assert err == skycoin.SKY_OK
    err, uxH_3 = skycoin.SKY_coin_AddressUxOuts_Sub(uxH_1,uxH_2)
    assert err == skycoin.SKY_OK
    # length
    err, length = skycoin.SKY_coin_AddressUxOuts_Length(uxH_3)
    assert length == 2
    assert err == skycoin.SKY_OK
    # hasKey
    err,  has_key = skycoin.SKY_coin_AddressUxOuts_HasKey(uxH_3, uxa[2].Body.Address)
    assert err == skycoin.SKY_OK
    assert has_key == 0
    err, ux_3 = skycoin.SKY_coin_AddressUxOuts_Get(uxH_3,uxa[3].Body.Address)
    assert err == skycoin.SKY_OK
    assert len(ux_3) == 1
    uxtmp = ux_3[0]
    assert uxtmp == ux_3[0]
    assert ux_3[0] == uxa[3]
    err, ux_2 = skycoin.SKY_coin_AddressUxOuts_Get(uxH_3,uxa[0].Body.Address)
    assert err == skycoin.SKY_OK
    assert len(ux_2) == 1
    assert ux_2[0] == uxa[1]
    # Originals should be unmodified
    err, length = skycoin.SKY_coin_AddressUxOuts_Length(uxH_1)
    assert err == skycoin.SKY_OK
    assert length == 3
    err, length = skycoin.SKY_coin_AddressUxOuts_GetOutputLength(uxH_1,uxa[0].Body.Address)
    assert err == skycoin.SKY_OK
    assert length == 2
    err, length = skycoin.SKY_coin_AddressUxOuts_GetOutputLength(uxH_1,uxa[2].Body.Address)
    assert err == skycoin.SKY_OK
    assert length == 1
    err, length = skycoin.SKY_coin_AddressUxOuts_GetOutputLength(uxH_1,uxa[3].Body.Address)
    assert err == skycoin.SKY_OK
    assert length == 1

    err, length = skycoin.SKY_coin_AddressUxOuts_Length(uxH_2)
    assert err == skycoin.SKY_OK
    assert length == 2
    err, length = skycoin.SKY_coin_AddressUxOuts_GetOutputLength(uxH_2,uxa[0].Body.Address)
    assert err == skycoin.SKY_OK
    assert length == 1
    err, length = skycoin.SKY_coin_AddressUxOuts_GetOutputLength(uxH_2,uxa[2].Body.Address)
    assert err == skycoin.SKY_OK
    assert length == 1


def test_TestAddressUxOutsAdd():
    uxa = utils.makeUxArray(4)
    empty = utils.makeUxArray(0)
    err, uxH_1 = skycoin.SKY_coin_NewAddressUxOuts(empty)
    assert err == skycoin.SKY_OK
    err, uxH_2 = skycoin.SKY_coin_NewAddressUxOuts(empty)
    assert err == skycoin.SKY_OK
    uxa[1].Body.Address = uxa[0].Body.Address
    ux_2 = [uxa[0]]
    err = skycoin.SKY_coin_AddressUxOuts_Set(uxH_1,uxa[0].Body.Address,ux_2)
    assert err == skycoin.SKY_OK
    ux_3 = [uxa[2]]
    err = skycoin.SKY_coin_AddressUxOuts_Set(uxH_1,uxa[2].Body.Address, ux_3)
    assert err == skycoin.SKY_OK
    ux_4 = [uxa[3]]
    err = skycoin.SKY_coin_AddressUxOuts_Set(uxH_1,uxa[3].Body.Address,ux_4)
    assert err == skycoin.SKY_OK
    ux_5 = [uxa[0]]
    err = skycoin.SKY_coin_AddressUxOuts_Set(uxH_2,uxa[0].Body.Address,ux_5)
    assert err == skycoin.SKY_OK
    ux_6 = [uxa[2]]
    err = skycoin.SKY_coin_AddressUxOuts_Set(uxH_2,uxa[2].Body.Address,ux_6)
    assert err == skycoin.SKY_OK
    err, uxH_3 = skycoin.SKY_coin_AddressUxOuts_Add(uxH_1,uxH_2)
    assert err == skycoin.SKY_OK
    # length
    err, length = skycoin.SKY_coin_AddressUxOuts_Length(uxH_3)
    assert err == skycoin.SKY_OK
    assert length == 3
    err, length = skycoin.SKY_coin_AddressUxOuts_GetOutputLength(uxH_3,uxa[0].Body.Address)
    assert err == skycoin.SKY_OK
    # assert length == 2
    err, ux_2 = skycoin.SKY_coin_AddressUxOuts_Get(uxH_3,uxa[0].Body.Address)
    assert err == skycoin.SKY_OK
    # assert len(ux_2) == 2
    assert ux_2[0] == uxa[0]
    # assert ux_2[1] == uxa[1]
    err, ux_2 = skycoin.SKY_coin_AddressUxOuts_Get(uxH_3,uxa[2].Body.Address)
    assert err == skycoin.SKY_OK
    assert len(ux_2) == 1
    assert ux_2[0] == uxa[2]
    err, ux_2 = skycoin.SKY_coin_AddressUxOuts_Get(uxH_3,uxa[3].Body.Address)
    assert err == skycoin.SKY_OK
    assert len(ux_2) == 1
    assert ux_2[0] == uxa[3]
    err, ux_2 = skycoin.SKY_coin_AddressUxOuts_Get(uxH_3,uxa[1].Body.Address)
    assert err == skycoin.SKY_OK
    # assert len(ux_2) == 2
    assert ux_2[0] == uxa[0]
    # assert ux_2[1] == uxa[1]
    # Originals should be unmodified
    err, length = skycoin.SKY_coin_AddressUxOuts_Length(uxH_1)
    assert err == skycoin.SKY_OK
    assert length == 3
    err, length = skycoin.SKY_coin_AddressUxOuts_GetOutputLength(uxH_1,uxa[0].Body.Address)
    assert err == skycoin.SKY_OK
    assert length == 1
    err, length = skycoin.SKY_coin_AddressUxOuts_GetOutputLength(uxH_1,uxa[2].Body.Address)
    assert err == skycoin.SKY_OK
    assert length == 1
    err, length = skycoin.SKY_coin_AddressUxOuts_GetOutputLength(uxH_1,uxa[3].Body.Address)
    assert err == skycoin.SKY_OK
    assert length == 1
    err, length = skycoin.SKY_coin_AddressUxOuts_Length(uxH_2)
    assert err == skycoin.SKY_OK
    assert length == 2
    err, length = skycoin.SKY_coin_AddressUxOuts_GetOutputLength(uxH_2,uxa[0].Body.Address)
    assert err == skycoin.SKY_OK
    assert length == 1
    err, length = skycoin.SKY_coin_AddressUxOuts_GetOutputLength(uxH_2,uxa[2].Body.Address)
    assert err == skycoin.SKY_OK
    assert length == 1

def test_TestAddressUxOutsFlatten():
    uxa = utils.makeUxArray(3)
    empty = utils.makeUxArray(0)
    err, uxH = skycoin.SKY_coin_NewAddressUxOuts(empty)
    assert err == skycoin.SKY_OK
    uxa[2].Body.Address = uxa[1].Body.Address
    emptyAddr = skycoin.cipher__Address()
    err = skycoin.SKY_coin_AddressUxOuts_Set(uxH,emptyAddr,empty)
    assert err == skycoin.SKY_OK
    ux_1 = [uxa[0]]
    err = skycoin.SKY_coin_AddressUxOuts_Set(uxH,uxa[0].Body.Address,ux_1)
    assert err == skycoin.SKY_OK
    ux_2 = uxa[1:]
    err = skycoin.SKY_coin_AddressUxOuts_Set(uxH,uxa[1].Body.Address,ux_2)
    assert err == skycoin.SKY_OK
    err, flatArray = skycoin.SKY_coin_AddressUxOuts_Flatten(uxH)
    assert err == skycoin.SKY_OK
    assert len(flatArray) == 3
    for x in flatArray:
        assert x.Body.Address != emptyAddr

    if flatArray[0].Body.Address == uxa[0].Body.Address:
        assert flatArray[0] == uxa[0]
        assert flatArray[0].Body.Address == uxa[0].Body.Address
        assert flatArray[1] == uxa[1]
        assert flatArray[1].Body.Address == uxa[1].Body.Address
        assert flatArray[2] == uxa[2]
        assert flatArray[2].Body.Address == uxa[2].Body.Address
    else:
        assert flatArray[0] == uxa[1]
        assert flatArray[0].Body.Address == uxa[1].Body.Address
        assert flatArray[1] == uxa[2]
        assert flatArray[1].Body.Address == uxa[2].Body.Address
        assert flatArray[2] == uxa[0]
        assert flatArray[2].Body.Address == uxa[0].Body.Address

def test_TestNewAddressUxOuts():
    uxa = utils.makeUxArray(6)
    uxa[1].Body.Address = uxa[0].Body.Address
    uxa[3].Body.Address = uxa[2].Body.Address
    uxa[4].Body.Address = uxa[2].Body.Address
    err, uxH = skycoin.SKY_coin_NewAddressUxOuts(uxa)
    assert err == skycoin.SKY_OK
    # length
    err, length = skycoin.SKY_coin_AddressUxOuts_Length(uxH)
    assert err == skycoin.SKY_OK
    assert length == 3
    err, ux_2 = skycoin.SKY_coin_AddressUxOuts_Get(uxH,uxa[0].Body.Address)
    assert err == skycoin.SKY_OK
    assert len(ux_2) == 2
    assert ux_2[0] == uxa[0]
    assert ux_2[1] == uxa[1]
    err, ux_2 = skycoin.SKY_coin_AddressUxOuts_Get(uxH,uxa[3].Body.Address)
    assert err == skycoin.SKY_OK
    assert len(ux_2) == 3
    assert ux_2[0] == uxa[2]
    assert ux_2[1] == uxa[3]
    assert ux_2[2] == uxa[4]
    err, ux_2 = skycoin.SKY_coin_AddressUxOuts_Get(uxH,uxa[5].Body.Address)
    assert err == skycoin.SKY_OK
    assert len(ux_2) == 1
    assert ux_2[0] == uxa[5]
