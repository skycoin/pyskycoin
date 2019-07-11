# Install twine
echo "Installing twine"
python -m pip install twine

echo "Upload to testPyPI"
twine upload -u pyskycoin -p "prerelease_0.X" --repository-url https://test.pypi.org/legacy/ lib/skyapi/dist/*
