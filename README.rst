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

