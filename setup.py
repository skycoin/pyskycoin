"""
 Skycoin python extension

"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages, Extension
from setuptools.command.build_ext import build_ext
from distutils.errors import DistutilsSetupError

# To use a consistent encoding
from codecs import open
from os import path
import os
import subprocess
import platform
import sys
from skycoin import __version__

script_dirname = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(script_dirname, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


class skycoin_build_ext(build_ext, object):
    def build_extension(self, ext):

        if ext.name != "_skycoin":
            # Handle unspecial extensions with the parent class' method
            super(skycoin_build_ext, self).build_extension(ext)
        else:
            # Handle special extension
            sources = ext.sources
            if sources is None or not isinstance(sources, (list, tuple)):
                raise DistutilsSetupError(
                    "in 'ext_modules' option (extension '%s'), "
                    "'sources' must be present and must be "
                    "a list of source filenames" % ext.name
                )
            sources = list(sources)

            if len(sources) > 1:
                sources_path = os.path.commonprefix(sources)
            else:
                sources_path = os.path.dirname(sources[0])
            sources_path = os.path.realpath(sources_path)
            if not sources_path.endswith(os.path.sep):
                sources_path += os.path.sep

            if not os.path.exists(sources_path) or not os.path.isdir(sources_path):
                raise DistutilsSetupError(
                    "in 'extensions' option (extension '%s'), "
                    "the supplied 'sources' base dir "
                    "must exist" % ext.name
                )

            make_path = os.path.realpath(os.path.join(sources_path, ".."))

            make_process = subprocess.Popen(
                "make build-libc-swig",
                cwd=make_path,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True,
            )
            stdout, stderr = make_process.communicate()
            print("stdout:")
            sys.stderr.write(str(stdout))
            if len(stderr) > 0:
                print("stderr:")
                sys.stderr.write(str(stderr))
            # After making the library build the c library's
            # python interface with the parent build_extension method
            super(skycoin_build_ext, self).build_extension(ext)


skypath = path.join(*("gopath/src/github.com/skycoin/libskycoin".split("/")))
lib_path = path.join(skypath, "build", "libskycoin")
library_file = path.join(lib_path, "libskycoin.a")
extra_link_args = []
if platform.system() == "Darwin":
    extra_link_args += ["-framework", "Foundation", "-framework", "Security"]
extra_link_args.append(library_file)

setup(
    name='pyskycoin',  # Required
    version=__version__,  # Required
    description="Skycoin Python Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/skycoin/pyskycoin",
    author="Ratmil Torres",  # Optional
    author_email="skycoin@simelo.tech",
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "urllib3", "certifi"],
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="skycoin crypto coin currency blockchain",  # Optional
    py_modules=["skycoin"],
    packages=find_packages(exclude=["contrib", "docs", "tests"]),  # Required
    install_requires=[],
    extras_require={"dev": ["check-manifest"], "test": ["coverage"]},  # Optional
    package_data={},
    entry_points={"console_scripts": []},
    cmdclass={"build_ext": skycoin_build_ext},
    ext_modules=[
        Extension(
            "_skycoin",
            ["swig/pyskycoin_wrap.c"],
            include_dirs=["swig/include", path.join(skypath, "include")],
            extra_link_args=extra_link_args,
            depends=[],
        )
    ],
)