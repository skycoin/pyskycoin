#!/bin/bash

set -ev

# Repository root path
REPO_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )/.."
echo "Install Linux packages from $REPO_ROOT"

# Install gimme
curl -sL -o ~/bin/gimme https://raw.githubusercontent.com/travis-ci/gimme/master/gimme
chmod +x ~/bin/gimme

#Install Python libraries
python -m pip install --upgrade pip setuptools tox-travis
python -m pip install -r "$REPO_ROOT/requirements.dev.txt"

# Compile SWIG
mkdir swig_build && \
  cd swig_build && \
  wget http://prdownloads.sourceforge.net/swig/swig-3.0.12.tar.gz && \
  tar -zxf swig-3.0.12.tar.gz && \
  cd swig-3.0.12 && \
  sudo ./configure --prefix=/usr && \
  sudo make && \
  sudo make install && \
  cd ../../ && \
  sudo rm -rf swig_build

