#!/usr/bin/env bash

set -x

if [[ "$URL_DEPLOY" ]]; then

 $TWINE_PATH upload -u ${PYPI_USER} -p ${PYPI_PASSWD} --skip-existing --repository-url ${URL_DEPLOY} /io/dist/*sky*

else

 $TWINE_PATH upload -u ${PYPI_USER} -p ${PYPI_PASSWD} --skip-existing  /io/dist/*sky*
 go get github.com/tcnksm/ghr
 ghr -t ${GITHUB_OAUTH_TOKEN} -u ${PROJECT_USERNAME} -r ${PROJECT_REPONAME} -c ${SHA1} ${VERSION} /io/dist/*sky*

fi