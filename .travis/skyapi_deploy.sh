# Install twine
echo "Installing twine"
python -m pip install twine

#Upload to PyPi
echo "Upload to PyPi"
twine upload -u $PYPI_USER -p $PYPI_PWD --repository-url https://upload.pypi.org/legacy/ lib/skyapi/dist/*