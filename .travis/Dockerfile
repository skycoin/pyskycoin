FROM balenalib/armv7hf-ubuntu-golang

RUN [ "cross-build-start" ]

RUN apt-get update  
RUN apt-get install python python-pip curl swig -y  
RUN pip install --upgrade pip setuptools tox-travis

RUN [ "cross-build-end" ]  

WORKDIR $GOPATH/src/github.com/skycoin

VOLUME $GOPATH/src/