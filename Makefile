# Compilation output
.ONESHELL:
SHELL := /bin/bash

PYTHON_BIN = python
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
FULL_PATH_LIB = $(PWD)/$(BUILDLIBC_DIR)

LIB_FILES = $(shell find $(SKYCOIN_DIR)/lib/cgo -type f -name "*.go")
SRC_FILES = $(shell find $(SKYCOIN_DIR)/src -type f -name "*.go")
SWIG_FILES = $(shell find $(LIBSWIG_DIR) -type f -name "*.i")
HEADER_FILES = $(shell find $(SKYCOIN_DIR)/include -type f -name "*.h")

ifeq ($(shell uname -s),Linux)
	TEMP_DIR = tmp
else ifeq ($(shell uname -s),Darwin)
	TEMP_DIR = $TMPDIR
endif

configure:
	mkdir -p $(BUILD_DIR)/usr/tmp $(BUILD_DIR)/usr/lib $(BUILD_DIR)/usr/include
	mkdir -p $(BUILDLIBC_DIR) $(BIN_DIR) $(INCLUDE_DIR)

$(BUILDLIBC_DIR)/libskycoin.a: $(LIB_FILES) $(SRC_FILES) $(HEADER_FILES)
	rm -f $(BUILDLIBC_DIR)/libskycoin.a
	GOPATH="$(GOPATH_DIR)" make -C $(SKYCOIN_DIR) build-libc-static
	ls $(BUILDLIBC_DIR)
	rm -f swig/include/libskycoin.h
	mkdir -p swig/include
	grep -v _Complex $(INCLUDE_DIR)/libskycoin.h > swig/include/libskycoin.h

## Build libskycoin C client library
build-libc: configure $(BUILDLIBC_DIR)/libskycoin.a

build-swig:
	#Generate structs.i from skytypes.gen.h
	rm -f $(LIBSWIG_DIR)/structs.i
	cp $(INCLUDE_DIR)/skytypes.gen.h $(LIBSWIG_DIR)/structs.i
	#sed -i 's/#/%/g' $(LIBSWIG_DIR)/structs.i
	{ \
		if [[ "$$(uname -s)" == "Darwin" ]]; then \
			sed -i '.kbk' 's/#/%/g' $(LIBSWIG_DIR)/structs.i ;\
		else \
			sed -i 's/#/%/g' $(LIBSWIG_DIR)/structs.i ;\
		fi \
	}
	rm -f ./skycoin/skycoin.py
	rm -f swig/pyskycoin_wrap.c
	swig -python -Iswig/include -I$(INCLUDE_DIR) -outdir ./skycoin/ -o swig/pyskycoin_wrap.c $(LIBSWIG_DIR)/skycoin.coin.i

develop:
	$(PYTHON_BIN) setup.py develop

build-libc-swig: build-libc build-swig

test-ci:
	tox

test: build-libc build-swig develop
	$(PYTHON_BIN) setup.py test
