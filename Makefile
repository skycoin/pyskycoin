pyskycoin:
	echo "Building Pyskycoin"
	rm -Rf lib/include/libskycoin.h
	grep -v _Complex skycoin/include/libskycoin.h >> lib/include/libskycoin.h
	swig -python -outdir tests -o lib/wrappers/pyskycoin_wrap.c lib/skycoin.i
	cc -O2 -fPIC -c lib/wrappers/pyskycoin_wrap.c -I/usr/include  -I/usr/include/python2.7 -Iskycoin/include/ -o lib/wrappers/pyskycoin_wrap.o
	cc -shared lib/wrappers/pyskycoin_wrap.o -o tests/_skycoin.so skycoin/build/libskycoin/libskycoin.a
