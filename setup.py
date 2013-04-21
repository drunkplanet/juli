# coding: utf-8

__VERSION__ = '0.0.1'

import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

params = {
    'name': 'juli',
    'version': __VERSION__,
    'description': 'Make texts more readable',
    'long_description': read('README.md'),
    'author': 'shaung',
    'author_email': '_@shaung.org',
    'url': 'https://github.com/shaung/juli/',
    'py_modules': ['juli'],
    'license': 'BSD',
    'download_url': 'https://github.com/shaung/juli/archive/master.zip',
    'zip_safe': False,
    'classifiers': [
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    'install_requires': [
    ],
}

from setuptools import setup
setup(**params)
