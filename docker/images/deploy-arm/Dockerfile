FROM quay.io/pypa/manylinux1_x86_64

RUN yum install -y sudo pcre pcre-devel
RUN mkdir -p "$HOME/bin"
RUN PIP=/opt/python/cp27-cp27m/bin/pip source /io/.travis/install-linux.sh
RUN eval "$(gimme 1.10)"