#!/bin/bash

set -ev

# Install some dependencies
brew update;
brew outdated pyenv || brew upgrade pyenv;
brew install pyenv-virtualenv
echo 'Creating swig@3.0.12 formula';
cd "$(brew --repository)/Library/Taps/homebrew/homebrew-core";
git show 42d31bba7772fb01f9ba442d9ee98b33a6e7a055:Formula/swig.rb | grep -v 'fails_with' > Formula/swig.rb;
echo 'Installing swig@3.0.12 (3.0.12)';
brew install swig || brew link --overwrite swig;
# brew install gimme;

# Install Python
# pyenv install ${PYTHON}
# pyenv global ${PYTHON}

# Prepare and initialize pyenv environment
# eval "$(pyenv init -)";
# eval "$(pyenv virtualenv-init -)";
# pyenv rehash

# Setup environment and PATH in MacOS
# export PYCMD_VERSION="$(echo ${PYTHON} | cut -d . -f 1,2)"
# export PYCMD_PATH="$(pyenv which python${PYCMD_VERSION})"
# export PYCMD_DIRPATH="$( dirname ${PYCMD_PATH} )"
# export PATH="${PYCMD_DIRPATH}:/Users/travis/.pyenv/shims:${PATH}"

# eval "python${PYCMD_VERSION} -m pip install --upgrade pip setuptools wheel tox tox-pyenv pytest pytest-runner"

# Install by BREW

echo 'Creating python formula';
cd "$(brew --repository)/Library/Taps/homebrew/homebrew-core";
echo 'Installing python';

if [[ "$TOXENV" == 'py34' ]]; then
    git show bd43f59bd50bb49242259f327cb6ac7a8dd59478:Formula/python3.rb | grep -v 'fails_with' > Formula/python.rb;
    brew install python || brew link --overwrite python;
fi

if [[ "$TOXENV" == 'py35' ]]; then
    git show ec545d45d4512ace3570782283df4ecda6bb0044:Formula/python3.rb | grep -v 'fails_with' > Formula/python.rb;
    brew install python || brew link --overwrite python;
fi

if [[ "$TOXENV" == 'py36' ]]; then
    git show f2a764ef944b1080be64bd88dca9a1d80130c558:Formula/python3.rb | grep -v 'fails_with' > Formula/python.rb;
    brew install python || brew link --overwrite python;
fi

if [[ "$TOXENV" == 'py37' ]]; then
    git show 42d31bba7772fb01f9ba442d9ee98b33a6e7a055:Formula/python3.rb | grep -v 'fails_with' > Formula/python.rb;
    brew install python || brew link --overwrite python;
fi

python -m pip install --upgrade pip setuptools wheel tox tox-pyenv pytest pytest-runner

