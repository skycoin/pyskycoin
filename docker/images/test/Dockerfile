ARG ARCH_OS
# FROM balenalib/armv7hf-debian-golang
FROM balenalib/${ARCH_OS}-debian-python

ENV REPO_ROOT=$GOPATH/src/github.com/skycoin/pyskycoin/
ADD . ${REPO_ROOT}

ARG PIP_PACKAGES="setuptools wheel tox pytest"

RUN [ "cross-build-start" ]

# Install packages in PIP_PACKAGES
RUN pip install --upgrade $PIP_PACKAGES

RUN pip install -i https://test.pypi.org/simple/ pyskycoin==0.25.1.dev0

RUN cd $REPO_ROOT && python -m tox

RUN [ "cross-build-end" ]  

WORKDIR $GOPATH/src/github.com/skycoin

VOLUME $GOPATH/src/
