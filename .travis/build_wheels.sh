#!/bin/bash
set -e -x

export CGO_ENABLE=1
# Install system packages required by our library
yum install -y sudo pcre pcre-devel
mkdir -p "$HOME/bin"
PIP=/opt/python/cp27-cp27m/bin/pip source /io/.travis/install-linux.sh
eval "$(gimme 1.10)"

# Compile wheels
for PYBIN in /opt/python/*/bin; do
  "${PYBIN}/pip" install -r /io/requirements.dev.txt
  "${PYBIN}/pip" wheel /io/ -w wheelhouse/
done

# Bundle external shared libraries into the wheels
for whl in wheelhouse/*.whl; do
  auditwheel repair "$whl" -w /io/wheelhouse/
done

