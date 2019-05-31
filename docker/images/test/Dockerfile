ARG ARCH_OS
FROM balenalib/${ARCH_OS}-debian-python

ADD . $GOPATH/src/github.com/skycoin/pyskycoin/
ARG PIP_PACKAGES="setuptools wheel tox pytest"

# Install packages in PIP_PACKAGES
RUN pip install --upgrade $PIP_PACKAGES \

RUN pip install -i https://test.pypi.org/simple/ pyskycoin==0.25.1.dev0

RUN cd $GOPATH/src/github.com/skycoin/pyskycoin && python -m tox

WORKDIR $GOPATH/src/github.com/skycoin

VOLUME $GOPATH/src/
