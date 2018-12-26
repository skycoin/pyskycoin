#!/bin/bash

set -ev

# Install some dependencies
brew update;
brew outdated pyenv || brew upgrade pyenv;
brew install pyenv-virtualenv
brew install swig;
brew install gimme;

# Install Python
pyenv install ${PYTHON}
pyenv install 2.7.14
pyenv global ${PYTHON} 2.7.14

# Prepare and initialize pyenv environment
eval "$(pyenv init -)";
eval "$(pyenv virtualenv-init -)";
pyenv rehash

# Setup environment and PATH in MacOS
export PYCMD_VERSION="$(echo ${PYTHON} | cut -d . -f 1,2)"
export PYCMD_PATH="$(pyenv which python${PYCMD_VERSION})"
export PYCMD_DIRPATH="$( dirname ${PYCMD_PATH} )"
export PATH="${PYCMD_DIRPATH}:/Users/travis/.pyenv/shims:${PATH}"

eval "python${PYCMD_VERSION} -m pip install --upgrade pip setuptools wheel tox tox-pyenv pytest pytest-runner"

