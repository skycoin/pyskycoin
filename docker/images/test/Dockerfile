ARG IMAGE
FROM ${IMAGE}

ENV REPO_ROOT=$GOPATH/src/github.com/skycoin/pyskycoin/
ADD . ${REPO_ROOT}
ENV PIP='python3 -m pip'
#Install package
RUN apt-get update
RUN apt-get install make cmake python-pip python3-dev python-dev python-setuptools libpcre3-dev curl gcc -y

# Install packages in PIP_PACKAGES
RUN ${PIP} install --upgrade tox pip setuptools
RUN ${PIP} install -r "${REPO_ROOT}/requirements.dev.txt"
RUN ${PIP} install -r "${REPO_ROOT}/lib/skyapi/requirements.txt"
RUN ${PIP} install -r "${REPO_ROOT}/lib/skyapi/test-requirements.txt"

RUN ${PIP} -i https://test.pypi.org/simple/ pyskycoin

RUN cd ${REPO_ROOT} && python3 -m pytest tests/*.py
