# -*- coding: utf-8 -*-
"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='murre',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.4.0',

    description='The amazing Murre will normalize non-standard Finnish and Swedish, and dialectalize standard Finnish!',
    long_description=long_description,
    long_description_content_type='text/markdown',

    # The project's main homepage.
    url='https://github.com/mikahama/murre',

    # Author details
    author='Mika Hämäläinen, Rootroo Ltd',
    author_email='mika@rootroo.com',
    zip_safe=False,
    # Choose your license
    license='Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        "Topic :: Text Processing :: Linguistic",

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',

    ],

    # What does your project relate to?
    keywords='Spoken Finnish, spelling normalization',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=["murre"],
    package_dir={'murre': 'murre'},

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=["natas", "OpenNMT-tf>=2.18.1", "pyonmttok>=1.23.0", "tensorflow-macos==2.11.0", "tensorflow-addons==0.19.0"],
   # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={},

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        'murre': ['models/*.txt'],
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=[],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={},
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/mikahama/murre/issues',
        'Developer': 'https://mikakalevi.com/'
    },
)