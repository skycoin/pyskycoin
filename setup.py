"""
 Skycoin python extension

"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages, Extension
# To use a consistent encoding
from codecs import open
from os import path

import os
import platform

script_dirname = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(script_dirname, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
   
build_path = path.join(*("gopath/src/github.com/skycoin/skycoin/build/libskycoin".split('/')))
skypath = path.join(*("gopath/src/github.com/skycoin/skycoin".split('/')))

lib_path = path.join(skypath, 'build', 'libskycoin')
library_file = path.join(lib_path, 'libskycoin.a')


setup(
	name='Pyskycoin',  # Required
    version='0.24',  # Required
	description='Skycoin Python Library',
    long_description=long_description,
    url='https://github.com/simelo/pyskycoin',
    author='stdevEclipse',  # Optional
    author_email='dev0003@simelo.tech',
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='skycoin crypto coin currency blockchain',  # Optional
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
    install_requires=[],
    extras_require={  # Optional
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    package_data={
    },
    entry_points={
        'console_scripts': [
        ],
    },
    ext_modules = [Extension("_skycoin", ["swig/pyskycoin_wrap.c"],
                         include_dirs=[
                             "swig/include",
                             path.join(skypath, "include")
                         ],
                         extra_link_args=[library_file],
                         depends=[],
                   )],

)
