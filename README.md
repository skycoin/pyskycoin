# PySkycoin

[![Build Status](https://travis-ci.org/skycoin/pyskycoin.svg?branch=develop)](https://travis-ci.org/skycoin/pyskycoin)

Python extension for Skycoin API.
A Python extension generated with SWIG to access Skycoin API from Python.

## Table of Contents

<!-- MarkdownTOC levels="1,2,3,4,5" autolink="true" bracket="round" -->
- [Installation](#installation)
- [Using the API](#usage)
  - [Naming](#naming)
  - [Parameters](#parameters)
    - [Handles](#handles)
    - [Byte Slices](#byte-slices)
    - [Structures](#structures)
    - [Fixed Size Arrays](#fixed-size-array)
    - [Other Slices](#other-slices)
    - [Memory Managemanet](#memory-management)
- [Make rules](#make-rules)
- [Development setup](#development-setup)
  - [Running tests](#running-tests)
  - [Releases](#releases)
    - [Update the version](#update-the-version)
    - [Pre-release testing](#pre-release-testing)
    - [Creating release builds](#creating-release-builds)
<!-- /MarkdownTOC -->

## Installation

Download the repository from http://github.com/simelo/pyskycoin.git. 
Execute (`python setup.py install`) to install the library. Although executing (python setup.py develop) is a better choice for making changes to the library. However, when using tox these commands are not required at all because calling tox will make any necessary installation and execute the tests.

## Usage
### Naming

The exported function in PySkycoin have the following naming format: `SKY_package_func_name` where package is replace by the package where the original Skycoin function is and func_name is the name of the function. For example, `LoadConfig` function from `cli` package is called in Python `SKY_cli_LoadConfig`
### Parameters

All skycoin exported functions return an error object as the last of the return parameters. In Pyskycoin error is return as an integer and it is the first return parameter. The rest of the parameters are returned in the same order.

Receivers in Skycoin are the first of the input parameters. Simple types, like integer, float, string will be used as the corresponding types in Python.

#### Handles

Some of Skycoin types are too complex to be exported to a scripting language. So, handles are used instead. Therefore all functions taking a complex type will receive a handle instead of the original Skycoin type. For example, having these functions exported from Skycoin:

```go
	func LoadConfig() (Config, error)
	func (c Config) FullWalletPath() string
```


Config is a struct type that is treated as a handle in Pyskycoin. The usage in Python will be:

```python

import skycoin
	
def main:
	err, configHandle = skycoin.SKY_cli_LoadConfig()
	if err == skycoin.SKY_OK:  # 0 then no error
		fullWalletPath = skycoin.SKY_cli_FullWalletPath(configHandle)
		print fullWallerPath
		#Close the handle after using the it
		#so the garbage collector can delete the object associated with it. 
		skycoin.SKY_handle_close( configHandle )
	else: 
		#Error
		print err
```

#### Byte slices

Parameters of type byte[] will treated as string . Example, this function in Skycoin:

```go
func (s ScryptChacha20poly1305) Encrypt(data, password []byte) ([]byte, error)
```

Will be called like this:

```python
encrypt_settings = skycoin.encrypt__ScryptChacha20poly1305()
data = "Data to encrypt" #It will be passed as a parameter of type []byte
pwd = "password"         #As []byte too
err, encrypted = skycoin.SKY_encrypt_ScryptChacha20poly1305_Encrypt(encrypt_settings, data, pwd)
if err == skycoin.SKY_OK:
	print encrypted #Encrypted is string
```

#### Structures

Structures that are not exported as handles are treated like classes in Python. In the previous example type ScryptChacha20poly1305 is created in Python like:

```python
encrypt_settings = skycoin.encrypt__ScryptChacha20poly1305()
```

And passed as first parameter in call to SKY_encrypt_ScryptChacha20poly1305_Encrypt.

#### Fixed Sized Arrays

Parameters of fixed size array are wrapped in structures when called from python.

Given these types in Skycoin:

```go
	type PubKey [33]byte
	type SecKey [32]byte
```

And this exported function:

```go
	func GenerateDeterministicKeyPair(seed []byte) (PubKey, SecKey)
```
	
This is how it is used in Python:

```python
#Generates random seed
err, data = skycoin.SKY_cipher_RandByte(32)
assert err == error["SKY_OK"]
pubkey = skycoin.cipher_PubKey()
seckey = skycoin.cipher_SecKey()
err = skycoin.SKY_cipher_GenerateDeterministicKeyPair(data, pubkey, seckey)
```

pubkey and seckey are objects of type structure containing a field name data for the corresponding type of PubKey and SecKey. Something like:

```cpp
	cipher_PubKey struct{
		data [33]byte;
	} cipher_PubKey;

	cipher_SecKey struct{
		data [32]byte;
	} ;
```

#### Other Slices

Other slices of type different than byte were wrapped inside classes. Calling the following function:

```go
func GenerateDeterministicKeyPairs(seed []byte, n int) []SecKey
```
	
Would be like:

```python
#Generates random seed
err, seed = skycoin.SKY_cipher_RandByte(32)
err, seckeys = skycoin.SKY_cipher_GenerateDeterministicKeyPairs(seed, 2)
for seckey in seckeys:
	pubkey = skycoin.cipher_PubKey()
	skycoin.SKY_cipher_PubKeyFromSecKey(seckey, pubkey)
	err = skycoin.SKY_cipher_PubKey_Verify(pubkey)
	assert err == error["SKY_OK"]
```

### Memory Management

Memory management is transparent to the user. Any object allocated inside the library is left to be managed by Python garbage collector.

## Make Rules

All these make rules require skycoin to be a git submodule of pyskycoin

- build-libc
  * Compiles skycoin C language library.
- build-swig
  * Creates the wrapper C code to generate the Python library.
- develop
  * Install a developer version of the module.	
- test
  * Compiles skycoin C language library, creates the wrapper and execute Tox. Tox installs compiles the Python library and executes the tests.	

## Development setup

It is highly recommended for developers to setup their environment using
the available Docker images.
Read the [PySkycoin Docker docs](docker/images/dev-cli/README.md) for further
details.

The project has two branches: `master` and `develop`.

- `develop` is the default branch and will always have the latest code.
  The submodule at `gopath/src/github.com/skycoin/skycoin` has to be
  in sync with `skycoin/skycoin` `develop` branch.
- `master` will always be equal to the current stable release on the website, and should correspond with the latest release tag.
  The submodule at `gopath/src/github.com/skycoin/skycoin` has to be
  in sync with `skycoin/skycoin` `master` branch.

Separate stable development branches will be created to work on releases for supporting the
most recent stable version of Skycoin. The name of these branches should be the Skycoin
imajor and minor version numbers followed by `dev` suffix e.g. `0.25dev`.
These branches may be forked out of either `master` or `develop` branches, and 
the submodule at `gopath/src/github.com/skycoin/skycoin` has to be
in sync with the corresponding tag of `skycoin/skycoin` official repository.

Stable development branches are created most of the time for the following reasons:

- A Skycoin release increasing [patch version number](https://semver.org/).
- Enhanced support and bug fixes for a version of PySkycoin compiled against an
  stable version of Skycoin
- Backporting useful features added in `develop`.

### Running tests

```sh
$ make test
```

### Releases

#### Update the version

0. If the `master` branch has commits that are not in `develop` (e.g. due to a hotfix applied to `master`), merge `master` into `develop` (and fix any build or test failures)
0. Switch to a new release branch named `release-X.Y.Z` for preparing the release.
0. Ensure that the submodule at `gopath/src/github.com/skycoin/skycoin` is in sync with respect to the corresponding tag in https://github.com/skycoin/skycoin repository.
0. Update `__version__` in `skycoin/__init__.py`
0. Run `make build` to make sure that the code base is up to date
0. Update `CHANGELOG.md`: move the "unreleased" changes to the version and add the date.
0. Update files in https://github.com/skycoin/repo-info/tree/master/repos/skycoin/remote for `skycoin/skycoin-python` Docker image, adding a new file for the new version and adjusting any configuration text that may have changed
0. Follow the steps in [pre-release testing](#pre-release-testing)
0. Make a PR merging the release branch into `master`
0. Review the PR and merge it
0. Tag the `master` branch with the version number. Version tags start with `v`, e.g. `v0.20.0`. Sign the tag. If you have your GPG key in github, creating a release on the Github website will automatically tag the release. It can be tagged from the command line with `git tag -as v0.20.0 $COMMIT_ID`, but Github will not recognize it as a "release".
0. Release builds are created and uploaded by travis. To do it manually, checkout the master branch and follow the [create release builds instructions](#creating-release-builds).
0. Checkout `develop` branch and bump `__version__` to next [`dev` version number](https://www.python.org/dev/peps/pep-0440/#developmental-releases).

#### Pre-release testing

Perform these actions before releasing:

```sh
make check
make integration-test
```

#### Creating release builds

Release builds should be created from `master` branch . After [updating release version](#update-the-version) it is necessary to follow these steps

```sh
cd /path/to/pyskycoin
python3 setup.py sdist bdist_wheel
python3 -m pip install --user --upgrade twine
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

