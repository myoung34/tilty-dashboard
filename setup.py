#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import find_packages, setup

README = None
with open(os.path.abspath('README.md')) as fh:
    README = fh.read()

setup(
    name='tilty_dashboard',
    version='0.0.1',
    description=README,
    author='Marcus Young',
    author_email='3vilpenguin@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    package_data={
       # If any package contains *.txt or *.rst files, include them:
       "": ["*.html"],
    },
    install_requires=[
        'Flask',
        'Flask-Bootstrap',
        'Flask-Cors',
        'Flask-SQLAlchemy',
        'Flask-SocketIO',
        'Flask-Script',
        'backoff',
        'configobj',
        'gunicorn',
        'Werkzeug',
        'eventlet',
    ],
    entry_points={
        'console_scripts': [
            'tilty_dashboard=tilty_dashboard.controller:main',
            'tilty_dashboard-worker=tilty_dashboard.worker:main',
        ],
    }
)
