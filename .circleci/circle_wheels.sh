# Compile wheels
for PYBIN in /opt/python/*/bin; do
  "${PYBIN}/pip" install -r /io/requirements.dev.txt
  "${PYBIN}/pip" install -r /io/requirements.txt
  "${PYBIN}/pip" install -r /io/lib/skyapi/requirements.txt
  "${PYBIN}/pip" wheel /io/ -w /io/wheelhouse/
  "${PYBIN}/pip" wheel /io/lib/skyapi/ -w /io/wheelhouse/
done

# Bundle external shared libraries into the wheels
for whl in /io/wheelhouse/*.whl; do
  auditwheel repair "$whl" -w /io/wheelhouse/
done

rm -rfv /io/wheelhouse/*linux_i686.whl
rm -rfv /io/wheelhouse/*linux_x86_64.whl