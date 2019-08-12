#!/bin/bash
set -e -x

# Install system packages required by our library
yum install -y sudo pcre pcre-devel
mkdir -p "$HOME/bin"
PIP=/opt/python/cp27-cp27m/bin/pip source /io/.travis/install-linux.sh
eval "$(gimme 1.10)"

# Install golang
curl -sL -o "go1.11.3.linux-$1.tar.gz" https://storage.googleapis.com/golang/go1.11.3.linux-$1.tar.gz
sudo tar -zxf go1.11.3.linux-$1.tar.gz -C /usr/local
echo 'export GOROOT=/usr/local/go' | sudo tee -a /etc/profile
echo 'export PATH=$PATH:/usr/local/go/bin' | sudo tee -a /etc/profile
echo 'export CGO_ENABLE=1' | sudo tee -a /etc/profile
source /etc/profile
go version
go env

# Compile wheels
for PYBIN in /opt/python/*/bin; do
  "${PYBIN}/pip" install -r /io/lib/skyapi/requirements.txt
  "${PYBIN}/pip" wheel /io/lib/skyapi/ -w wheelhouse/
done

# Bundle external shared libraries into the wheels
for whl in wheelhouse/*.whl; do
  auditwheel repair "$whl" -w /io/wheelhouse/
done

