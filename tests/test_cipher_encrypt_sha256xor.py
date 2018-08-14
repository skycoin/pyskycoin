import skycoin

tt = [
    [
        b"data length=1 password is empty=true",
    	skycoin.SKY_cipher_RandByte(1)[1],
    	b"",
    	b"missing password",
    ],
    [
        b"data length=1  password is empty=false",
    	skycoin.SKY_cipher_RandByte(1)[1],
    	b"key",
    	None,
    ],
    [
        b"data length<32 password is empty=false",
    	skycoin.SKY_cipher_RandByte(2)[1],
    	b"pwd",
    	None,
    ],
    [
        b"data length=32 password is empty=false",
    	skycoin.SKY_cipher_RandByte(32)[1],
    	b"pwd",
    	None,
    ],
    [
        b"data length=2*32 password is empty=false",
    	skycoin.SKY_cipher_RandByte(64)[1],
    	b"9JMkCPphe73NQvGhmab",
    	None,
    ],
    [
        b"data length>2*32 password is empty=false",
    	skycoin.SKY_cipher_RandByte(65)[1],
    	b"9JMkCPphe73NQvGhmab",
    	None,
    ],
]

