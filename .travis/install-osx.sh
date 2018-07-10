#!/bin/bash

set -ev

# Install some dependencies
brew update;
brew outdated pyenv || brew upgrade pyenv;
brew install pyenv-virtualenv
brew install swig;
brew install gimme;

# Install Python
pyenv install $PYTHON
pyenv install 2.7.14
pyenv global $PYTHON 2.7.14
pyenv versions
pyenv which python${PYTHOB}

# Temp vars
export PYCMDVERSION="$(echo $PYTHON | cut -d . -f 1,2)"
export PYENVBINPATH="$(pyenv which python${PYCMDVERSION})"

export PATH="$( dirname ${PYENVBINPATH} ):/Users/travis/.pyenv/shims:${PATH}"
echo "PATH=$PATH"

# Define command aliases
eval "alias python$PYCMDVERSION=$(pyenv which python$PYCMDVERSION)"
eval "alias python2.7=$(pyenv which python2.7)"

# Prepare and initialize pyenv environment
eval "$(pyenv init -)";
eval "$(pyenv virtualenv-init -)";
pyenv rehash
python -m pip install --upgrade pip setuptools wheel tox tox-pyenv

# Create and activate python virtual environment
#pyenv virtualenv $PYTHON venv;
#pyenv activate venv;
