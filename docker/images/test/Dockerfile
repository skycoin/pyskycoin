ARG ARCH_OS
FROM balenalib/${ARCH_OS}-debian-golang

ENV REPO_ROOT=$GOPATH/src/github.com/skycoin/pyskycoin/
ADD . ${REPO_ROOT}
ARG PIP_PACKAGES="setuptools wheel tox pytest"
ENV TOXENV=py27
#Install package
RUN apt-get update
RUN apt-get install make cmake python-pip gcc -y

# Install packages in PIP_PACKAGES
RUN pip install --upgrade $PIP_PACKAGES

RUN pip install -i https://test.pypi.org/simple/ pyskycoin==0.25.1.dev0

RUN cd ${REPO_ROOT} && python -m tox
