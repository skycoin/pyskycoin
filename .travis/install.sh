#!/bin/bash

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
    brew update;
    brew install swig;

    case "${TOXENV}" in
        py27)
            # Install some custom Python 3.2 requeriments
            brew install python;
            pip install tox-travis;
            ;;
        py35)
            # Install some custom Python 3.2 requeriments
            brew install python3;
            pip3 install tox-travis;
            ;;
    esac

else
    # Install some custom requeriments por Linux
    pip install tox-travis;
    eval "$(gimme 1.10)"
    sudo apt-get update && sudo apt-get install swig
fi
