# pylint: disable=missing-function-docstring,missing-module-docstring,wildcard-import,undefined-variable,trailing-whitespace
import os

from behave import *
from pyspark.sql import SparkSession

from pysequila import SequilaSession


@given("a sequila session")
def step_sequila_session(context):
    context.spark = (
        SparkSession.builder.master("local[1]")
        .appName("SeQuiLa")
        .config("spark.jars.packages", f"org.biodatageeks:sequila_2.12:{os.getenv('SEQUILA_VERSION','0.7.3')}")
        .config("spark.driver.memory", "2g")
        .config("spark.driver.maxResultSize", "1g")
        .getOrCreate()
    )
    context.sequila = SequilaSession(context.spark)


@given("create alignment tables")
def step_create_tables(context):
    root_dir = os.getenv("PWD")
    context.sample_id = "NA12878.multichrom.md"
    context.bam_table_name = "reads_bam"
    context.bam_file = f"{root_dir}/features/data/NA12878.multichrom.md.bam"
    context.cram_file = f"{root_dir}/features/data/NA12878.multichrom.md.cram"
    context.ref_file = f"{root_dir}/features/data/Homo_sapiens_assembly18_chr1_chrM.small.fasta"
    context.sequila.sql(
        f"""
        CREATE TABLE IF NOT EXISTS {context.bam_table_name} 
        USING org.biodatageeks.sequila.datasources.BAM.BAMDataSource
        OPTIONS(path "{context.bam_file}")
        """
    )

    print(context.sequila.sql(f"DESCRIBE FORMATTED {context.bam_table_name}"))
