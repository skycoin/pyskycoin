# Compile wheels
  pip wheel /io/ -w /io/wheelhouse/
  pip wheel /io/lib/skyapi/ -w /io/wheelhouse/
  # python3.4 -m pip wheel /io/ -w wheelhouse/
  pip3 wheel /io/lib/skyapi/ -w /io/wheelhouse/
  pip3 wheel /io/ -w /io/wheelhouse/
  # python3.6 -m pip wheel /io/ -w wheelhouse/
  # python3.7 -m pip wheel /io/ -w wheelhouse/

# # Bundle external shared libraries into the wheels
# for whl in wheelhouse/*.whl; do
#   python -m auditwheel repair "$whl" -w /io/wheelhouse/
#   # python3.4 -m auditwheel repair "$whl" -w /io/wheelhouse/
#   python3 -m auditwheel repair "$whl" -w /io/wheelhouse/
#   # python3.6 -m auditwheel repair "$whl" -w /io/wheelhouse/
#   # python3.7 -m auditwheel repair "$whl" -w /io/wheelhouse/
# done