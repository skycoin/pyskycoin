# Supported tags and respective `Dockerfile` links

## Simple Tags

- [`develop` (*docker/images/dev/Dockerfile*)](https://github.com/simelo/pyskycoin/blob/develop/docker/images/dev/Dockerfile)
- [`dind` (*docker/images/dev/Dockerfile*)](https://github.com/simelo/pyskycoin/blob/develop/docker/images/dev/Dockerfile)

## Pyskycoin CLI/DIND development image

This image (CLI) has the necessary tools to build, test, edit, lint and version the Pyskycoin
source code. It comes with some versions of Python (2.7, 3.4, 3.5 and 3.6) and with Vim editor installed, along with some plugins
to ease go development and version control with git.

Besides it is possible to use Docker in Docker (DIND) Pyskycoin development image,
it is based on `skycoin/skycoindev-cli:dind` and provides all tools included in Pyskycoin CLI image.

## How to use this image

## Initialize your development environment

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

## Pre-installed pip packages

In order to provide a good development environment for you, some pip packages has been installed:

- [setuptools](https://pypi.org/project/setuptools/)
- [wheel](https://pypi.org/project/wheel/)
- [tox](https://pypi.org/project/tox/)
- [tox-pyenv](https://pypi.org/project/tox-pyenv/)
- [tox-travis](https://pypi.org/project/tox-travis/)
- [pytest](https://pypi.org/project/pytest/)
- [pytest-runner](https://pypi.org/project/pytest-runner/)
- [virtualenv](https://pypi.org/project/virtualenv/)
- [pylint](https://pypi.org/project/pylint/)
- [flake8](https://pypi.org/project/flake8/)

## Running commands inside the container

You can run commands by just passing them to the image. Everything is run
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

## How to use Docker in Docker image

### Start a daemon instance

```sh
$ docker run --privileged --name some-name \
    -d skycoin/skycoindev-python:dind
```

### Where to store data

Create a data directory on the host system (outside the container) and mount this to a directory visible from inside the container.

The downside is that you need to make sure that the directory exists, and that e.g. directory permissions and other security mechanisms on the host system are set up correctly.

1. Create a data directory on a suitable volume on your host system, e.g. /my/own/var-lib-docker.
2. Start your docker container like this:

```sh
$ docker run --privileged --name some-name \
    -v /my/own/var-lib-docker:/var/lib/docker \ 
    -d skycoin/skycoindev-python:dind
```

### Use Visual Studio Code

In order to use Visual Studio Code on development process, please read carefull
the [documentation of oficial Skycoin Visual Studio Code dev image](https://github.com/skycoin/skycoin/tree/develop/docker/images/dev-vscode#initialize-your-development-environment)

#### Pre-installed extensions

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Python Docstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)
- [Trailing Spaces](https://marketplace.visualstudio.com/items?itemName=shardulm94.trailing-spaces)

#### Add extensions to Visual Studio Code

Like Skycoin Visual Studio Code dev image, you must pass `VS_EXTENSIONS` environment variable
to the command-line with extensions you prefer. **Pass it if you use a docker image with Visual Studio Code**

```sh
$ docker run --rm -it -v /tmp/.X11-unix:/tmp/.X11-unix \
        -v $PWD:/go/src/github.com/simelo/libskycoin-dotnet \
        -w $GOPATH/src/github.com/simelo/libskycoin-dotnet \
        -e DISPLAY=$DISPLAY \
        -e VS_EXTENSIONS="ms-python.python rebornix.Ruby" \
        simelotech/skycoindev-dotnet:vscode
```

## Build your own images

The build process relies on the following parameters

- `SOURCE_COMMIT`: the SHA1 hash of the commit being tested.
- `IMAGE_NAME`: the name and tag of the Docker repository being built.
- `DOCKERFILE_PATH`: the dockerfile currently being built.
- `PIP_PACKAGES`: pip packages to install inside docker image.
- `VS_EXTENSIONS` Visual Studio Code extensions to add on docker image.

In order to build image from `skycoindev-cli:develop` execute the following shell command

```sh
$ cd pyskycoin
$ SOURCE_COMMIT=$(git rev-parse HEAD)
$ IMAGE_NAME=skycoin/skycoindev-python:develop
$ DOCKERFILE_PATH=docker/images/dev-cli/Dockerfile
$ docker build --build-arg BDATE=`date -u +"%Y-%m-%dT%H:%M:%SZ"` \
               --build-arg SCOMMIT=$SOURCE_COMMIT \
               --build-arg PIP_PACKAGES="Twisted tox" \
               -f $DOCKERFILE_PATH \
               -t "$IMAGE_NAME" .
```

If do you prefer to use `skycoindev-cli:dind` then run:

```sh
$ cd pyskycoin
$ IMAGE_FROM="skycoin/skycoindev-cli:dind"
$ SOURCE_COMMIT=$(git rev-parse HEAD)
$ IMAGE_NAME=skycoin/skycoindev-python:dind
$ DOCKERFILE_PATH=docker/images/dev-cli/Dockerfile
$ docker build --build-arg IMAGE_FROM="$IMAGE_FROM" \
               --build-arg BDATE=`date -u +"%Y-%m-%dT%H:%M:%SZ"` \
               --build-arg SCOMMIT=$SOURCE_COMMIT \
               --build-arg PIP_PACKAGES="Twisted tox" \
               -f $DOCKERFILE_PATH \
               -t "$IMAGE_NAME" .
```

Nevertheless, if do you like use Visual Studio Code instead of CLI, you can change `IMAGE_FROM` to build it. **When base image use Visual Studio Code, you can use `VS_EXTENSIONS` build arg**

```sh
$ cd pyskycoin
$ git submodule update --init --recursive
$ # Move to vscode folder to avoid file errors with vscode docker image
$ cd gopath/src/github.com/skycoin/skycoin/docker/images/dev-vscode/
$ IMAGE_FROM="skycoin/skycoindev-python:develop"
$ SOURCE_COMMIT=$(git rev-parse HEAD)
$ IMAGE_NAME=skycoin/skycoindev-python:vscode
$ DOCKERFILE_PATH=docker/images/dev-cli/Dockerfile
$ docker build --build-arg IMAGE_FROM="$IMAGE_FROM"
               --build-arg BDATE=`date -u +"%Y-%m-%dT%H:%M:%SZ"` \
               --build-arg SCOMMIT=$SOURCE_COMMIT \
               --build-arg PIP_PACKAGES="matplotlib tox" \
               --build-arg VS_EXTENSIONS="almenon.arepl ms-python.python" \
               -f $DOCKERFILE_PATH \
               -t "$IMAGE_NAME" .
```

## Automated builds

Docker Cloud is configured to build images from `develop`
and `master` branch on every push made after merging. The same process 
is triggered for all feature branches matching the pattern
`/^([^_]+)_t([0-9]+)_.*docker.*/`. The tag generated for such images
will be of the form `feature-{\1}-{\2}`.
