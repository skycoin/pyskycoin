# Compilation output
<<<<<<< HEAD
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
=======
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
>>>>>>> remotes/origin/stdevStark_t4_make_buildswig

LIB_FILES = $(shell find $(SKYCOIN_DIR)/lib/cgo -type f -name "*.go")
SRC_FILES = $(shell find $(SKYCOIN_DIR)/src -type f -name "*.go")
SWIG_FILES = $(shell find $(SKYCOIN_DIR)/lib/swig -type f -name "*.i")

configure:
	mkdir -p $(BUILD_DIR)/usr/tmp $(BUILD_DIR)/usr/lib $(BUILD_DIR)/usr/include
	mkdir -p $(BUILDLIBC_DIR) $(BIN_DIR) $(INCLUDE_DIR)

$(BUILDLIBC_DIR)/libskycoin.a: $(LIB_FILES) $(SRC_FILES)
	cd $(SKYCOIN_DIR) && GOPATH="$(GOPATH_DIR)" make build-libc-static
	grep -v _Complex $(INCLUDE_DIR)/libskycoin.h > swig/include/libskycoin.h

## Build libskycoin C client library
build-libc: configure $(BUILDLIBC_DIR)/libskycoin.a

build-swig:
	#Generate structs.i from skytypes.gen.h
	rm -Rf $(SWIG_DIR)/structs.i
	cp $(INCLUDE_DIR)/skytypes.gen.h $(SWIG_DIR)/structs.i
	sed -i 's/#/%/g' $(SWIG_DIR)/structs.i
	swig -python -outdir . -o swig/pyskycoin_wrap.c skycoin/lib/swig/skycoin.i
develop:
	python setup.py develop
install: build-libc wrapper 
	python setup.py install

pyskycoin: build-libc tests/_skycoin.so

test: build-libc wrapper develop
test: build-libc build-swig
	tox
