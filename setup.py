#!/usr/bin/env python

__author__ = 'Jason Corbett'

from setuptools import setup

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Software Development :: Quality Assurance',
    'Topic :: Software Development :: Testing'
]

requirements = []
with open('requirements.txt', 'r') as reqfile:
    requirements.extend(reqfile.read().split())

setup(
    name="slickqa-selenium",
    description="An api for writing tests using selenium v2's webdriver api.",
    version="1.0" + open("build.txt").read(),
    license="Apache Software License v2",
    long_description=open('README.rst').read(),
    packages=['slickselenium'],
    package_data={'': ['*.txt', '*.rst', '*.html']},
    include_package_data=True,
    install_requires=requirements,
    tests_require=['nose',],
    classifiers=classifiers,
    author="Jason Corbett",
    url="http://github.com/slickqa/slickqa-selenium"
)
