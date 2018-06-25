#!/bin/bash

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
    brew update;
    brew install swig;
    pyenv install 3.4.0;
    pyenv global 3.4.0;
    brew install pyenv-virtualenv;
    pyenv virtualenv venv34
    sudo easy_install pip

    case "${TOXENV}" in
        py27)
            # Install some custom Python 3.2 requeriments
            brew install python;
            pip install tox-travis;
            ;;
        py35)
            # Install some custom Python 3.5 requeriments
            pip3 install tox-travis;
            ;;
    esac

else
    # Install some custom requeriments por Linux
    pip install tox-travis;
    eval "$(gimme 1.10)"
    sudo apt-get update && sudo apt-get install swig
fi
