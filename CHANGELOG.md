# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## PySkycoin 0.25.0 - 2019/01/01

### Added

- Feature compatible with Skycoin `v0.25.0`
- Add `make build` target to build PySkycoin C extension module
- Add `make help`
- Add Python-specific SWIG interface files
- Add `skycoin/skycoindev-python:develop` Docker image including Python `3.4`, `3.5`, `3.6`, and `3.7`

### Fixed

- Fix #73 - Wrong number or type of arguments for overloaded function `SKY_cipher_GenerateDeterministicKeyPairs`

### Changed

- Generate error codes from SWIG interfaces
- Define PySkycoin __version__ in a single place

## PySkycoin 0.24.6 - 2018/08/06

### Added

- Feature compatible with Skycoin `v0.24.1`
- PySkycoin usage explained in README.md
- Error code constants
- Implement functions receiving pointer to functions or GoSlices of type different than byte

### Fixed

- Fix #54 - Fix pip installation issue

## PySkycoin 0.24.1 - 2018/07/23

### Added

- Install from source with `make install`
- Implement `libskycoin` handles in Pyskycoin using SWIG typemaps
- Add comparison methods for cipher structure
- Treat as lists the functions parameters being go slices of type other than byte

### Fixed

- Fix #28 - Fix libskycoin C build using `make build-libc-static`
- Fix #30 - Fix random error in `SKY_cipher_GenerateDeterministicKeyPairs`
- Fix #38 - Pyskycoin compilation should reflect changes in skycoin header file

## PySkycoin 0.24 - 2018/06/23

### Added

- Feature compatible with Skycoin `v0.24.0`
- Initial source code base with generated C code for Skycoin Python extension module
- Feature compatible with Skycoin `v0.24.1`

### Known issues

- The file swig.h has to be copied at build time from `skycoin/skycoin` submodule due to bizarre error

