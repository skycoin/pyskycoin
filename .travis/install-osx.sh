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

eval 'alias python$(echo $PYTHON | cut -d . -f 1,2)=$(pyenv which python3)'
eval 'alias python2.7=$(pyenv which python2.7)'

python3.4 --help
# Prepare and initialize pyenv environment
PYENVPATH="$(dirname "$(pyrenv which python${PYTHON})")" export PATH="$(dirname "$PYENVPATH"):/Users/travis/.pyenv/shims:${PATH}"
echo "PATH=$PATH"
eval "$(pyenv init -)";
eval "$(pyenv virtualenv-init -)";
pyenv rehash
python -m pip install --upgrade pip setuptools wheel tox tox-pyenv

# Create and activate python virtual environment
#pyenv virtualenv $PYTHON venv;
#pyenv activate venv;
