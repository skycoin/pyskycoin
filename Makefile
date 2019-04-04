.DEFAULT_GOAL := help
.PHONY: configure build-libc build-swig develop build-libc-swig build 
.PHONY: test test-ci help format lint

# Compilation output
.ONESHELL:
SHELL := /bin/bash

PYTHON_BIN   ?= python
MKFILE_PATH   = $(abspath $(lastword $(MAKEFILE_LIST)))
REPO_ROOT     = $(dir $(MKFILE_PATH))
GOPATH_DIR    = gopath
SKYLIBC_DIR  ?= $(GOPATH_DIR)/src/github.com/skycoin/libskycoin
SKYCOIN_DIR  ?= $(SKYLIBC_DIR)/vendor/github.com/skycoin/skycoin
SKYBUILD_DIR  = $(SKYLIBC_DIR)/build
BUILDLIBC_DIR = $(SKYBUILD_DIR)/libskycoin
LIBC_DIR      = $(SKYLIBC_DIR)/lib/cgo
LIBSWIG_DIR   = swig
BUILD_DIR     = build
DIST_DIR      = dist
BIN_DIR       = $(SKYLIBC_DIR)/bin
INCLUDE_DIR   = $(SKYLIBC_DIR)/include
FULL_PATH_LIB = $(REPO_ROOT)/$(BUILDLIBC_DIR)

LIB_FILES = $(shell find $(SKYLIBC_DIR)/lib/cgo -type f -name "*.go")
SRC_FILES = $(shell find $(SKYCOIN_DIR)/src -type f -name "*.go")
SWIG_FILES = $(shell find $(LIBSWIG_DIR) -type f -name "*.i")
HEADER_FILES = $(shell find $(INCLUDE_DIR) -type f -name "*.h")

ifeq ($(shell uname -s),Linux)
	TEMP_DIR = tmp
else ifeq ($(shell uname -s),Darwin)
	TEMP_DIR = $TMPDIR
endif

configure: ## Configure build environment
	mkdir -p $(BUILD_DIR)/usr/tmp $(BUILD_DIR)/usr/lib $(BUILD_DIR)/usr/include
	mkdir -p $(BUILDLIBC_DIR) $(BIN_DIR) $(INCLUDE_DIR)
	mkdir -p $(DIST_DIR)

$(BUILDLIBC_DIR)/libskycoin.a: $(LIB_FILES) $(SRC_FILES) $(HEADER_FILES)
	rm -f $(BUILDLIBC_DIR)/libskycoin.a
	GOPATH="$(REPO_ROOT)/$(GOPATH_DIR)" make -C $(SKYLIBC_DIR) build-libc
	ls $(BUILDLIBC_DIR)
	rm -f swig/include/libskycoin.h
	mkdir -p swig/include
	grep -v _Complex $(INCLUDE_DIR)/libskycoin.h > swig/include/libskycoin.h

build-libc: configure $(BUILDLIBC_DIR)/libskycoin.a ## Build libskycoin C client library

build-swig: ## Generate Python C module from SWIG interfaces
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
	rm -f swig/include/swig.h
	swig -python -w501,505,401,302,509,451 -Iswig/include -I$(INCLUDE_DIR) -outdir ./skycoin/ -o swig/pyskycoin_wrap.c $(LIBSWIG_DIR)/pyskycoin.i

develop: ## Install PySkycoin for development
	$(PYTHON_BIN) setup.py develop

build-libc-swig: build-libc build-swig

build: build-libc-swig ## Build PySkycoin Python package
	$(PYTHON_BIN) setup.py build

test-ci: build-libc build-swig develop ## Run tests on (Travis) CI build
	tox

test: build-libc build-swig develop ## Run project test suite
	$(PYTHON_BIN) setup.py test

sdist: ## Create source distribution archive
	$(PYTHON_BIN) setup.py sdist --formats=gztar

bdist_wheel: ## Create architecture-specific binary wheel distribution archive
	$(PYTHON_BIN) setup.py bdist_wheel

# FIXME: After libskycoin 32-bits binaries add bdist_manylinux_i686
bdist_manylinux: bdist_manylinux_amd64 ## Create multilinux binary wheel distribution archives

bdist_manylinux_amd64: ## Create 64 bits multilinux binary wheel distribution archives
	docker pull quay.io/pypa/manylinux1_x86_64
	docker run --rm -t -v $(REPO_ROOT):/io quay.io/pypa/manylinux1_x86_64 /io/.travis/build_wheels.sh
	ls wheelhouse/
	cp -v wheelhouse/* $(DIST_DIR)

bdist_manylinux_i686: ## Create 32 bits multilinux binary wheel distribution archives
	docker pull quay.io/pypa/manylinux1_i686
	docker run --rm -t -v $(REPO_ROOT):/io quay.io/pypa/manylinux1_i686 linux32 /io/.travis/build_wheels.sh
	ls wheelhouse/
	cp -v wheelhouse/* $(DIST_DIR)

dist: sdist bdist_wheel bdist_manylinux_amd64 ## Create distribution archives

check-dist: dist ## Perform self-tests upon distributions archives
	docker run --rm -t -v $(REPO_ROOT):/io quay.io/pypa/manylinux1_i686 linux32 /io/.travis/check_wheels.sh

format: ## Format code that autopep8
	autopep8 --in-place --aggressive --aggressive --aggressive --aggressive ./tests/*.py

lint: ## Linter to pylint
	pylint -E tests/*.py
	yamllint -d relaxed .travis.yml

help: ## List available commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
