# Install twine
echo "Installing twine"
python -m pip install twine

echo "Generating distribution archives before deploy"
make sdist
make bdist_wheel
if [ $TRAVIS_OS_NAME == "linux" ]; then make bdist_manylinux_amd64 ; fi

#Upload to testPyPI
echo "Upload to testPyPI"
twine upload -u pyskycoin -p "prerelease_0.X" --skip-existing --repository-url https://test.pypi.org/legacy/ lib/skyapi/dist/*
