# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()


setup(name='SeamlessPy',
      version='0.1.0',
      description='Library for working with Seamlessweb',
      long_description=readme,
      author='Patrick Britz',
      author_email='patrick.g.britz@gmail.com',
      license=license,
      packages=find_packages(exclude=('tests', 'docs')),
      zip_safe=False,
      install_requires=[
          'certifi==2019.3.9',
          'chardet==3.0.4',
          'idna==2.8',
          'requests==2.22.0',
          'urllib3==1.25.2'
      ]
      )
