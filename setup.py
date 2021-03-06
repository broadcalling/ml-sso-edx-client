import os
from os.path import join, dirname, split
from setuptools import setup, find_packages


with open('requirements.txt', 'r') as f:
    requirements = f.readlines()


setup(
    name='ml_sso_edx_client',
    version='1.0',
    description='Client OAuth2 from edX installations',
    author='edX',
    url='https://github.com/raccoongang/ml-sso-edx-client',
    
    install_requires=requirements,
    packages=find_packages(exclude=['tests']),
)
