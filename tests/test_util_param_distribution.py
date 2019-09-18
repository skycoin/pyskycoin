import skycoin
import tests.utils as utils


def test_TestDistributionAddressArrays():
    err, dist = skycoin.SKY_params_Distribution_GetMainNetDistribution()
    assert err == skycoin.SKY_OK
    err, addr = skycoin.SKY_params_Distribution_GetAddresses(dist)
    assert err == skycoin.SKY_OK
    err, length_addr = skycoin.SKY_Handle_Strings_GetCount(addr)
    assert err == skycoin.SKY_OK

    assert length_addr == 100
    #  At the time of this writing, there should be 25 addresses in the
    #  unlocked pool and 75 in the locked pool.
    err, unlocked = skycoin.SKY_params_Distribution_UnlockedAddresses(dist)
    assert err == skycoin.SKY_OK
    err, countUnlocked = skycoin.SKY_Handle_Strings_GetCount(unlocked)
    assert err == skycoin.SKY_OK
    assert countUnlocked == 25
    err, locked = skycoin.SKY_params_Distribution_LockedAddresses(dist)
    assert err == skycoin.SKY_OK
    err, countLocked = skycoin.SKY_Handle_Strings_GetCount(locked)
    assert err == skycoin.SKY_OK
    assert countLocked == 75
    # err, string = skycoin.SKY_Handle_Strings_GetAt(unlocked, 1)
    # assert err == skycoin.SKY_OK
    # for i in range(len(addrs)):
    #     iStr = addrs[i]
    #     for j in range(i + 1):
    #         if j < len(addrs):
    #             break
    #         jStr = addrs[i + 1]
    #         assert iStr != jStr

    # for i in range(len(unlocked)):
    #     iStr = unlocked[i]
    #     for j in range(i + 1):
    #         if j < len(unlocked):
    #             break
    #         jStr = unlocked[i + 1]
    #         assert iStr != jStr

    # for i in range(len(locked)):
    #     iStr = locked[i]
    #     for j in range(i + 1):
    #         if j < len(locked):
    #             break
    #         jStr = locked[i + 1]
    #         assert iStr != jStr
