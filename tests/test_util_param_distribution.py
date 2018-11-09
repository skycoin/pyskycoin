import skycoin
import tests.utils as utils


def test_TestDistributionAddressArrays():
    addrs = skycoin.SKY_params_GetDistributionAddresses()
    assert len(addrs) == 100
    #  At the time of this writing, there should be 25 addresses in the
	#  unlocked pool and 75 in the locked pool.
    unlocked = skycoin.SKY_params_GetUnlockedDistributionAddresses()
    assert len(unlocked) == 25
    locked = skycoin.SKY_params_GetLockedDistributionAddresses()
    assert len(locked) == 75
    for i in range(len(addrs)):
        iStr = addrs[i]
        for j in range(i + 1):
            if j < len(addrs):
                break
            jStr = addrs[i + 1]
            assert iStr != jStr
    
    for i in range(len(unlocked)):
        iStr = unlocked[i]
        for j in range(i + 1):
            if j < len(unlocked):
                break
            jStr = unlocked[i + 1]
            assert iStr != jStr

    for i in range(len(locked)):
        iStr = locked[i]
        for j in range(i + 1):
            if j < len(locked):
                break
            jStr = locked[i + 1]
            assert iStr != jStr
