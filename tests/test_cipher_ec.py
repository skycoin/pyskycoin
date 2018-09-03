import skycoin

def test_TestECmult():
    _, u1 = skycoin.secp256k1go.NumberCreate()
    _, u2 = skycoin.secp256k1go.NumberCreate()
    public_keyj = expres = pr = skycoin.secp256k1go.XYZ()
    
    skycoin.secp256k1go.FieldSetHex(public_keyj.X, b"0EAEBCD1DF2DF853D66CE0E1B0FDA07F67D1CABEFDE98514AAD795B86A6EA66D")
    skycoin.secp256k1go.FieldSetHex(public_keyj.Y, b"BEB26B67D7A00E2447BAECCC8A4CEF7CD3CAD67376AC1C5785AEEBB4F6441C16")
    skycoin.secp256k1go.FieldSetHex(public_keyj.Z, b"0000000000000000000000000000000000000000000000000000000000000001")
    skycoin.secp256k1go.NumberSetHex(u1, b"B618EBA71EC03638693405C75FC1C9ABB1A74471BAAF1A3A8B9005821491C4B4")
    skycoin.secp256k1go.NumberSetHex(u2, b"8554470195DE4678B06EDE9F9286545B51FF2D9AA756CE35A39011783563EA60")
    skycoin.secp256k1go.FieldSetHex(expres.X, b"EB6752420B6BDB40A760AC26ADD7E7BBD080BF1DF6C0B009A0D310E4511BDF49")
    skycoin.secp256k1go.FieldSetHex(expres.Y, b"8E8CEB84E1502FC536FFE67967BC44314270A0B38C79865FFED5A85D138DCA6B")
    skycoin.secp256k1go.FieldSetHex(expres.Z, b"813925AF112AAB8243F8CCBADE4CC7F63DF387263028DE6E679232A73A7F3C31")
    
    err = skycoin.secp256k1go.XYZECmult(public_keyj, pr, u2, u1)
    assert err == skycoin.SKY_OK
    err, val = skycoin.secp256k1go.XYZEquals(pr, expres) 
    assert err == skycoin.SKY_OK and val

def test_TestMultGen():
    _, noce = skycoin.secp256k1go.NumberCreate()
    assert _ == 0
    x = skycoin.secp256k1go.Field()
    y = skycoin.secp256k1go.Field()
    z = skycoin.secp256k1go.Field()
    pr = skycoin.secp256k1go.XYZ()
    skycoin.secp256k1go.NumberSetHex(noce, b"9E3CD9AB0F32911BFDE39AD155F527192CE5ED1F51447D63C4F154C118DA598E")
    skycoin.secp256k1go.FieldSetHex(x, b"02D1BF36D37ACD68E4DD00DB3A707FD176A37E42F81AEF9386924032D3428FF0")
    skycoin.secp256k1go.FieldSetHex(y, b"FD52E285D33EC835230EA69F89D9C38673BD5B995716A4063C893AF02F938454")
    skycoin.secp256k1go.FieldSetHex(z, b"4C6ACE7C8C062A1E046F66FD8E3981DC4E8E844ED856B5415C62047129268C1B")
    skycoin.secp256k1go.ECmultGen(pr, noce)
    skycoin.secp256k1go.FieldNormalize(pr.X)
    skycoin.secp256k1go.FieldNormalize(pr.Y)
    skycoin.secp256k1go.FieldNormalize(pr.Z)
    err, val = skycoin.secp256k1go.FieldEquals(pr.X, x)
    assert err == skycoin.SKY_OK and val
    err, val = skycoin.secp256k1go.FieldEquals(pr.Y, y)
    assert err == skycoin.SKY_OK and val
    err, val = skycoin.secp256k1go.FieldEquals(pr.Z, z)
    assert err == skycoin.SKY_OK and val