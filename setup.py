"""
SPDX-License-Identifier: MIT

Install augur package with pip.
"""
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

exec(open("metadata.py").read())

setup(
    name=__slug__,
    version=__version__,
    include_package_data=True,
    description=__short_description__,
    long_description=long_description,
    url=__url__,
    author="Derek Howard",
    author_email="derek@howderek.com",
    packages=find_packages(),
    license=__license__,
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Version Control",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
    install_requires=[
        "beaker==1.11.0",
        "click==7.1.2",
        "coloredlogs==14.0",
        "flask==1.1.2",
        "flask_cors==3.0.8",
        "gunicorn==20.0.4",
        "pandas==1.0.5",
        "psutil==5.7.2",
        "psycopg2_binary==2.8.5",
        "requests==2.24.0",
        "six==1.15.0",
        "sqlalchemy==1.3.19"
    ],
    extras_require={
        "dev": [
            "docutils==0.15",
            "ipdb==0.13.3",
            "pytest==6.0.1",
            "sphinx==3.2.1",
            "sphinx_rtd_theme==0.5.0",
            "sphinxcontrib-openapi==0.7.0",
            "sphinxcontrib-redoc==1.6.0",
            "tox==3.19.0"
        ]
    },
    entry_points={
        "console_scripts": [
            "augur=augur.cli._multicommand:run"
        ],
    }
)
