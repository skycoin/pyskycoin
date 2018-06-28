# Compilation output

PWD = $(shell pwd)
GOPATH_DIR = $(PWD)/gopath
SKYCOIN_DIR = gopath/src/github.com/skycoin/skycoin
SKYBUILD_DIR = $(SKYCOIN_DIR)/build
BUILDLIBC_DIR = $(SKYBUILD_DIR)/libskycoin
LIBC_DIR = $(SKYCOIN_DIR)/lib/cgo
LIBSWIG_DIR = $(SKYCOIN_DIR)/lib/swig
BUILD_DIR = build
BIN_DIR = $(SKYCOIN_DIR)/bin
INCLUDE_DIR = $(SKYCOIN_DIR)/include

LIB_FILES = $(shell find $(SKYCOIN_DIR)/lib/cgo -type f -name "*.go")
SRC_FILES = $(shell find $(SKYCOIN_DIR)/src -type f -name "*.go")
SWIG_FILES = $(shell find $(LIBSWIG_DIR) -type f -name "*.i")

ifeq ($(shell uname -s),Darwin)
	SED_COMMAND="sed -i '.kbk' 's/#/%/g' $(LIBSWIG_DIR)/structs.i"
else
	SED_COMMAND="sed -i 's/#/%/g' $(LIBSWIG_DIR)/structs.i"

configure:
	mkdir -p $(BUILD_DIR)/usr/tmp $(BUILD_DIR)/usr/lib $(BUILD_DIR)/usr/include
	mkdir -p $(BUILDLIBC_DIR) $(BIN_DIR) $(INCLUDE_DIR)

$(BUILDLIBC_DIR)/libskycoin.a: $(LIB_FILES) $(SRC_FILES)
	cd $(SKYCOIN_DIR) && GOPATH="$(GOPATH_DIR)" make build-libc-static
	rm -Rf swig/include/libskycoin.h
	mkdir -p swig/include
	grep -v _Complex $(INCLUDE_DIR)/libskycoin.h > swig/include/libskycoin.h

## Build libskycoin C client library
build-libc: configure $(BUILDLIBC_DIR)/libskycoin.a

build-swig:
	#Generate structs.i from skytypes.gen.h
	rm -Rf $(LIBSWIG_DIR)/structs.i
	cp $(INCLUDE_DIR)/skytypes.gen.h $(LIBSWIG_DIR)/structs.i
	eval "$SED_COMMAND"
	swig -python -Iswig/include -I$(INCLUDE_DIR) -outdir . -o swig/pyskycoin_wrap.c $(LIBSWIG_DIR)/skycoin.i
	
develop:
	python setup.py develop
	
build-libpy: build-libc build-swig
	python setup.py install
	
test: build-libc build-swig
	tox
