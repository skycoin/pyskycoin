ARG IMAGE
FROM ${IMAGE}

ADD . /io
RUN ls -oa /io
ENV PIP='python3 -m pip'
#Install package
RUN apt-get update
RUN apt-get install make cmake python3-dev python3-pip python3-setuptools python3-pytest libpcre3-dev curl gcc -y

# Install packages in PIP_PACKAGES
RUN ${PIP} install -i https://test.pypi.org/simple/ pyskycoin

RUN ls -oa /io/tests
RUN python3 -m pytest /io/tests/*.py
