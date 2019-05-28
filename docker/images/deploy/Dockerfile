ARG ARCH

FROM quay.io/pypa/manylinux1_${ARCH}

ARG GO_ARCH

ADD . /io

RUN ls /io
RUN yum install -y sudo pcre pcre-devel
RUN mkdir -p "$HOME/bin"
RUN PIP=/opt/python/cp27-cp27m/bin/pip source /io/.travis/install-linux.sh
RUN eval "$(gimme 1.10)"

RUN curl -sL -o "go1.11.3.linux-${GO_ARCH}.tar.gz" https://storage.googleapis.com/golang/go1.11.3.linux-${GO_ARCH}.tar.gz
RUN sudo tar -zxf go1.11.3.linux-${GO_ARCH}.tar.gz -C /usr/local
ENV GOROOT=/usr/local/go
ENV PATH="${PATH}:/usr/local/go/bin"
ENV CGO_ENABLE=1

RUN go version
RUN go env

RUN for PYBIN in /opt/python/*/bin; do \
        "${PYBIN}/pip" install -r /io/requirements.dev.txt \
        "${PYBIN}/pip" wheel /io/ -w wheelhouse/ \
    done

RUN for whl in wheelhouse/*.whl; do \
        auditwheel repair "$whl" -w /io/wheelhouse/ \
    done

RUN ls /io/wheelhouse
RUN mkdir -p /io/dist
RUN cp -v /io/wheelhouse/* /io/dist
RUN python -m pip install twine
RUN python -m twine upload -u pyskycoin -p "prerelease_0.X" --skip-existing --repository-url https://test.pypi.org/legacy/ /io/dist/*

WORKDIR /io