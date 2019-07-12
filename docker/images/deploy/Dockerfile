ARG ARCH

FROM quay.io/pypa/manylinux1_${ARCH}

ARG GO_ARCH
ARG URL_DEPLOY
ARG PYPI_USER
ARG PYPI_PASSWD
ADD . /io

RUN ls /io
RUN yum install -y sudo pcre pcre-devel curl git --skip-broken
RUN mkdir -p "$HOME/bin"
ENV PIP "/opt/python/cp27-cp27m/bin/pip"
ENV REPO_ROOT "/io/"
RUN curl -sL -o "$HOME/bin/gimme" https://raw.githubusercontent.com/travis-ci/gimme/master/gimme
RUN chmod +x "$HOME/bin/gimme"
ENV PATH="${PATH}:$HOME/bin/gimme"
RUN eval "$(gimme 1.11)"

RUN $PIP install --upgrade pip setuptools tox-travis
RUN $PIP install -r "$REPO_ROOT/requirements.dev.txt"
RUN $PIP install -r "$REPO_ROOT/lib/skyapi/requirements.txt"
RUN $PIP install -r "$REPO_ROOT/lib/skyapi/test-requirements.txt"

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

RUN curl -sL -o "go1.11.3.linux-${GO_ARCH}.tar.gz" https://storage.googleapis.com/golang/go1.11.12.linux-${GO_ARCH}.tar.gz
RUN tar -zxf go1.11.3.linux-${GO_ARCH}.tar.gz -C /usr/local
ENV GOROOT=/usr/local/go
ENV PATH="${PATH}:/usr/local/go/bin"
ENV CGO_ENABLE=1

RUN go version
RUN go env
RUN go get github.com/gz-c/gox
RUN cd /io && git submodule update --init --recursive 
RUN make -C /io/gopath/src/github.com/skycoin/libskycoin dep
RUN make -C /io build-libc
RUN make -C /io build-swig 
RUN sh /io/.circleci/circle_wheels.sh

RUN ls /io/wheelhouse
RUN mkdir -p /io/dist
RUN cp -v /io/wheelhouse/* /io/dist
RUN $PIP install twine
RUN /opt/python/cp27-cp27m/bin/twine upload -u ${PYPI_USER} -p ${PYPI_PASSWD} --skip-existing --repository-url ${URL_DEPLOY} /io/dist/*

WORKDIR /io