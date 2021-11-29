|version| |downloads| |version_sequila| |build| |python| |license| |coverage| |contributors| |last_commit|

.. |version| image:: https://badge.fury.io/py/pysequila.svg
    :target: https://badge.fury.io/py/pysequila

.. |version_sequila| image:: https://img.shields.io/maven-central/v/org.biodatageeks/sequila_2.12
    :alt: Maven Central

.. |build| image:: https://gitlab.com/biodatageeks/pysequila/badges/master/pipeline.svg
    :alt: status

.. |python| image:: https://img.shields.io/badge/python-3.8-blue.svg
    :alt: Python-3.8

.. |license| image:: https://img.shields.io/badge/license-Apache%202.0-blue.svg
    :alt: license

.. |coverage| image:: https://gitlab.com/biodatageeks/pysequila/badges/master/coverage.svg
    :alt: coverage

.. |contributors| image:: https://img.shields.io/github/contributors/biodatageeks/pysequila
    :alt: GitHub contributors

.. |last_commit| image:: https://img.shields.io/github/commit-activity/m/biodatageeks/pysequila
    :alt: GitHub commit activity

.. |downloads| image:: https://pepy.tech/badge/pysequila
    :alt: PyPI downloads


===========
 pysequila
===========

pysequila is Python entrypoint to SeQuiLa, an ANSI-SQL compliant solution for efficient sequencing reads processing and genomic intervals querying built on top of Apache Spark. Range joins, depth of coverage and pileup computations are bread and butter for NGS analysis but the high volume of data make them execute very slowly or even failing to compute.


Requirements
============

* Python 3.7, 3.8

Features
========

* custom data sources for bioinformatics file formats (BAM, CRAM, VCF)
* depth of coverage calculations 
* pileup calculations
* reads filtering
* efficient range joins
* other utility functions
* support for both SQL and Dataframe/Dataset API

Setup
=====

::

  $ python -m pip install --user pysequila
  or
  (venv)$ python -m pip install pysequila

Usage
=====

::

  $ python
  >>> from pysequila import SequilaSession
  >>> ss = SequilaSession \
    .builder \
    .config("spark.driver.memory", "2g") \
    .getOrCreate()
  >>> ss.sql ("SELECT * FROM  coverage('reads', 'NA12878'")
  >>>

