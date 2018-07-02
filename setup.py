"""
 Skycoin python extension

"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages, Extension
#from setuptools.command.build_ext import build_ext
# To use a consistent encoding
from codecs import open
from os import path
#import os, subprocess
#from distutils.errors import DistutilsSetupError
#from distutils import log as distutils_logger
import platform

script_dirname = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(script_dirname, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

skypath = path.join(*("gopath/src/github.com/skycoin/skycoin".split('/')))

lib_path = path.join(skypath, 'build', 'libskycoin')
extra_link_args = []

if platform.system() == 'Darwin':
    extra_link_args.append('-Wl,-rpath,' + lib_path)

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
    #cmdclass = {'build_ext': skycoin_build_ext},
    ext_modules = [Extension("_skycoin", ["swig/pyskycoin_wrap.c"],
                         include_dirs=[
                             "swig/include",
                             path.join(skypath, "include")
                         ],
                         extra_link_args = extra_link_args,
                         depends=[],
                         libraries = [':libskycoin.a'],
                         library_dirs = [
                             lib_path
                         ],
                   )],

)
