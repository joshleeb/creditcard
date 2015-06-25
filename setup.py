import os
from setuptools import setup


short_description = 'Module to validate, generate and determine the format of credit card numbers.'

setup(
    name='CreditCard',
    version='1.0.0',
    author='Josh Leeb-du Toit',
    author_email='josh.leebdutoit@gmail.com',
    description=short_description,
    license='MIT',
    keywords='credit card generate validate numbers',
    url='https://github.com/joshleeb/creditcard',
    packages=['creditcard', 'tests'],
    classifiers=[
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
    ],
)
