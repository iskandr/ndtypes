#!/usr/bin/env python

from setuptools import setup, Extension

import sys


setup(
    name="ndtypes",
    description="Types for array-oriented domain-specific languages embedded in Python.", 

    long_description="",
    classifiers=['Development Status :: 3 - Alpha',
                 'Topic :: Software Development :: Libraries',
                 'License :: OSI Approved :: BSD License',
                 'Intended Audience :: Developers',
                 'Programming Language :: Python :: 2.7',
                 ],
    author="Alex Rubinsteyn",
    author_email="alexr@cs.nyu.edu",
    license="BSD",
    version="0.1.3",
    url="http://github.com/iskandr/ndtypes",
    packages=[ 'ndtypes'],
    package_dir={ '' : '.' },
    requires=['treelike'] 
    )
