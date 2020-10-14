|version| |python| |license| |contributors| |last_commit|

.. |version| image:: https://badge.fury.io/py/pysequila.svg
    :target: https://badge.fury.io/py/pysequila

.. |python| image:: https://img.shields.io/badge/python-3.7-blue.svg
    :alt: Python-3.7

.. |license| image:: https://img.shields.io/badge/license-Apache%202.0-blue.svg
    :alt: license

.. |contributors| image:: https://img.shields.io/github/contributors/biodatageeks/pysequila
    :alt: GitHub contributors

.. |last_commit| image:: https://img.shields.io/github/commit-activity/m/biodatageeks/pysequila
    :alt: GitHub commit activity

===========
 pysequila
===========

pysequila is Python entrypoint to SeQuiLa, an ANSI-SQL compliant solution for efficient sequencing reads processing and genomic intervals querying built on top of Apache Spark. Range joins, depth of coverage and pileup computations are bread and butter for NGS analysis but the high volume of data make them execute very slowly or even failing to compute.


Requirements
============

* Python 3.7

Features
========

* custom data sources for bioinformatics file formats (BAM, CRAM, VCF)
* depth of coverage calculations 
* pileup calculations
* reads filtering
* efficient range joins
* other utility functions 

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
  >>> from pyspark.sql import SparkSession
  >>> spark = SparkSession \
      .builder \
      .appName(f'{app_name}') \
      .getOrCreate()
  >>> from sequila import SequilaSession
  >>> ss = SequilaSession(spark)
  >>> ss.sql ("SELECT * FROM  coverage('reads', 'NA12878'")
  >>>

