"""
 Skycoin python extension

"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages, Extension
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


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
    install_requires=['peppercorn'], 
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
    
    ext_modules = [Extension("pyskycoin", ["swig/pyskycoin_wrap.c"],
                         include_dirs=["swig/include", "skycoin/include"],
                         depends=["swig/include/libskycoin.h", "swig/include/extras.h"])],

    
    #Extension('foo', ['foo.c'])
)
