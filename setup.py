"""The setup for 'todo' python todo generate.

See:
https://github.com/thee-engineer/todo
"""

import io

from setuptools import setup, find_packages
from codecs import open as copen
from os import path


CWD = path.abspath(path.dirname(__file__))


def read_description():
    """Read the LONG DESCRIPTION."""
    with copen(path.join(CWD, 'README.md'), encoding='utf-8') as f:
        return f.read()


def read(*names, **kwargs):
    """Read file contents."""
    with io.open(
        path.join(path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()


setup(
    name='todo2',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.1.0',

    description='A python todo generator.',
    long_description=read_description(),

    # The project's main homepage.
    url='https://github.com/thee-engineer/todo',

    # Author details
    author='Alexandru-Paul Copil (thee-engineer)',
    author_email='alexandru.p.copil@gmail.com',

    # Choose your license
    license='BEERWARE',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project?
        'Development Status :: 3 - Alpha',
        'License :: Freely Distributable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],

    # What does your project relate to?
    keywords='todo',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['docs', 'old', 'tests', 'dist', 'build']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=[],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'todo = todo.main:main',
        ],
    },
)
