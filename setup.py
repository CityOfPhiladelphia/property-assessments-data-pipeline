#!/usr/bin/eng python

from distutils.core import setup

setup(
    name='phl-property',
    version='1.0.0',
    packages=['phl_property'],
    scripts=['bin/phl-properties',
             'bin/phl-assessment-history',
             'bin/phl-building-codes',
             'bin/phl-off-property',
             'bin/phl-street-codes'],
)
