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

pysequila is a Python entrypoint to SeQuiLa, an ANSI-SQL compliant solution for efficient sequencing reads processing and genomic intervals querying built on top of Apache Spark. Range joins, depth of coverage and pileup computations are bread and butter for NGS analysis but the high volume of data make them execute very slowly or even failing to compute.


Requirements
============

* Python 3.7, 3.8, 3.9

Features
========

* custom data sources for bioinformatics file formats (BAM, CRAM, VCF)
* depth of coverage calculations 
* pileup calculations
* reads filtering
* efficient range joins
* other utility functions
* support for both SQL and Dataframe/Dataset API

Building
=====

::

  $ python3.9 -m venv .venv
  $ source .venv/bin/activate
  $ pip install -r requirements.txt
  $ python setup.py sdist bdist_wheel

Install
=====

::

  $ python -m pip install --user pysequila
  or
  (venv)$ python -m pip install pysequila

Usage
=====

::

  $ python
  >>> import os
  >>> from pysequila import SequilaSession
  >>> curr_dir = os.getcwd()
  >>> ss = SequilaSession \
    .builder \
    .config("spark.jars.packages", "org.biodatageeks:sequila_2.12:1.3.6") \
    .config("spark.driver.memory", "2g") \
    .getOrCreate()
  >>> ss.sql(f"""
        CREATE TABLE IF NOT EXISTS reads
        USING org.biodatageeks.sequila.datasources.BAM.BAMDataSource
        OPTIONS(path "{curr_dir}/features/data/NA12878.multichrom.md.bam")
        """)
  >>> df = ss.sql (f"SELECT * FROM  coverage('reads', 'NA12878','{curr_dir}/features/data/Homo_sapiens_assembly18_chr1_chrM.small.fasta')")
  >>> # or using DataFrame/DataSet API
  >>> df = ss.coverage(f"{curr_dir}/features/data/NA12878.multichrom.md.bam", "{curr_dir}/features/data/Homo_sapiens_assembly18_chr1_chrM.small.fasta")

