ARG ARCH_OS
# FROM balenalib/armv7hf-debian-golang
FROM balenalib/${ARCH_OS}-debian-golang

ADD . $GOPATH/src/github.com/skycoin/pyskycoin/
ARG PIP_PACKAGES="setuptools wheel tox pytest"

# Install Python 2/3 runtime and development tools
RUN apt update
RUN apt install python3 python python3-pip python-pip -y

# Install packages in PIP_PACKAGES
RUN pip install --upgrade $PIP_PACKAGES \
    && pip3 install --upgrade $PIP_PACKAGES 

RUN pip install -i https://test.pypi.org/simple/ pyskycoin==0.25.1.dev0
RUN pip3 install -i https://test.pypi.org/simple/ pyskycoin==0.25.1.dev0

RUN cd $GOPATH/src/github.com/skycoin/pyskycoin && python -m tox

WORKDIR $GOPATH/src/github.com/skycoin

VOLUME $GOPATH/src/
