# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package
import skycoin
import sys
from tests.utils.skyerror import error


# Test with handles and strings
def test_loadconfig():
    err, old_coin = skycoin.SKY_cli_Getenv(b"COIN")
    assert err == error["SKY_OK"]
    err = skycoin.SKY_cli_Setenv(b"COIN", b"foocoin")
    assert err == error["SKY_OK"]
    err, configHandle = skycoin.SKY_cli_LoadConfig()
    assert err == error["SKY_OK"]
    err, new_coin = skycoin.SKY_cli_Config_GetCoin(configHandle)
    assert err == error["SKY_OK"]
    assert new_coin == b"foocoin"
    skycoin.SKY_handle_close(configHandle)
    err = skycoin.SKY_cli_Setenv(b"COIN", old_coin)
    assert err == error["SKY_OK"]


# Test with slices as []byte
def test_Sha256XorEncrypt():
    err, data = skycoin.SKY_cipher_RandByte(32)
    assert err == error["SKY_OK"]
    assert len(data) == 32
    pwd = b"pwd"
    err, encrypted = skycoin.SKY_encrypt_Sha256Xor_Encrypt(
        data, pwd)
    assert err == error["SKY_OK"]
    err, decrypted = skycoin.SKY_encrypt_Sha256Xor_Decrypt(
        encrypted, pwd)
    assert err == error["SKY_OK"]
    assert data == decrypted


# Test with struct and slices
def test_encrypt_ScryptChacha20poly1305Encrypt():
    encrypt_settings = skycoin.encrypt__ScryptChacha20poly1305()
    encrypt_settings.N = 2
    encrypt_settings.R = 8
    encrypt_settings.P = 1
    encrypt_settings.KeyLen = 32

    err, data = skycoin.SKY_cipher_RandByte(32)
    assert err == error["SKY_OK"]
    assert len(data) == 32
    err, encrypted = skycoin.SKY_encrypt_ScryptChacha20poly1305_Encrypt(
        encrypt_settings, data, b"password")
    assert err == error["SKY_OK"]
    err, decrypted = skycoin.SKY_encrypt_ScryptChacha20poly1305_Decrypt(
        encrypt_settings, encrypted, b"password")
    assert err == error["SKY_OK"]
    assert data == decrypted


# Test with struct containing array
def test_cipherAddress():
    address = skycoin.cipher__Address()
    err = skycoin.SKY_cipher_DecodeBase58Address(
        b"2GgFvqoyk9RjwVzj8tqfcXVXB4orBwoc9qv", address)
    assert err == error["SKY_OK"]

    err, bytes = skycoin.SKY_cipher_Address_BitcoinBytes(address)
    assert err == error["SKY_OK"]
    assert len(bytes) > 0
    address2 = skycoin.cipher__Address()
    err = skycoin.SKY_cipher_BitcoinAddressFromBytes(bytes, address2)
    assert err == error["SKY_OK"]
    assert address == address2


# Test with array typedefs. Array typedefs were wrapped inside a struct
# Notice that the type used is cipher_PubKey instead of cipher__PubKey
def test_GenerateKeyPairs():
    err, data = skycoin.SKY_cipher_RandByte(32)
    assert err == error["SKY_OK"]

    pubkey = skycoin.cipher_PubKey()
    seckey = skycoin.cipher_SecKey()

    err = skycoin.SKY_cipher_GenerateDeterministicKeyPair(
        data, pubkey, seckey)
    assert err == error["SKY_OK"]

    address = skycoin.cipher__Address()
    err = skycoin.SKY_cipher_AddressFromPubKey(pubkey, address)
    assert err == error["SKY_OK"]
    err = skycoin.SKY_cipher_Address_Verify(address, pubkey)
    assert err == error["SKY_OK"]

    err, address_string = skycoin.SKY_cipher_Address_String(address)
    assert err == error["SKY_OK"]
    address2 = skycoin.cipher__Address()
    err = skycoin.SKY_cipher_DecodeBase58Address(address_string, address2)
    assert err == error["SKY_OK"]
    assert address == address2


def test_GenerateDeterministicKeyPairs():
    err, seed = skycoin.SKY_cipher_RandByte(32)
    assert err == error["SKY_OK"]
    err, seckeys = skycoin.SKY_cipher_GenerateDeterministicKeyPairs(seed, 2)
    assert err == error["SKY_OK"]
    length = len(seckeys)
    assert length == 2
    for seckey in seckeys:
        address = skycoin.cipher__Address()
        err = skycoin.SKY_cipher_AddressFromSecKey(seckey, address)
        assert err == error["SKY_OK"]
        pubkey = skycoin.cipher_PubKey()
        err = skycoin.SKY_cipher_PubKeyFromSecKey(seckey, pubkey)
        assert err == error["SKY_OK"]
        err = skycoin.SKY_cipher_PubKey_Verify(pubkey)
        assert err == error["SKY_OK"]


def test_GenerateDeterministicKeyPairsSeed():
    err, seed = skycoin.SKY_cipher_RandByte(32)
    assert err == error["SKY_OK"]
    err, newseed, seckeys = \
        skycoin.SKY_cipher_GenerateDeterministicKeyPairsSeed(seed, 2)
    length = len(seckeys)
    assert length == 2


def test_Transaction():
    err, handle = skycoin.SKY_coin_Create_Transaction()
    assert err == error["SKY_OK"]
    pubkey = skycoin.cipher_PubKey()
    seckey = skycoin.cipher_SecKey()
    err = skycoin.SKY_cipher_GenerateKeyPair(pubkey, seckey)
    assert err == error["SKY_OK"]
    address = skycoin.cipher__Address()
    err = skycoin.SKY_cipher_AddressFromPubKey(pubkey, address)
    assert err == error["SKY_OK"]
    err = skycoin.SKY_coin_Transaction_PushOutput(
        handle, address, 1000000, 100)
    assert err == error["SKY_OK"]
    err, transaction = skycoin.SKY_coin_Get_Transaction_Object(handle)
    assert err == error["SKY_OK"]
    assert transaction.Length >= 0
    skycoin.SKY_handle_close(handle)


def test_Transactions():
    err, handleTransactions = skycoin.SKY_coin_Create_Transactions()
    assert err == error["SKY_OK"]
    err, handleTransaction1 = skycoin.SKY_coin_Create_Transaction()
    assert err == error["SKY_OK"]
    skycoin.SKY_coin_Transactions_Add(handleTransactions, handleTransaction1)
    err, handleTransaction2 = skycoin.SKY_coin_Create_Transaction()
    assert err == error["SKY_OK"]
    skycoin.SKY_coin_Transactions_Add(handleTransactions, handleTransaction2)
    err, transactions = skycoin.SKY_coin_Get_Transactions_Object(
        handleTransactions)
    skycoin.SKY_handle_close(handleTransaction1)
    skycoin.SKY_handle_close(handleTransaction2)
    skycoin.SKY_handle_close(handleTransactions)


def test_Transactions2():
    err, handleTransaction1 = skycoin.SKY_coin_Create_Transaction()
    assert err == error["SKY_OK"]
    err, handleTransaction2 = skycoin.SKY_coin_Create_Transaction()
    assert err == error["SKY_OK"]
    err, transaction1 = skycoin.SKY_coin_Get_Transaction_Object(
        handleTransaction1)
    assert err == error["SKY_OK"]
    err, transaction2 = skycoin.SKY_coin_Get_Transaction_Object(
        handleTransaction2)
    assert err == error["SKY_OK"]
    assert transaction1 == transaction2
    pubkey = skycoin.cipher_PubKey()
    seckey = skycoin.cipher_SecKey()
    err = skycoin.SKY_cipher_GenerateKeyPair(pubkey, seckey)
    assert err == error["SKY_OK"]
    address = skycoin.cipher__Address()
    err = skycoin.SKY_cipher_AddressFromPubKey(pubkey, address)
    assert err == error["SKY_OK"]
    err = skycoin.SKY_coin_Transaction_PushOutput(
        handleTransaction1, address, 1000000, 100)
    assert err == error["SKY_OK"]
    assert not (transaction1 == transaction2)
    skycoin.SKY_handle_close(handleTransaction1)
    skycoin.SKY_handle_close(handleTransaction2)


def test_SHA256NULL():
    sha256 = skycoin.cipher_SHA256()
    err, result = skycoin.SKY_cipher_SHA256_Null(sha256)
    assert err == error["SKY_OK"]
    assert result == True


def test_AddUint64():
    err, n = skycoin.SKY_coin_AddUint64(10, 11)
    assert err == error["SKY_OK"]
    assert int(21) == n
    err, n = skycoin.SKY_coin_AddUint64(int(0xFFFFFFFFFFFFFFFF), 1)
    assert err == error["SKY_ErrUint64AddOverflow"]


def test_Ripemd160Set():
    h = skycoin.cipher_Ripemd160()
    _, b = skycoin.SKY_cipher_RandByte(21)
    assert skycoin.SKY_cipher_Ripemd160_Set(h, b) == error["SKY_ERROR"]
    _, b = skycoin.SKY_cipher_RandByte(100)
    assert skycoin.SKY_cipher_Ripemd160_Set(h, b) == error["SKY_ERROR"]
    _, b = skycoin.SKY_cipher_RandByte(19)
    assert skycoin.SKY_cipher_Ripemd160_Set(h, b) == error["SKY_ERROR"]
    _, b = skycoin.SKY_cipher_RandByte(0)
    assert skycoin.SKY_cipher_Ripemd160_Set(h, b) == error["SKY_ERROR"]
    _, b = skycoin.SKY_cipher_RandByte(20)
    assert skycoin.SKY_cipher_Ripemd160_Set(h, b) == error["SKY_OK"]
    _, b1 = skycoin.SKY_cipher_RandByte(20)
    skycoin.SKY_cipher_Ripemd160_Set(h, b1)
    assert h.compareToString(str(b))