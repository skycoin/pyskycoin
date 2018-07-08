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

# Prepare and initialize pyenv environment
export PYENV_VERSION=$PYTHON
export PATH="/Users/travis/.pyenv/shims:${PATH}"
eval "$(pyenv init -)";
eval "$(pyenv virtualenv-init -)";
pyenv rehash
python -m pip install --upgrade pip setuptools wheel

# Create and activate python virtual environment
#pyenv virtualenv $PYTHON venv;
#pyenv activate venv;
