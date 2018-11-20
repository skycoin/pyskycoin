# Supported tags and respective `Dockerfile` links

## Simple Tags

-	[`develop` (*docker/images/dev/Dockerfile*)](https://github.com/simelo/pyskycoin/blob/develop/docker/images/dev/Dockerfile)
-	[`dind` (*docker/images/dev/Dockerfile*)](https://github.com/simelo/pyskycoin/blob/develop/docker/images/dev/Dockerfile)

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

## How to use docker in docker image

### Start a daemon instance

```sh
$ docker run --privileged --name some-name -d skycoin/skycoindev-python:dind
```

### Where to store data

Create a data directory on the host system (outside the container) and mount this to a directory visible from inside the container.

The downside is that you need to make sure that the directory exists, and that e.g. directory permissions and other security mechanisms on the host system are set up correctly.

1. Create a data directory on a suitable volume on your host system, e.g. /my/own/var-lib-docker.
2. Start your docker container like this:

```sh
$ docker run --privileged --name some-name -v /my/own/var-lib-docker:/var/lib/docker \ 
-d skycoin/skycoindev-python:dind
```

# Build your own images

`SOURCE_COMMIT`: the SHA1 hash of the commit being tested.

`IMAGE_NAME`: the name and tag of the Docker repository being built.

`DOCKERFILE_PATH`: the dockerfile currently being built.


Build image from `skycoindev-cli:develop`.

```sh
$ cd skycoin
$ SOURCE_COMMIT=352c8705eb776baf79da96216308b6d164e0ae13
$ IMAGE_NAME=skycoin/skycoindev-python:develop
$ DOCKERFILE_PATH=docker/images/dev/Dockerfile
$ docker build --build-arg BDATE=`date -u +"%Y-%m-%dT%H:%M:%SZ"` \
               --build-arg SCOMMIT=$SOURCE_COMMIT \
               -f $DOCKERFILE_PATH \
               -t $IMAGE_NAME .
```

Or, if you prefer use `skycoindev-cli:dind`. Run:

```sh
$ cd skycoin
$ SOURCE_COMMIT=352c8705eb776baf79da96216308b6d164e0ae13
$ IMAGE_NAME=skycoin/skycoindev-python:dind
$ DOCKERFILE_PATH=docker/images/dev/Dockerfile
$ docker build --build-arg IMAGE_FROM="skycoin/skycoindev-cli:dind" \
               --build-arg BDATE=`date -u +"%Y-%m-%dT%H:%M:%SZ"` \
               --build-arg SCOMMIT=$SOURCE_COMMIT \
               -f $DOCKERFILE_PATH \
               -t IMAGE_NAME .
```


