#!/bin/bash

set -ev

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
    brew update;
    brew outdated pyenv || brew upgrade pyenv;
    brew install pyenv-virtualenv
    pyenv install $PYTHON
    export PYENV_VERSION=$PYTHON
    export PATH="/Users/travis/.pyenv/shims:${PATH}"
    brew install swig;
    eval "$(pyenv init -)";
    eval "$(pyenv virtualenv-init -)";
    pyenv virtualenv $PYTHON venv;
    pyenv activate venv;
    python --version;
    pip install tox;

    case "${TOXENV}" in
        py27)
            # pip install tox-travis;
            ;;
        py35)
            #pip3 install tox-travis;
            ;;
    esac

else
    # Install some custom requeriments por Linux
    pip install tox-travis;
    eval "$(gimme 1.10)"
    sudo apt-get update && sudo apt-get install swig
fi
