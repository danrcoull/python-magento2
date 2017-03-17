#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
    Magento API

    :license: BSD, see LICENSE for more details

'''
import os
from setuptools import setup

exec(open(os.path.join('magento2', 'version.py')).read())

setup(
    name = 'magento2',
    version=VERSION,
    url='https://github.com/fulfilio/magento/',
    license='BSD 3-Clause',
    author='Gerhard Baumgartner, Callino',
    author_email='gbaumgartner@callino.at',
    description='Magento 2 Core API Client',
    long_description=open('README.rst').read(),
    packages=['magento2'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'suds-jurko>=0.6',
    ],
    classifiers=[
        'Development Status :: 6 - Mature',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
