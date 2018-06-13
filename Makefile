# Compilation output
BUILD_DIR = skycoin/build
BUILDLIB_DIR = $(BUILD_DIR)/libskycoin
LIB_DIR = lib
LIB_FILES = $(shell find ./skycoin/lib/cgo -type f -name "*.go")
SRC_FILES = $(shell find ./skycoin/src -type f -name "*.go")
SWIG_FILES = $(shell find ./skycoin/lib/swig -type f -name "*.i")
BIN_DIR = skycoin/bin
INCLUDE_DIR = skycoin/include
SWIG_DIR = skycoin/lib/swig
LIBSRC_DIR = skycoin/lib/cgo


configure-build:
	mkdir -p $(BUILD_DIR)/usr/tmp $(BUILD_DIR)/usr/lib $(BUILD_DIR)/usr/include
	mkdir -p $(BUILDLIB_DIR) $(BIN_DIR) $(INCLUDE_DIR)

$(BUILDLIB_DIR)/libskycoin.a: $(LIB_FILES) $(SRC_FILES)
	rm -Rf $(BUILDLIB_DIR)/*
	go build -buildmode=c-archive -o $(BUILDLIB_DIR)/libskycoin.a  $(LIB_FILES)
	mv $(BUILDLIB_DIR)/libskycoin.h $(INCLUDE_DIR)/
	rm -Rf swig/include/libskycoin.h
	grep -v _Complex $(INCLUDE_DIR)/libskycoin.h >> swig/include/libskycoin.h

build-libc: configure-build $(BUILDLIB_DIR)/libskycoin.a ## Build libskycoin C client library

wrapper:
	rm -Rf $(SWIG_DIR)/structs.i
	cp $(INCLUDE_DIR)/skytypes.gen.h $(SWIG_DIR)/structs.i
	sed -i 's/#include "/%include "..\/..\/include\//g' $(SWIG_DIR)/structs.i
	swig -python  -outdir . -o swig/pyskycoin_wrap.c skycoin/lib/swig/skycoin.i
develop:
	python setup.py develop

pyskycoin: build-libc tests/_skycoin.so

test: build-libc wrapper
	tox
