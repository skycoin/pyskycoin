import skycoin
import json
import base64
import tests.utils

define = {
    "PLAINTEXT": b"plaintext",
    "PASSWORD": b"password",
    "ENCRYPTED": b"dQB7Im4iOjUyNDI4OCwiciI6OCwicCI6MSwia2V5TGVuIjozMiwic2FsdCI6ImpiejUrSFNjTFFLWkI5T0tYblNNRmt2WDBPY3JxVGZ0ZFpDNm9KUFpaeHc9Iiwibm9uY2UiOiJLTlhOQmRQa1ZUWHZYNHdoIn3PQFmOot0ETxTuv//skTG7Q57UVamGCgG5",
    "SCRYPTCHACHA20METALENGTHSIZE": 2,
}


def test_TestScryptChacha20poly1305Encrypt():
    for i in range(20)[1:]:
        crypto = skycoin.encrypt__ScryptChacha20poly1305()
        crypto.R = 8
        crypto.P = 1
        crypto.KeyLen = 32
        crypto.N = 1 << i
        _, encData = skycoin.SKY_encrypt_ScryptChacha20poly1305_Encrypt(
            crypto, define["PLAINTEXT"], define["PASSWORD"])
        assert _ == skycoin.SKY_OK
        Data = base64.standard_b64decode(encData)
        ml_ = [x for x in Data]
        if type(ml_[0]) == int:
            ml = ml_[0]
            _Data = [chr(x) for x in Data]
            D = ""
            for x in _Data:
                D += x
            Data = D
        else:
            ml = ord(ml_[0])
        assert int(define["SCRYPTCHACHA20METALENGTHSIZE"] + ml) <= len(Data)
        m = json.loads(Data[define["SCRYPTCHACHA20METALENGTHSIZE"]:define["SCRYPTCHACHA20METALENGTHSIZE"] + ml])
        print(m)
        assert m["n"] == 1 << i
        assert m["r"] == 8
        assert m["p"] == 1
        assert m["keyLen"] == 32


def test_TestScryptChacha20poly1305Decrypt():
    encrypto = b"dQB7Im4iOjUyNDI4OCwiciI6OCwicCI6MSwia2V5TGVuIjozMiwic2FsdCI6ImpiejUrSFNjTFFLWkI5T0tYblNNRmt2WDBPY3JxVGZ0ZFpDNm9KUFpaeHc9Iiwibm9uY2UiOiJLTlhOQmRQa1ZUWHZYNHdoIn3PQFmOot0ETxTuv//skTG7Q57UVamGCgG5"
    password = b"pwd"
    invalid_passwd = b"wrong password"
    crypto = skycoin.encrypt__ScryptChacha20poly1305()
    crypto.R = 8
    crypto.P = 1
    crypto.KeyLen = 32
    crypto.N = 1 << 19
    err, decrypted = skycoin.SKY_encrypt_ScryptChacha20poly1305_Decrypt(
        crypto, encrypto, password)
    assert err == skycoin.SKY_OK and decrypted == define["PLAINTEXT"]
    # Wrong Password
    err, decrypted = skycoin.SKY_encrypt_ScryptChacha20poly1305_Decrypt(
        crypto, encrypto, invalid_passwd)
    assert err == skycoin.SKY_ERROR
    # Missing Password
    err, decrypted = skycoin.SKY_encrypt_ScryptChacha20poly1305_Decrypt(
        crypto, encrypto, b"")
    assert err == skycoin.SKY_ERROR
