ARG IMAGE
FROM ${IMAGE}

ADD . /io
RUN ls -oa /io
ENV PIP='python -m pip'
#Install package
RUN apt-get update
RUN apt-get install make cmake python-dev python-pip python-setuptools python-pytest libpcre3-dev curl gcc -y

# Install packages in PIP_PACKAGES
RUN ${PIP} install -i https://test.pypi.org/simple/ pyskycoin

RUN ls -oa /io/tests
RUN py.test /io/tests/*.py
