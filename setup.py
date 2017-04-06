#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

DIR = os.path.dirname(os.path.abspath(__file__))


from setuptools import setup, find_packages


readme = open(os.path.join(DIR, 'README.md')).read()


setup(
    name='trie',
    version="0.1.1",
    description="""Python implementation of the Trie structure""",
    long_description=readme,
    include_package_data=True,
    py_modules=['trie'],
    install_requires=[
    ],
    license="MIT",
    zip_safe=False,
    keywords='trie',
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)