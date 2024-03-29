# -*- coding: utf-8 -*-
"""setup.py"""

import os
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


class Tox(TestCommand):
    user_options = [("tox-args=", "a", "Arguments to pass to tox")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import shlex

        import tox

        if self.tox_args:
            errno = tox.cmdline(args=shlex.split(self.tox_args))
        else:
            errno = tox.cmdline(self.test_args)
        sys.exit(errno)


def read_content(filepath):
    with open(filepath) as fobj:
        return fobj.read()


classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
]


long_description = read_content("README.rst") + read_content(os.path.join("docs/source", "CHANGELOG.rst"))

requires = ["setuptools", "typeguard==2.9.1", "pyspark==3.2.2", "findspark", "pandas"]

extras_require = {
    "reST": ["Sphinx"],
}
if os.environ.get("READTHEDOCS", None):
    extras_require["reST"].append("recommonmark")

setup(
    name="pysequila",
    version=os.getenv("VERSION", "0.1.0"),
    description="An SQL-based solution for large-scale genomic analysis",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author="biodatageeks",
    author_email="team@biodatageeks.org",
    url="https://biodatageeks.github.io/sequila/",
    classifiers=classifiers,
    packages=["pysequila"],
    data_files=[],
    install_requires=requires,
    include_package_data=True,
    extras_require=extras_require,
    tests_require=["tox"],
    cmdclass={"test": Tox},
)
