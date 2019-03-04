FROM balenalib/armv7hf-ubuntu-golang

RUN [ "cross-build-start" ]

RUN apt-get update  
RUN apt-get install python python-pip -y  
RUN pip install --upgrade pip setuptools tox-travis
RUN mkdir swig_build && \
	cd swig_build && \
	curl -sL -o "swig-3.0.12.tar.gz" http://prdownloads.sourceforge.net/swig/swig-3.0.12.tar.gz && \
	tar -zxf swig-3.0.12.tar.gz && \
	cd swig-3.0.12 && \
	sudo ./configure --prefix=/usr && \
	sudo make && \
	sudo make install && \
	cd ../../ && \
	sudo rm -rf swig_build

RUN [ "cross-build-end" ]  

WORKDIR $GOPATH/src/github.com/skycoin

VOLUME $GOPATH/src/