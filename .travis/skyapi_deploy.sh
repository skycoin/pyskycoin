# Install twine
echo "Installing twine"
python -m pip install twine

#Upload to PyPi
echo "Upload to PyPI"
twine upload -u $PYPI_USER -p $PYPI_PASSWD --repository-url https://upload.pypi.org/legacy/ lib/skyapi/dist/*sky*
