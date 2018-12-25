#!/bin/bash

set -ev

# Install gimme
curl -sL -o ~/bin/gimme https://raw.githubusercontent.com/travis-ci/gimme/master/gimme
chmod +x ~/bin/gimme

#Install Python libraries
python -m pip install --upgrade pip setuptools wheel tox tox-travis tox-pyenv pytest pytest-runner

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

