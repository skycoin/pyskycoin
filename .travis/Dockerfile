# Creates an image for skycoin development with Python tools installed
ARG IMAGE_FROM=balenalib/armv7hf-ubuntu-golang:latest-xenial-build
FROM $IMAGE_FROM

ARG BDATE
ARG SCOMMIT
ARG PIP_PACKAGES="setuptools wheel"

# Image labels (see ./hooks/build for ARGS)
LABEL "org.label-schema.name"="skycoindev-python" \
      "org.label-schema.description"="Docker image with go, node, python and dev tools for Skycoin developers" \
      "org.label-schema.vendor"="Skycoin project" \
      "org.label-schema.url"="skycoin.net" \
      "org.label-schema.version"="0.24.4" \
      "org.label-schema.build-date"=$BDATE \
      "org.label-schema.vcs-url"="https://github.com/skycoin/pyskycoin.git" \
      "org.label-schema.vcs-ref"=$SCOMMIT \
      "org.label-schema.usage"="https://github.com/skycoin/pyskycoin/blob/"$SCOMMIT"/docker/images/dev/README.md" \
      "org.label-schema.schema-version"="1.0" \
      "org.label-schema.docker.cmd"="mkdir src; docker run --rm -v ${PWD}/src:/usr/local/src skycoin/skycoindev-python:develop git clone https://github.com/simelo/pyskycoin.git"

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


WORKDIR $GOPATH/src/github.com/skycoin

VOLUME $GOPATH/src/
