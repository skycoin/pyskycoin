FROM balenalib/armv7hf-ubuntu-golang

ADD . $GOPATH/src/github.com/skycoin/pyskycoin/

RUN [ "cross-build-start" ]

RUN uname -a
RUN ls $GOPATH/src/github.com/skycoin/pyskycoin
RUN apt-get update  
RUN apt-get install apt-utils python python-pip curl swig git make -y  
RUN pip install --upgrade pip setuptools tox-travis
RUN go get github.com/gz-c/gox
RUN go get -t ./...
RUN cd $GOPATH/src/github.com/skycoin/pyskycoin && make test

RUN [ "cross-build-end" ]  

WORKDIR $GOPATH/src/github.com/skycoin

VOLUME $GOPATH/src/