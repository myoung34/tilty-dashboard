#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='tilty_dashboard',
    description='A live dashboard for the tilty based on Flask-SocketIO',  # noqa
    author='Marcus Young',
    author_email='3vilpenguin@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    version='1.2.0',
    package_data={
       "": ["*.html", "*.png", "*.css", "*.js"],
    },
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        'Flask==2.1.0',
        'Jinja2==2.11.3',
        'Flask-SocketIO==5.2.0',
        'Flask-SQLAlchemy==2.4.4',
        'Werkzeug==2.1.2',
        'Flask-Bootstrap==3.3.7',
        'Flask-Cors==3.0.9',
        'gunicorn==20.0.4',
        'configobj==5.0.6',
        'eventlet==0.33.1',
        'flask-session==0.3.2',
        'urllib3==1.26.5',
    ]
)
