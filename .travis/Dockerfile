FROM resin/armv7hf-ubuntu-golang

RUN [ "cross-build-start" ]

RUN apt-get update  
RUN apt-get install python python-pip curl swig git make -y  
RUN pip install --upgrade pip setuptools tox-travis
RUN cd $GOPATH/src/github.com/skycoin && git clone --recursive --depth=50 https://github.com/simelo/pyskycoin.git --branch=stdevHan_102_matrix_arm32
RUN cd $GOPATH/src/github.com/skycoin/pyskycoin && make test

RUN [ "cross-build-end" ]  

WORKDIR $GOPATH/src/github.com/skycoin

VOLUME $GOPATH/src/