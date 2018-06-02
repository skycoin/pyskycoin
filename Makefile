# Compilation output
BUILD_DIR = skycoin/build
BUILDLIB_DIR = $(BUILD_DIR)/libskycoin
LIB_DIR = lib
LIB_FILES = $(shell find ./skycoin/lib/cgo -type f -name "*.go")
SRC_FILES = $(shell find ./skycoin/src -type f -name "*.go")
SWIG_FILES = $(shell find ./skycoin/lib/swig -type f -name "*.i")
BIN_DIR = skycoin/bin
INCLUDE_DIR = skycoin/include
LIBSRC_DIR = skycoin/lib/cgo


configure-build:
	mkdir -p $(BUILD_DIR)/usr/tmp $(BUILD_DIR)/usr/lib $(BUILD_DIR)/usr/include
	mkdir -p $(BUILDLIB_DIR) $(BIN_DIR) $(INCLUDE_DIR)

$(BUILDLIB_DIR)/libskycoin.a: $(LIB_FILES) $(SRC_FILES)
	rm -Rf $(BUILDLIB_DIR)/*
	go build -buildmode=c-archive -o $(BUILDLIB_DIR)/libskycoin.a  $(LIB_FILES)
	mv $(BUILDLIB_DIR)/libskycoin.h $(INCLUDE_DIR)/

build-libc: configure-build $(BUILDLIB_DIR)/libskycoin.a ## Build libskycoin C client library

tests/_skycoin.so: #$(SWIG_FILES)
	echo "Building Pyskycoin"
	rm -Rf swig/include/_libskycoin.h
	grep -v _Complex skycoin/include/libskycoin.h >> swig/include/_libskycoin.h
	swig -python -outdir tests -o swig/pyskycoin_wrap.c skycoin/lib/swig/skycoin.i
	$(CC) -O2 -fPIC -c swig/pyskycoin_wrap.c -I/usr/include  -I/usr/include/python2.7 -Iskycoin/include/ -o swig/pyskycoin_wrap.o
	$(CC) -shared swig/pyskycoin_wrap.o -o tests/_skycoin.so $(BUILDLIB_DIR)/libskycoin.a

build/lib.linux-x86_64-2.7/_skycoin.so:
	echo "Building Pyskycoin"
	rm -Rf swig/include/_libskycoin.h
	grep -v _Complex skycoin/include/libskycoin.h >> swig/include/_libskycoin.h
	mkdir -p build/lib.linux-x86_64-2.7
	swig -python -outdir tests -o swig/pyskycoin_wrap.c skycoin/lib/swig/skycoin.i
	$(CC) -O2 -fPIC -c swig/pyskycoin_wrap.c -I/usr/include  -I/usr/include/python2.7 -Iskycoin/include/ -o swig/pyskycoin_wrap.o
	$(CC) -shared swig/pyskycoin_wrap.o -o build/lib.linux-x86_64-2.7/_skycoin.so $(BUILDLIB_DIR)/libskycoin.a
wrapper:
	swig -python -outdir swig -o swig/pyskycoin_wrap.c skycoin/lib/swig/skycoin.i
develop:
	python setup.py develop

pyskycoin: build-libc tests/_skycoin.so

test: pyskycoin
	tox
