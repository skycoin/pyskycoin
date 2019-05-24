# Creates an image for skycoin development with Python tools installed
ARG IMAGE_FROM=skycoin/skycoindev-cli:develop
FROM $IMAGE_FROM

ARG BDATE
ARG SCOMMIT
ARG PIP_PACKAGES="pip setuptools wheel"

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
		ca-certificates \
		libexpat1 \
		libffi6 \
		libgdbm3 \
		libreadline7 \
		libsqlite3-0 \
		libssl1.1 \
		netbase \
		wget \
		make \
		build-essential \
		libssl1.0-dev \
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
        git \
        && git clone git://github.com/yyuu/pyenv.git ~/.pyenv \
        && rm -rf ~/.pyenv/plugins/pyenv-virtualenv \
        && git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv

ENV HOME  /root
ENV PROJECT_ROOT /source
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

RUN echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc \
    && echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc \
    && echo 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc \
    && bash \
    && git clone https://github.com/skycoin/pyskycoin.git $PROJECT_ROOT/pyskycoin \
    && cd $PROJECT_ROOT/pyskycoin \
    && git checkout v0.25.0 \
    && git submodule update --init --recursive \
    && echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc \
    && bash -c "eval "$(pyenv virtualenv-init -)"" \
    && pyenv install 2.7.10 \
    && pyenv install 3.4.9 \
    && pyenv install 3.5.7 \
    && pyenv install 3.6.7 \
    && pyenv install 3.7.1 \
    && pyenv virtualenv 2.7.10 pysky27 \
    && pyenv virtualenv 3.4.9 pysky34 \
    && pyenv virtualenv 3.5.7 pysky35 \
    && pyenv virtualenv 3.6.7 pysky36 \
    && pyenv virtualenv 3.7.1 pysky37 \
    && . $PYENV_ROOT/versions/pysky27/bin/activate && pip install --upgrade $PIP_PACKAGES && pip install pyskycoin && deactivate \
    && . $PYENV_ROOT/versions/pysky34/bin/activate && pip install --upgrade $PIP_PACKAGES && pip install pyskycoin && deactivate \
    && . $PYENV_ROOT/versions/pysky35/bin/activate && pip install --upgrade $PIP_PACKAGES && pip install pyskycoin && deactivate \
    && . $PYENV_ROOT/versions/pysky36/bin/activate && pip install --upgrade $PIP_PACKAGES && pip install pyskycoin && deactivate \
    && . $PYENV_ROOT/versions/pysky37/bin/activate && pip install --upgrade $PIP_PACKAGES && pip install pyskycoin && deactivate

WORKDIR $GOPATH/src/github.com/skycoin

VOLUME $GOPATH/src/
