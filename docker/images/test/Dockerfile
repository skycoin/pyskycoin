ARG ARCH_OS
FROM balenalib/${ARCH_OS}-debian-golang

ENV REPO_ROOT=$GOPATH/src/github.com/skycoin/pyskycoin/
ADD . ${REPO_ROOT}
ENV TOXENV=py27
ENV PIP='python -m pip'
#Install package
RUN apt-get update
RUN apt-get install make cmake python-pip python3-dev python-dev python-setuptools gcc -y
RUN mkdir swig_build && \
  cd swig_build && \
  curl -sL -o "swig-3.0.12.tar.gz" http://prdownloads.sourceforge.net/swig/swig-3.0.12.tar.gz && \
  tar -zxf swig-3.0.12.tar.gz && \
  cd swig-3.0.12 && \
  ./configure --prefix=/usr && \
  make && \
  make install && \
  cd ../../ && \
  rm -rf swig_build
# Install packages in PIP_PACKAGES
RUN ${PIP} install --upgrade tox pip setuptools
RUN ${PIP} install -r "${REPO_ROOT}/requirements.dev.txt"
RUN ${PIP} install -r "${REPO_ROOT}/lib/skyapi/requirements.txt"
RUN ${PIP} install -r "${REPO_ROOT}/lib/skyapi/test-requirements.txt"

RUN pip install -i https://test.pypi.org/simple/ pyskycoin

RUN cd ${REPO_ROOT} && python -m tox
