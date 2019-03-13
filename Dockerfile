FROM balenalib/armv7hf-ubuntu-golang

ADD . $GOPATH/src/github.com/skycoin/pyskycoin/
ARG PIP_PACKAGES="setuptools wheel"

RUN [ "cross-build-start" ]

RUN go get github.com/gz-c/gox
ENV CGO_ENABLED=1

# Install Python 2/3 runtime and development tools
RUN apt update
RUN apt install python3 python python3-pip python-pip -y

# Install packages in PIP_PACKAGES
RUN pip install --upgrade $PIP_PACKAGES \
    && pip3 install --upgrade $PIP_PACKAGES 

RUN cd $GOPATH/src/github.com/skycoin/pyskycoin && make test

RUN [ "cross-build-end" ]  

WORKDIR $GOPATH/src/github.com/skycoin

VOLUME $GOPATH/src/
