import  skycoin
import operator
import random

TESTS = 1


def test_Test_Secp256_00():
    err , nonce = skycoin.SKY_cipher_RandByte(32)
    assert err == skycoin.SKY_OK
    assert len(nonce) == 32


def test_Test_Secp256_01():
    pubkey = skycoin.cipher_PubKey()
    seckey = skycoin.cipher_SecKey()
    assert skycoin.SKY_cipher_GenerateKeyPair(pubkey, seckey) == skycoin.SKY_OK
    assert skycoin.SKY_cipher_PubKey_Verify(pubkey) == skycoin.SKY_OK
    assert skycoin.SKY_cipher_SecKey_Verify(seckey) == skycoin.SKY_OK


def test_Test_PubkeyFromSeckey():
    _, privkey = skycoin.SKY_base58_String2Hex(b"f19c523315891e6e15ae0608a35eec2e00ebd6d1984cf167f46336dabd9b2de4")
    _, desiredPubKey = skycoin.SKY_base58_String2Hex(b"04fe43d0c2c3daab30f9472beb5b767be020b81c7cc940ed7a7e910f0c1d9feef10fe85eb3ce193405c2dd8453b7aeb6c1752361efdbf4f52ea8bf8f304aab37ab")

    err, pubkey = skycoin.SKY_secp256k1_UncompressedPubkeyFromSeckey(privkey)
    assert err == skycoin.SKY_OK
    assert pubkey != None
    assert pubkey == desiredPubKey


def RandX():
    err, pubkey, seckey = skycoin.SKY_secp256k1_GenerateKeyPair()
    assert err == skycoin.SKY_OK
    err, msg = skycoin.SKY_cipher_RandByte(32)
    assert err == skycoin.SKY_OK
    err, sig = skycoin.SKY_secp256k1_Sign(msg, seckey)
    assert err == skycoin.SKY_OK
    return pubkey, seckey, msg, sig


def test_Test_SignatureVerifyPubkey():
    err, pubkey1, seckey = skycoin.SKY_secp256k1_GenerateKeyPair()
    assert err == skycoin.SKY_OK
    err, msg = skycoin.SKY_cipher_RandByte(32)
    assert err == skycoin.SKY_OK
    err, sig = skycoin.SKY_secp256k1_Sign(msg, seckey)
    assert err == skycoin.SKY_OK
    err, value = skycoin.SKY_secp256k1_VerifyPubkey(pubkey1)
    assert err == skycoin.SKY_OK
    assert value != 0
    err , pubkey2 = skycoin.SKY_secp256k1_RecoverPubkey(msg, sig)
    assert pubkey1 == pubkey2


def test_Test_verify_functions():
    pubkey, seckey, hashs, sig = RandX()
    err, value = skycoin.SKY_secp256k1_VerifySeckey(seckey)
    assert err == skycoin.SKY_OK
    assert value != 0
    err, value = skycoin.SKY_secp256k1_VerifyPubkey(pubkey)
    assert err == skycoin.SKY_OK
    assert value != 0
    err, value = skycoin.SKY_secp256k1_VerifySignature(hashs, sig, pubkey)
    assert err == skycoin.SKY_OK
    assert value != 0
    _ = sig


def test_Test_SignatureVerifySecKey():
    err , pubkey, seckey = skycoin.SKY_secp256k1_GenerateKeyPair()
    assert err == skycoin.SKY_OK
    err, value = skycoin.SKY_secp256k1_VerifySeckey(seckey)
    assert err == skycoin.SKY_OK
    assert value != 0
    err, value = skycoin.SKY_secp256k1_VerifyPubkey(pubkey)
    assert err == skycoin.SKY_OK
    assert value != 0


def test_Test_Secp256_02s():
    err , pubkey, seckey = skycoin.SKY_secp256k1_GenerateKeyPair()
    assert err == skycoin.SKY_OK
    err, msg = skycoin.SKY_secp256k1_RandByte(32)
    assert err == skycoin.SKY_OK
    err, sig = skycoin.SKY_secp256k1_Sign(msg, seckey)
    assert err == skycoin.SKY_OK
    assert sig != None
    assert len(pubkey) == 33
    assert len(seckey) == 32
    assert len(sig) == (64 + 1)
    assert bytes(sig[64]) < bytes(4)


def test_Test_Secp256_02():
    err, pubkey, seckey = skycoin.SKY_secp256k1_GenerateKeyPair()
    assert err == skycoin.SKY_OK
    err, msg = skycoin.SKY_secp256k1_RandByte(32)
    assert err == skycoin.SKY_OK
    err, sig = skycoin.SKY_secp256k1_Sign(msg, seckey)
    assert err == skycoin.SKY_OK
    assert sig != None
    err, pubkey2 = skycoin.SKY_secp256k1_RecoverPubkey(msg, sig)
    assert err == skycoin.SKY_OK
    assert pubkey2 != None
    assert pubkey == pubkey2
    err, value = skycoin.SKY_secp256k1_VerifySignature(msg, sig, pubkey)
    assert err == skycoin.SKY_OK
    assert value == 1


def test_Test_Secp256_02a():
    err, pubkey1, seckey1 = skycoin.SKY_secp256k1_GenerateKeyPair()
    assert err == skycoin.SKY_OK
    err , msg = skycoin.SKY_secp256k1_RandByte(32)
    assert err == skycoin.SKY_OK
    err, sig = skycoin.SKY_secp256k1_Sign(msg, seckey1)
    assert err == skycoin.SKY_OK
    assert sig != None
    err, value = skycoin.SKY_secp256k1_VerifySignature(msg, sig, pubkey1)
    assert err == skycoin.SKY_OK
    assert value == 1
    err, pubkey2 = skycoin.SKY_secp256k1_RecoverPubkey(msg, sig)
    assert err == skycoin.SKY_OK
    assert len(pubkey1) == len(pubkey2)
    for i in range(len(pubkey1)):
        assert pubkey1[i] == pubkey2[i]
    assert pubkey1 == pubkey2


def test_Test_Secp256_03():
    err , _, seckey = skycoin.SKY_secp256k1_GenerateKeyPair()
    for i in range(TESTS):
        _, msg = skycoin.SKY_secp256k1_RandByte(32)
        _, sig = skycoin.SKY_secp256k1_Sign(msg, seckey)
        err , pubkey2 = skycoin.SKY_secp256k1_RecoverPubkey(msg, sig)
        assert err == skycoin.SKY_OK
        assert pubkey2 != None


def test_Test_Secp256_04():
    for i in range(TESTS):
        err, pubkey, seckey = skycoin.SKY_secp256k1_GenerateKeyPair()
        assert err == skycoin.SKY_OK
        _, msg = skycoin.SKY_secp256k1_RandByte(32)
        _, sig = skycoin.SKY_secp256k1_Sign(msg, seckey)
        last = sig[len(sig) - 1]
        assert operator.ge(bytes(last), bytes(4)) == False
        err , pubkey2 = skycoin.SKY_secp256k1_RecoverPubkey(msg, sig)
        assert err == skycoin.SKY_OK
        assert pubkey2 != None
        assert pubkey == pubkey2

# def randSig():
#     err, sig = skycoin.SKY_secp256k1_RandByte(65)
#     assert err == skycoin.SKY_OK
#     assert len(sig) == 65
#     operator.and_(sig[32], str(0x70))
#     sig[64] %= 4
#     return sig
    
# def test_Test_Secp256_06a_alt0():
#     err, pubkey, seckey = skycoin.SKY_secp256k1_GenerateKeyPair()
#     assert err == skycoin.SKY_OK
#     _, msg = skycoin.SKY_secp256k1_RandByte(32)
#     err, sig = skycoin.SKY_secp256k1_Sign(msg, seckey)
#     assert err == skycoin.SKY_OK
#     assert sig != None
#     assert len(sig) == 65
#     for i in range(TESTS):
#         sig = randSig()
#         err, pubkey2 = skycoin.SKY_secp256k1_RecoverPubkey(msg, sig)
#         assert pubkey != pubkey2
#         err, value = skycoin.SKY_secp256k1_VerifySignature(msg, sig, pubkey2)
#         assert err == skycoin.SKY_OK
#         assert pubkey2 == None , value == 1
#         err. value = skycoin.SKY_secp256k1_VerifySignature(msg, sig, pubkey)
#         assert err == skycoin.SKY_OK
#         assert value != 1


def test_Test_Secp256_06b():
    err, pubkey1, seckey = skycoin.SKY_secp256k1_GenerateKeyPair()
    assert err == skycoin.SKY_OK
    _, msg = skycoin.SKY_secp256k1_RandByte(32)
    _, sig = skycoin.SKY_secp256k1_Sign(msg, seckey)
    failCount = 0
    for i in range(TESTS):
        _, msg = skycoin.SKY_secp256k1_RandByte(32)
        err, pubkey2 = skycoin.SKY_secp256k1_RecoverPubkey(msg, sig)
        assert err == skycoin.SKY_OK
        assert pubkey1 != pubkey2
        err, value = skycoin.SKY_secp256k1_VerifySignature(msg, sig, pubkey2)
        assert err == skycoin.SKY_OK
        assert value == 1
        err, value = skycoin.SKY_secp256k1_VerifySignature(msg, sig, pubkey1)
        assert err == skycoin.SKY_OK
        assert value != 1


def test_Test_Deterministic_Keypairs_00():
    for i in range(64):
        _, seed = skycoin.SKY_secp256k1_RandByte(64)
        err, _, pub1, sec1 = skycoin.SKY_secp256k1_DeterministicKeyPairIterator(seed)
        assert err == skycoin.SKY_OK
        err, pub2, sec2 = skycoin.SKY_secp256k1_GenerateDeterministicKeyPair(seed)
        assert err == skycoin.SKY_OK
        assert pub1 == pub2
        assert sec1 == sec2


def test_Test_Deterministic_Keypairs_01():
    for i in range(64):
        _, seed = skycoin.SKY_secp256k1_RandByte(32)
        err, _, pub1, sec1 = skycoin.SKY_secp256k1_DeterministicKeyPairIterator(seed)
        assert err == skycoin.SKY_OK
        err, pub2, sec2 = skycoin.SKY_secp256k1_GenerateDeterministicKeyPair(seed)
        assert err == skycoin.SKY_OK
        assert pub1 == pub2
        assert sec1 == sec2


def test_Test_Deterministic_Keypairs_02():
    for i in range(64):
        _, seed = skycoin.SKY_secp256k1_RandByte(32)
        err, _, pub1, sec1 = skycoin.SKY_secp256k1_DeterministicKeyPairIterator(seed)
        assert err == skycoin.SKY_OK
        err, pub2, sec2 = skycoin.SKY_secp256k1_GenerateDeterministicKeyPair(seed)
        assert err == skycoin.SKY_OK
        assert pub1 == pub2
        assert sec1 == sec2


def Decode(str1):
    err, byt = skycoin.SKY_base58_String2Hex(str1)
    assert err == skycoin.SKY_OK
    return byt


def test_Test_Deterministic_Keypairs_03():
    testArray = [
        b"tQ93w5Aqcunm9SGUfnmF4fJv", b"9b8c3e36adce64dedc80d6dfe51ff1742cc1d755bbad457ac01177c5a18a789f",
		b"DC7qdQQtbWSSaekXnFmvQgse", b"d2deaf4a9ff7a5111fe1d429d6976cbde78811fdd075371a2a4449bb0f4d8bf9",
		b"X8EkuUZC7Td7PAXeS7Duc7vR", b"cad79b6dcf7bd21891cbe20a51c57d59689ae6e3dc482cd6ec22898ac00cd86b",
		b"tVqPYHHNVPRWyEed62v7f23u", b"2a386e94e9ffaa409517cbed81b9b2d4e1c5fb4afe3cbd67ce8aba11af0b02fa",
		b"kCy4R57HDfLqF3pVhBWxuMcg", b"26a7c6d8809c476a56f7455209f58b5ff3f16435fcf208ff2931ece60067f305",
		b"j8bjv86ZNjKqzafR6mtSUVCE", b"ea5c0f8c9f091a70bf38327adb9b2428a9293e7a7a75119920d759ecfa03a995",
		b"qShryAzVY8EtsuD3dsAc7qnG", b"331206176509bcae31c881dc51e90a4e82ec33cd7208a5fb4171ed56602017fa",
		b"5FGG7ZBa8wVMBJkmzpXj5ESX", b"4ea2ad82e7730d30c0c21d01a328485a0cf5543e095139ba613929be7739b52c",
		b"f46TZG4xJHXUGWx8ekbNqa9F", b"dcddd403d3534c4ef5703cc07a771c107ed49b7e0643c6a2985a96149db26108",
		b"XkZdQJ5LT96wshN8JBH8rvEt", b"3e276219081f072dff5400ca29a9346421eaaf3c419ff1474ac1c81ad8a9d6e1",
		b"GFDqXU4zYymhJJ9UGqRgS8ty", b"95be4163085b571e725edeffa83fff8e7a7db3c1ccab19d0f3c6e105859b5e10",
		b"tmwZksH2XyvuamnddYxyJ5Lp", b"2666dd54e469df56c02e82dffb4d3ea067daafe72c54dc2b4f08c4fb3a7b7e42",
		b"EuqZFsbAV5amTzkhgAMgjr7W", b"40c325c01f2e4087fcc97fcdbea6c35c88a12259ebf1bce0b14a4d77f075abbf",
		b"TW6j8rMffZfmhyDEt2JUCrLB", b"e676e0685c5d1afd43ad823b83db5c6100135c35485146276ee0b0004bd6689e",
		b"8rvkBnygfhWP8kjX9aXq68CY", b"21450a646eed0d4aa50a1736e6c9bf99fff006a470aab813a2eff3ee4d460ae4",
		b"phyRfPDuf9JMRFaWdGh7NXPX", b"ca7bc04196c504d0e815e125f7f1e086c8ae8c10d5e9df984aeab4b41bf9e398",
    ]

    for i in range(int(len(testArray) / 2)):
        seed = bytes(testArray[2 * i + 0])
        sec1 = Decode(testArray[2 * i + 1])
        err, _, sec2 = skycoin.SKY_secp256k1_GenerateDeterministicKeyPair(seed)
        assert err == skycoin.SKY_OK
        assert sec2 == sec1


def test_Test_DeterministicWallets1():
    testArray = [
        b"90c56f5b8d78a46fb4cddf6fd9c6d88d6d2d7b0ec35917c7dac12c03b04e444e", b"94dd1a9de9ffd57b5516b8a7f090da67f142f7d22356fa5d1b894ee4d4fba95b",
		b"a3b08ccf8cbae4955c02f223be1f97d2bb41d92b7f0c516eb8467a17da1e6057", b"82fba4cc2bc29eef122f116f45d01d82ff488d7ee713f8a95c162a64097239e0",
		b"7048eb8fa93cec992b93dc8e93c5543be34aad05239d4c036cf9e587bbcf7654", b"44c059496aac871ac168bb6889b9dd3decdb9e1fa082442a95fcbca982643425",
		b"6d25375591bbfce7f601fc5eb40e4f3dde2e453dc4bf31595d8ec29e4370cd80", b"d709ceb1a6fb906de506ea091c844ca37c65e52778b8d257d1dd3a942ab367fb",
		b"7214b4c09f584c5ddff971d469df130b9a3c03e0277e92be159279de39462120", b"5fe4986fa964773041e119d2b6549acb392b2277a72232af75cbfb62c357c1a7",
		b"b13e78392d5446ae304b5fc9d45b85f26996982b2c0c86138afdac8d2ea9016e", b"f784abc2e7f11ee84b4adb72ea4730a6aabe27b09604c8e2b792d8a1a31881ac",
		b"9403bff4240a5999e17e0ab4a645d6942c3a7147c7834e092e461a4580249e6e", b"d495174b8d3f875226b9b939121ec53f9383bd560d34aa5ca3ac6b257512adf4",
		b"2665312a3e3628f4df0b9bc6334f530608a9bcdd4d1eef174ecda99f51a6db94", b"1fdc9fbfc6991b9416b3a8385c9942e2db59009aeb2d8de349b73d9f1d389374",
		b"6cb37532c80765b7c07698502a49d69351036f57a45a5143e33c57c236d841ca", b"c87c85a6f482964db7f8c31720981925b1e357a9fdfcc585bc2164fdef1f54d0",
		b"8654a32fa120bfdb7ca02c487469070eba4b5a81b03763a2185fdf5afd756f3c", b"e2767d788d1c5620f3ef21d57f2d64559ab203c044f0a5f0730b21984e77019c",
		b"66d1945ceb6ef8014b1b6703cb624f058913e722f15d03225be27cb9d8aabe4a", b"3fcb80eb1d5b91c491408447ac4e221fcb2254c861adbb5a178337c2750b0846",
		b"22c7623bf0e850538329e3e6d9a6f9b1235350824a3feaad2580b7a853550deb", b"5577d4be25f1b44487140a626c8aeca2a77507a1fc4fd466dd3a82234abb6785",
		b"a5eebe3469d68c8922a1a8b5a0a2b55293b7ff424240c16feb9f51727f734516", b"c07275582d0681eb07c7b51f0bca0c48c056d571b7b83d84980ab40ac7d7d720",
		b"479ec3b589b14aa7290b48c2e64072e4e5b15ce395d2072a5a18b0a2cf35f3fd", b"f10e2b7675dfa557d9e3188469f12d3e953c2d46dce006cd177b6ae7f465cfc0",
		b"63952334b731ec91d88c54614925576f82e3610d009657368fc866e7b1efbe73", b"0bcbebb39d8fe1cb3eab952c6f701656c234e462b945e2f7d4be2c80b8f2d974",
		b"256472ee754ef6af096340ab1e161f58e85fb0cc7ae6e6866b9359a1657fa6c1", b"88ba6f6c66fc0ef01c938569c2dd1f05475cb56444f4582d06828e77d54ffbe6",
    ]
    for i in range(int(len(testArray) / 2)):
        seed = Decode(testArray[2 * i + 0])
        seckey1 = Decode(testArray[2 * i + 1])
        err, _, _, seckey2 = skycoin.SKY_secp256k1_DeterministicKeyPairIterator(seed)
        assert err == skycoin.SKY_OK
        assert seckey2 == seckey1


def test_Test_Secp256k1_Hash():
    testArray = [
        b"90c56f5b8d78a46fb4cddf6fd9c6d88d6d2d7b0ec35917c7dac12c03b04e444e", b"a70c36286be722d8111e69e910ce4490005bbf9135b0ce8e7a59f84eee24b88b",
		b"a3b08ccf8cbae4955c02f223be1f97d2bb41d92b7f0c516eb8467a17da1e6057", b"e9db072fe5817325504174253a056be7b53b512f1e588f576f1f5a82cdcad302",
		b"7048eb8fa93cec992b93dc8e93c5543be34aad05239d4c036cf9e587bbcf7654", b"5e9133e83c4add2b0420d485e1dcda5c00e283c6509388ab8ceb583b0485c13b",
		b"6d25375591bbfce7f601fc5eb40e4f3dde2e453dc4bf31595d8ec29e4370cd80", b"8d5579cd702c06c40fb98e1d55121ea0d29f3a6c42f5582b902ac243f29b571a",
		b"7214b4c09f584c5ddff971d469df130b9a3c03e0277e92be159279de39462120", b"3a4e8c72921099a0e6a4e7f979df4c8bced63063097835cdfd5ee94548c9c41a",
		b"b13e78392d5446ae304b5fc9d45b85f26996982b2c0c86138afdac8d2ea9016e", b"462efa1bf4f639ffaedb170d6fb8ba363efcb1bdf0c5aef0c75afb59806b8053",
		b"9403bff4240a5999e17e0ab4a645d6942c3a7147c7834e092e461a4580249e6e", b"68dd702ea7c7352632876e9dc2333142fce857a542726e402bb480cad364f260",
		b"2665312a3e3628f4df0b9bc6334f530608a9bcdd4d1eef174ecda99f51a6db94", b"5db72c31d575c332e60f890c7e68d59bd3d0ac53a832e06e821d819476e1f010",
		b"6cb37532c80765b7c07698502a49d69351036f57a45a5143e33c57c236d841ca", b"0deb20ec503b4c678213979fd98018c56f24e9c1ec99af3cd84b43c161a9bb5c",
		b"8654a32fa120bfdb7ca02c487469070eba4b5a81b03763a2185fdf5afd756f3c", b"36f3ede761aa683813013ffa84e3738b870ce7605e0a958ed4ffb540cd3ea504",
		b"66d1945ceb6ef8014b1b6703cb624f058913e722f15d03225be27cb9d8aabe4a", b"6bcb4819a96508efa7e32ee52b0227ccf5fbe5539687aae931677b24f6d0bbbd",
		b"22c7623bf0e850538329e3e6d9a6f9b1235350824a3feaad2580b7a853550deb", b"8bb257a1a17fd2233935b33441d216551d5ff1553d02e4013e03f14962615c16",
		b"a5eebe3469d68c8922a1a8b5a0a2b55293b7ff424240c16feb9f51727f734516", b"d6b780983a63a3e4bcf643ee68b686421079c835a99eeba6962fe41bb355f8da",
		b"479ec3b589b14aa7290b48c2e64072e4e5b15ce395d2072a5a18b0a2cf35f3fd", b"39c5f108e7017e085fe90acfd719420740e57768ac14c94cb020d87e36d06752",
		b"63952334b731ec91d88c54614925576f82e3610d009657368fc866e7b1efbe73", b"79f654976732106c0e4a97ab3b6d16f343a05ebfcc2e1d679d69d396e6162a77",
		b"256472ee754ef6af096340ab1e161f58e85fb0cc7ae6e6866b9359a1657fa6c1", b"387883b86e2acc153aa334518cea48c0c481b573ccaacf17c575623c392f78b2",
    ]

    for i in range(int(len(testArray) / 2)):
        hash1 = Decode(testArray[2 * i + 0])
        hash2 = Decode(testArray[2 * i + 1])
        err, hash3 = skycoin.SKY_secp256k1_Secp256k1Hash(hash1)
        assert err == skycoin.SKY_OK
        assert hash2 == hash3


def test_Test_Secp256k1_Equal():
    for i in range(64):
        _, seed = skycoin.SKY_secp256k1_RandByte(128)
        err , hash1 = skycoin.SKY_secp256k1_Secp256k1Hash(seed)
        assert err == skycoin.SKY_OK
        err, hash2, _, _ = skycoin.SKY_secp256k1_DeterministicKeyPairIterator(seed)
        assert hash1 == hash2


def test_Test_DeterministicWalletGeneration():
    ins = b"8654a32fa120bfdb7ca02c487469070eba4b5a81b03763a2185fdf5afd756f3c"
    secOut = b"10ba0325f1b8633ca463542950b5cd5f97753a9829ba23477c584e7aee9cfbd5"
    pubOut = b"0249964ac7e3fe1b2c182a2f10abe031784e374cc0c665a63bc76cc009a05bc7c6"

    seed = bytes(ins)
    pubkey = bytes()
    seckey = bytes()

    for i in range(1024):
        err, seed, pubkey, seckey = skycoin.SKY_secp256k1_DeterministicKeyPairIterator(seed)
        assert err == skycoin.SKY_OK
    assert seckey == Decode(secOut)
    assert pubkey == Decode(pubOut)


def test_Test_ECDH():
    _, pubkey1, seckey1 = skycoin.SKY_secp256k1_GenerateKeyPair()
    _, pubkey2, seckey2 = skycoin.SKY_secp256k1_GenerateKeyPair()

    err, puba = skycoin.SKY_secp256k1_ECDH(pubkey1, seckey2)
    assert err == skycoin.SKY_OK
    err, pubb = skycoin.SKY_secp256k1_ECDH(pubkey2, seckey1)
    assert err == skycoin.SKY_OK
    assert puba != None
    assert pubb != None
    assert puba == pubb


def test_Test_ECDH2():
    for i in range(16 * 1024):
        _, pubkey1, seckey1 = skycoin.SKY_secp256k1_GenerateKeyPair()
        _, pubkey2, seckey2 = skycoin.SKY_secp256k1_GenerateKeyPair()
        err, puba = skycoin.SKY_secp256k1_ECDH(pubkey1, seckey2)
        assert err == skycoin.SKY_OK
        err, pubb = skycoin.SKY_secp256k1_ECDH(pubkey2, seckey1)
        assert err == skycoin.SKY_OK
        assert puba != None
        assert pubb != None
        assert puba == pubb


_testSeckey = [    b"08efb79385c9a8b0d1c6f5f6511be0c6f6c2902963d874a3a4bacc18802528d3", 	b"78298d9ecdc0640c9ae6883201a53f4518055442642024d23c45858f45d0c3e6", 	b"04e04fe65bfa6ded50a12769a3bd83d7351b2dbff08c9bac14662b23a3294b9e", 	b"2f5141f1b75747996c5de77c911dae062d16ae48799052c04ead20ccd5afa113"]    


def test_Test_Abnormal_Keys2():
    for i in range(len(_testSeckey)):
        err, seckey1 = skycoin.SKY_base58_String2Hex(_testSeckey[i])
        assert err == skycoin.SKY_OK
        err, pubkey1 = skycoin.SKY_secp256k1_PubkeyFromSeckey(seckey1)
        assert err == skycoin.SKY_OK
        assert pubkey1 != None
        assert seckey1 != None
        assert pubkey1 != None
        err, value = skycoin.SKY_secp256k1_VerifyPubkey(pubkey1)
        assert err == skycoin.SKY_OK
        assert value == 1


def test_Test_Abnormal_Keys3():
    for i in range(len(_testSeckey)):
        err, seckey1 = skycoin.SKY_base58_String2Hex(_testSeckey[i])
        assert err == skycoin.SKY_OK
        err, pubkey1 = skycoin.SKY_secp256k1_PubkeyFromSeckey(seckey1)
        assert err == skycoin.SKY_OK
        err, seckey2 = skycoin.SKY_base58_String2Hex(_testSeckey[random.randint(0, len(_testSeckey) - 1)])
        assert err == skycoin.SKY_OK
        err, pubkey2 = skycoin.SKY_secp256k1_PubkeyFromSeckey(seckey2)
        assert err == skycoin.SKY_OK
        assert pubkey1 != None
        assert pubkey2 != None
        err, puba = skycoin.SKY_secp256k1_ECDH(pubkey1, seckey2)
        assert err == skycoin.SKY_OK
        err, pubb = skycoin.SKY_secp256k1_ECDH(pubkey2, seckey1)
        assert err == skycoin.SKY_OK
        assert puba != None, pubb != None
        assert pubb == puba

