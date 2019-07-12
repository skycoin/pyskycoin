#!/usr/bin/env bash

set -x

if [[ "$URL_DEPLOY" ]]; then

 $TWINE_PATH upload -u ${PYPI_USER} -p ${PYPI_PASSWD} --skip-existing --repository-url ${URL_DEPLOY} /io/dist/*

else

 $TWINE_PATH upload -u ${PYPI_USER} -p ${PYPI_PASSWD} --skip-existing  /io/dist/*
 
fi