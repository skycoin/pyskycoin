# Compilation output
BUILD_DIR = skycoin/build
BUILDLIB_DIR = $(BUILD_DIR)/libskycoin
LIB_DIR = lib
LIB_FILES = $(shell find ./skycoin/lib/cgo -type f -name "*.go")
SRC_FILES = $(shell find ./skycoin/src -type f -name "*.go")
SWIG_FILES = $(shell find ./lib -type f -name "*.i")
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

tests/_skycoin.so: $(SWIG_FILES)
	echo "Building Pyskycoin"
	rm -Rf lib/include/libskycoin.h
	grep -v _Complex skycoin/include/libskycoin.h >> lib/include/libskycoin.h
	mkdir -p lib/wrappers
	swig -python -outdir tests -o lib/wrappers/pyskycoin_wrap.c lib/skycoin.i
	$(CC) -O2 -fPIC -c lib/wrappers/pyskycoin_wrap.c -I/usr/include  -I/usr/include/python2.7 -Iskycoin/include/ -o lib/wrappers/pyskycoin_wrap.o
	$(CC) -shared lib/wrappers/pyskycoin_wrap.o -o tests/_skycoin.so $(BUILDLIB_DIR)/libskycoin.a

pyskycoin: build-libc tests/_skycoin.so
	
test: pyskycoin
	tox
