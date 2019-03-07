FROM balenalib/armv7hf-ubuntu-golang

RUN [ "cross-build-start" ]

RUN uname -a
RUN apt-get update  
RUN apt-get install python python-pip curl swig git make -y  
RUN pip install --upgrade pip setuptools tox-travis
RUN mkdir -p $GOPATH/src && mkdir -p $GOPATH/src/github.com && mkdir -p $GOPATH/src/github.com/skycoin
RUN go get -v github.com/gz-c/gox

RUN [ "cross-build-end" ]  

WORKDIR $GOPATH/src/github.com/skycoin

VOLUME $GOPATH/src/