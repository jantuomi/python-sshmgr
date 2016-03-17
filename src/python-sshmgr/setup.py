#!/usr/bin/env python

from setuptools import setup

setup(name='sshmgr',
    version='0.1',
    description='',
    author='Jan Tuomi',
    author_email='jan-sebastian.tuomi@aalto.fi',
    url='',
    packages=['sshmgr', 'sshmgr.utils'],
    entry_points= {'console_scripts': [
            'sshmgr = sshmgr.manager:start',
        ],
    },
)
