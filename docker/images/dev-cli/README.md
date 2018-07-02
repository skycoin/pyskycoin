# Supported tags and respective `Dockerfile` links

## Simple Tags

-	[`develop` (*docker/images/dev-cli/Dockerfile*)](https://github.com/simelo/pyskycoin/blob/develop/docker/images/dev-cli/Dockerfile)

# Pyskycoin CLI development image

This image has the necessary tools to build, test, edit, lint and version the Pyskycoin
source code.  It comes with some versions of Python (2.7, 3.4, 3.5 and 3.6) and with Vim editor installed, along with some plugins
to ease go development and version control with git.

# How to use this image

## Initialize your development environment.

```sh
$ mkdir src
$ docker run --rm \
    -v ${PWD}/src:/usr/local/src skycoin/skycoindev-python:develop \
    git clone https://github.com/simelo/pyskycoin.git \
$ sudo chown -R `whoami` src
```

This downloads the pyskycoin source to src/pyskycoin and changes the owner
to your user. This is necessary, because all processes inside the container run
as root and the files created by it are therefore owned by root.

## Running commands inside the container

You can run commands by just passing the them to the image.  Everything is run
in a container and deleted when finished.

### Running tests

```sh
$ docker run --rm \
    -v ${PWD}/src:/usr/local/src skycoin/skycoindev-python:develop \
    sh -c "cd pyskycoin; make test"
```

### Editing code

```sh
$ docker run --rm \
    -v ${PWD}/src:/usr/local/src skycoin/skycoindev-python:develop \
    vim
```

