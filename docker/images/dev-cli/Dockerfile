# Creates an image for skycoin development with Python tools installed
ARG IMAGE_FROM=skycoin/skycoindev-cli:develop
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
		make \
		build-essential \
		libssl-dev \
		zlib1g-dev \
		libbz2-dev \
        libreadline-dev \
        libsqlite3-dev \
        wget \
        curl \
        llvm \
        libncurses5-dev \
        libncursesw5-dev \
        xz-utils \
        tk-dev \
        libffi-dev \
        liblzma-dev \
        python-openssl \
        git \
    && git clone https://github.com/pyenv/pyenv.git ~/.pyenv \
    && echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc \
    && echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc \
    && echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc \
    && bash \
    && git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv \
    && echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc \
    && bash \
    && pyenv install 2.7.10 \
#    && pyenv install 3.4.9 \
#    && pyenv install 3.6.7 \
#    && pyenv install 3.7.1 \
    && pyenv virtualenv 2.7.10 pysky27 \
#    && pyenv virtualenv 3.4.9 pysky34 \
#    && pyenv virtualenv 3.6.7 pysky36 \
#    && pyenv virtualenv 3.7.1 pysky37 \
    && pyenv activate pysky27 && pip install --upgrade $PIP_PACKAGES && pip install pyskycoin && pyenv deactivate
#    && pyenv activate pysky34 && pip install --upgrade $PIP_PACKAGES && pip install  pyskycoin && pyenv deactivate \
#    && pyenv activate pysky36 && pip install --upgrade $PIP_PACKAGES && pip install pyskycoin && pyenv deactivate \
#    && pyenv activate pysky37 && pip install --upgrade $PIP_PACKAGES && pip install pyskycoin

WORKDIR $GOPATH/src/github.com/skycoin

VOLUME $GOPATH/src/
