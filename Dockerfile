FROM balenalib/armv7hf-debian-golang

ADD . $GOPATH/src/github.com/skycoin/pyskycoin/
ARG PIP_PACKAGES="setuptools wheel"

RUN [ "cross-build-start" ]

RUN go get github.com/gz-c/gox
ENV CGO_ENABLED=1

# Install Python 2.7/3.5 runtime and development tools
RUN set -ex \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
    python2.7-dev \
    python3.5 \
    python3.5-dev \
    python-dev \
    python3-dev \
    ca-certificates \
    libexpat1 \
    libffi6 \
    libgdbm3 \
    libreadline7 \
    libsqlite3-0 \
    libssl1.1 \
    netbase \
    wget \
    python-pip \
    python3-pip \
    && pip install --upgrade pip \
    && pip3 install --upgrade pip

# Install packages in PIP_PACKAGES
RUN pip install --upgrade $PIP_PACKAGES \
    && pip3 install --upgrade $PIP_PACKAGES \

RUN cd $GOPATH/src/github.com/skycoin/pyskycoin && make test

RUN [ "cross-build-end" ]  

WORKDIR $GOPATH/src/github.com/skycoin

VOLUME $GOPATH/src/
