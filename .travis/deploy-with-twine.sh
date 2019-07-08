#Install twine
echo "Installing twine"
python -m pip install twine

#Make wheels
echo "Making wheels"
make sdist
make bdist_wheel
if [ $TRAVIS_OS_NAME == "linux" && $TOXENV == "py37" ]; then make bdist_manylinux_amd64 ; fi

echo "Upload to testPyPi"
twine upload -u pyskycoin -p "prerelease_0.X" --verbose --repository-url https://test.pypi.org/legacy/ dist/*
twine upload -u pyskycoin -p "prerelease_0.X" --verbose --repository-url https://test.pypi.org/legacy/ lib/skyapi/dist/*
#Upload to PyPi
# echo "Upload to PyPi"
# twine upload -u $PYPITEST_USER -p $PYPITEST_PWD --repository-url https://upload.pypi.org/legacy/ dist/*
# twine upload -u $PYPITEST_USER -p $PYPITEST_PWD --repository-url https://upload.pypi.org/legacy/ lib/skyapi/dist/*
