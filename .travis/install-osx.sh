#!/bin/bash

set -ev

# Install some dependencies
brew update;
brew outdated pyenv || brew upgrade pyenv;
brew install pyenv-virtualenv
brew install swig@3.04 || brew link --force swig@3.04;
echo 'export PATH="/usr/local/opt/swig@3.04/bin:$PATH"' >> ~/.bash_profile;
ls -oa /usr/local/opt/swig@3.04/bin;
source ~/.bash_profile;
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

