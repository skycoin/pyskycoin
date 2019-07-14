# import skycoin
# from . import test_testsuite
# import json
# import os
# import re

# # testdataDir           = "./testdata/"
# testdataDir           = "gopath/src/github.com/skycoin/libskycoin/vendor/github.com/skycoin/skycoin/src/cipher/testsuite/testdata/"
# manyAddressesFilename = "many-addresses.golden"
# inputHashesFilename   = "input-hashes.golden"
# seedFileRegex         = "seed-\d+.golden"


# def test_TestManyAddresses():
#     f = open(testdataDir+manyAddressesFilename,'r')
#     fn = f.read()
#     f_JSON = json.loads(fn)
#     dataJSON = test_testsuite.SeedTestData()
#     dataJSON.Seed = f_JSON["seed"]
#     dataJSON.Keys = f_JSON["keys"]
#     err, data = test_testsuite.SeedTestDataFromJSON(dataJSON)
#     assert err == skycoin.SKY_OK
#     err = test_testsuite.ValidateSeedData(data, None)
#     assert err == skycoin.SKY_OK

# def test_TestSeedSignatures():
#     f = open(testdataDir+inputHashesFilename,'r')
#     fn = f.read()
#     f_JSON = json.loads(fn)
#     inputDataJSON = test_testsuite.InputTestData()
#     inputDataJSON.Hashes = f_JSON["hashes"]
#     err, inputData = test_testsuite.InputTestDataFromJSON(inputDataJSON)
#     assert err == skycoin.SKY_OK
#     err, seedFiles = traverseFiles()
#     assert err == skycoin.SKY_OK
#     for dir_f in seedFiles:
#         f = open(testdataDir+dir_f,'r')
#         fn = f.read()
#         f_JSON = json.loads(fn)
#         dataJSON = test_testsuite.SeedTestData()
#         dataJSON.Seed = f_JSON["seed"]
#         dataJSON.Keys = f_JSON["keys"]
#         err, data = test_testsuite.SeedTestDataFromJSON(dataJSON)
#         assert err == skycoin.SKY_OK
#         err = test_testsuite.ValidateSeedData(data, inputData)
#         assert err == skycoin.SKY_OK


# def traverseFiles():
#     files = []
#     root = os.listdir(testdataDir)
#     pattern = re.compile(seedFileRegex)
#     for path in root:
#         if pattern.match(path):
#             files.append(path)
#     if len(files) == 0:
#         return skycoin.SKY_ERROR, None
#     return skycoin.SKY_OK, files
