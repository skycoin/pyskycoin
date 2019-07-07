#Install twine
pip install -U twine

#Make dist
make sdist
make bdist_wheel
if [ $TRAVIS_OS_NAME == "linux" && $TOXENV == "py37" ]; then make bdist_manylinux_amd64 ; fi

#Upload to PyPi
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
twine upload --repository-url https://upload.pypi.org/legacy/ lib/skyapi/dist/*