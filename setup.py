#! /usr/bin/python3
# -*- coding: utf-8 -*-

from setuptools import setup
requirements = open("requirements.txt")
require = requirements.readline()

setup(name="ressources",
      version="0.0.1",
      description="A program to interact with the database of the UPC Roubaix",
      author="Xorielle",
      packages=["BDD Test"],
      install_requires=[require],
      setup_requires=[require],
      extras_require={},
      license="GPL 3.0")