import skycoin
import tests.utils as utils


def test_TestDistributionAddressArrays():
    assert len(skycoin.SKY_params_GetDistributionAddresses()) == 100
    #  At the time of this writing, there should be 25 addresses in the
	#  unlocked pool and 75 in the locked pool.
    assert len(skycoin.SKY_params_GetUnlockedDistributionAddresses()) == 25
    assert len(skycoin.SKY_params_GetLockedDistributionAddresses()) == 75
    all = skycoin.SKY_params_GetDistributionAddresses()
    for i in  range(len(all)):
        pass