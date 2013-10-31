#!/usr/bin/env python
from setuptools import setup

setup(
    name='cos_syncer',
    version='1.0.0',
    description="A script that syncs a local file system to the COS",
    long_description=open('README.md').read(),
    author='HubSpot Dev Team',
    author_email='devteam+hapi@hubspot.com',
    url='https://github.com/HubSpot/cos_syncer',
    download_url='https://github.com/HubSpot/cos_syncer/tarball/v1.0.0',
    license='LICENSE.txt',
    packages=['cos_syncer'],
    install_requires=[
        'nose>=1.1.0',
        'unittest2>=0.5.0',
        'simplejson>=2.1.0',
        'snakecharmer==1.0.0',
        'requests>=2.0.0',
        'watchdog>=0.1.2',
        'ordereddict>=1.0',
        'Markdown>=2.3.0',
        'wsgiref>=0.1.2',
        'PyYAML>=3.10',
    ],
    dependency_links=[
        'http://github.com/HubSpot/snakecharmer/tarball/master#egg=snakecharmer-1.0.0',        
        ]
    ,
)
