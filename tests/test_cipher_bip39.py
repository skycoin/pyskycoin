import skycoin
import tests.utils


def test_TestIsMnemonicValid():
    err, m = skycoin.SKY_bip39_NewDefaultMnemomic()
    assert err == skycoin.SKY_OK
    assert skycoin.SKY_bip39_IsMnemonicValid(m)

    # Truncated
    m = m[:len(m) - 15]
    assert skycoin.SKY_bip39_IsMnemonicValid(m)[1] == False

    # Trailing whitespace
    err, m = skycoin.SKY_bip39_NewDefaultMnemomic()
    assert err == skycoin.SKY_OK
    m += b' '
    assert skycoin.SKY_bip39_IsMnemonicValid(m)[1] == False

    err, m = skycoin.SKY_bip39_NewDefaultMnemomic()
    assert err == skycoin.SKY_OK
    m += b'/n'
    assert skycoin.SKY_bip39_IsMnemonicValid(m)[1] == False

    # Preceding whitespace
    err, m = skycoin.SKY_bip39_NewDefaultMnemomic()
    assert err == skycoin.SKY_OK
    m = b' ' + m
    assert skycoin.SKY_bip39_IsMnemonicValid(m)[1] == False

    err, m = skycoin.SKY_bip39_NewDefaultMnemomic()
    assert err == skycoin.SKY_OK
    m = b'\n' + m
    assert skycoin.SKY_bip39_IsMnemonicValid(m)[1] == False

    # Extra whitespace between words
    err, m = skycoin.SKY_bip39_NewDefaultMnemomic()
    assert err == skycoin.SKY_OK
    ms = m.split(b' ')
    m = b'  '.join(ms)
    assert skycoin.SKY_bip39_IsMnemonicValid(m)[1] == False

    # Contains invalid word
    err, m = skycoin.SKY_bip39_NewDefaultMnemomic()
    assert err == skycoin.SKY_OK
    ms = m.split(b' ')
    ms[2] = b'foo'
    m = b' '.join(ms)
    assert skycoin.SKY_bip39_IsMnemonicValid(m)[1] == False

# Invalid number of words
    err, m = skycoin.SKY_bip39_NewDefaultMnemomic()
    assert err == skycoin.SKY_OK
    ms = m.split(b' ')
    m = b'  '.join(ms[:len(ms) - 1])
    assert skycoin.SKY_bip39_IsMnemonicValid(m)[1] == False
