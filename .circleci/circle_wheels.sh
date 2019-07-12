# Compile wheels
echo "Compile pyskycoin"
for PYBIN in /opt/python/*/bin; do
  "${PYBIN}/pip" install -r /io/requirements.dev.txt
  "${PYBIN}/pip" wheel /io/ -w /io/wheelhouse/
done

echo "Compile skyapi"
for PYBIN in /opt/python/*/bin; do
  "${PYBIN}/pip" install -r /io/lib/skyapi/requirements.txt
  "${PYBIN}/pip" wheel /io/lib/skyapi/ -w /io/wheelhouse/
done

ls -oa /io/wheelhouse

# Bundle external shared libraries into the wheels
for whl in /io/wheelhouse/*.whl; do
  auditwheel repair "$whl" -w /io/wheelhouse/
done