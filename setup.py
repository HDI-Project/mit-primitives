#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup


install_requires = [
    'd3m==2018.7.10',
    'mlblocks==0.1.7',
]

tests_require = [
    'pytest>=3.4.2',
]

setup_requires = [
    'pytest-runner>=2.11.1',
]

development_requires = [
    'autoflake>=1.1',
    'autopep8>=1.3.5',
    'bumpversion>=0.5.3',
    'flake8>=3.5.0',
    'isort>=4.3.4',
    'pip>=10.0.1',
    'pycodestyle==2.3.1',
    'pyflakes==1.6.0',
]

extras_require = {
    'test': tests_require,
    'dev': tests_require + development_requires
}

entry_points = {
    'd3m.primitives': [
        'mit_primitives.Learner = mit_primitives.learner:Learner',
    ]
}

setup(
    author='MIT Data To AI Lab',
    author_email='dailabmit@gmail.com',
    description="MIT DAI-Lab TA1 primitives",
    entry_points=entry_points,
    extras_require=extras_require,
    include_package_data=True,
    install_requires=install_requires,
    keywords='d3m_primitive',
    license="MIT license",
    name='mit-primitives',
    packages=find_packages(include=['mit_primitives', 'mit_primitives.*']),
    setup_requires=setup_requires,
    version='0.0.2',
    zip_safe=False,
)
