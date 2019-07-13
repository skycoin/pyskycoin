#!/usr/bin/env bash

set -x

git --version

export VERSION="$(git describe --tags --exact-match HEAD)"

if [[ "$VERSION" ]]; then
	docker build  --build-arg VERSION --build-arg SHA1=$CIRCLE_SHA1 --build-arg GITHUB_OAUTH_TOKEN --build-arg PROJECT_USERNAME=$CIRCLE_PROJECT_USERNAME --build-arg PROJECT_REPONAME=$CIRCLE_PROJECT_REPONAME --build-arg GO_ARCH=386 --build-arg ARCH=i686 --build-arg $PYPI_USER --build-arg $PYPI_PASSWD --build-arg URL_DEPLOY=https://pypi.org/legacy/  --file $GOPATH/src/github.com/skycoin/pyskycoin/docker/images/deploy/Dockerfile  $GOPATH/src/github.com/skycoin/pyskycoin -t skydev-deploy
	docker build  --build-arg VERSION --build-arg SHA1=$CIRCLE_SHA1 --build-arg GITHUB_OAUTH_TOKEN --build-arg PROJECT_USERNAME=$CIRCLE_PROJECT_USERNAME --build-arg PROJECT_REPONAME=$CIRCLE_PROJECT_REPONAME --build-arg GO_ARCH=amd64 --build-arg ARCH=x86_64 --build-arg $PYPI_USER --build-arg $PYPI_PASSWD --build-arg URL_DEPLOY=https://pypi.org/legacy/ --file $GOPATH/src/github.com/skycoin/pyskycoin/docker/images/deploy/Dockerfile  $GOPATH/src/github.com/skycoin/pyskycoin -t skydev-deploy
	docker build  --build-arg VERSION --build-arg SHA1=$CIRCLE_SHA1 --build-arg GITHUB_OAUTH_TOKEN --build-arg PROJECT_USERNAME=$CIRCLE_PROJECT_USERNAME --build-arg PROJECT_REPONAME=$CIRCLE_PROJECT_REPONAME --build-arg $PYPI_USER --build-arg $PYPI_PASSWD --build-arg ARCH=armv7hf --file $GOPATH/src/github.com/skycoin/pyskycoin/docker/images/deploy/Dockerfile-arm  $GOPATH/src/github.com/skycoin/pyskycoin -t skydev-test
	docker build  --build-arg VERSION --build-arg SHA1=$CIRCLE_SHA1 --build-arg GITHUB_OAUTH_TOKEN --build-arg PROJECT_USERNAME=$CIRCLE_PROJECT_USERNAME --build-arg PROJECT_REPONAME=$CIRCLE_PROJECT_REPONAME --build-arg $PYPI_USER --build-arg $PYPI_PASSWD --build-arg ARCH=aarch64 --file $GOPATH/src/github.com/skycoin/pyskycoin/docker/images/deploy/Dockerfile-arm  $GOPATH/src/github.com/skycoin/pyskycoin -t skydev-test
fi