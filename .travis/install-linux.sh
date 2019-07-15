#!/bin/bash

set -ev

# Environment checks
if [ "$PIP" == "" ]; then
  export PIP='python -m pip'
fi

# Repository root path
REPO_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )/.."
echo "Install Linux packages from $REPO_ROOT"

# Install gimme
curl -sL -o "$HOME/bin/gimme" https://raw.githubusercontent.com/travis-ci/gimme/master/gimme
chmod +x "$HOME/bin/gimme"

# Install Python libraries
$PIP install --upgrade pip setuptools tox-travis 
$PIP install -r "$REPO_ROOT/requirements.dev.txt"
$PIP install -r "$REPO_ROOT/lib/skyapi/requirements.txt"
$PIP install -r "$REPO_ROOT/lib/skyapi/test-requirements.txt"

# Compile SWIG
mkdir swig_build && \
  cd swig_build && \
  curl -sL -o "swig-3.0.12.tar.gz" http://prdownloads.sourceforge.net/swig/swig-3.0.12.tar.gz && \
  tar -zxf swig-3.0.12.tar.gz && \
  cd swig-3.0.12 && \
  sudo ./configure --prefix=/usr && \
  sudo make && \
  sudo make install && \
  cd ../../ && \
  sudo rm -rf swig_build
