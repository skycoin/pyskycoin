# Creates an image for skycoin development
FROM skycoin/skycoindev-cli:develop

# Install python software

RUN set -ex; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
    python2.7-dev \
    python-pip \
    tox ;\
    apt-get clean; \
    pip install --upgrade pip
