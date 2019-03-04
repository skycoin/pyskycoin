FROM resin/armv7hf-debian

RUN [ "cross-build-start" ]

RUN apt-get update  
RUN apt-get install python  
RUN pip install virtualenv

RUN [ "cross-build-end" ]  