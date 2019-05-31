ARG ARCH_OS
FROM balenalib/${ARCH_OS}-debian-golang

ENV REPO_ROOT=$GOPATH/src/github.com/skycoin/pyskycoin/
ADD . ${REPO_ROOT}
ENV TOXENV=py27
ENV PIP='python -m pip'
#Install package
RUN apt-get update
RUN apt-get install make cmake python-pip gcc -y

# Install packages in PIP_PACKAGES
RUN ${PIP} install --upgrade pip setuptools tox-travis
RUN ${PIP} install -r "${REPO_ROOT}/requirements.dev.txt"
RUN ${PIP} install -r "${REPO_ROOT}/lib/skyapi/requirements.txt"
RUN ${PIP} install -r "${REPO_ROOT}/lib/skyapi/test-requirements.txt"

RUN pip install -i https://test.pypi.org/simple/ pyskycoin==0.25.1.dev0

RUN cd ${REPO_ROOT} && python -m tox
