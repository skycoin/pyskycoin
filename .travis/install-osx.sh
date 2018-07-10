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

# Temp vars
export PYCMD_VERSION="$(echo ${PYTHON} | cut -d . -f 1,2)"
export PYCMD_PATH="$(pyenv which python${PYCMD_VERSION})"
export PYCMD_DIRPATH="$( dirname ${PYCMD_PATH} )"

pyenv versions
pyenv which python${PYCMD_VERSION}

export PATH="${PYCMD_DIRPATH}:/Users/travis/.pyenv/shims:${PATH}"
echo "PATH=$PATH"

# Define command aliases
eval "alias python${PYCMD_VERSION}=$(pyenv which python${PYCMD_VERSION})"
eval "alias python2.7=$(pyenv which python2.7)"

# Prepare and initialize pyenv environment
eval "$(pyenv init -)";
eval "$(pyenv virtualenv-init -)";
pyenv rehash
python -m pip install --upgrade pip setuptools wheel tox tox-pyenv

# Create and activate python virtual environment
#pyenv virtualenv $PYTHON venv;
#pyenv activate venv;
