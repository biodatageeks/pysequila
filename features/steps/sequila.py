# pylint: disable=missing-function-docstring,missing-module-docstring,wildcard-import,undefined-variable,trailing-whitespace
import os

from behave import *

from pysequila import SequilaSession

root_dir = os.getenv("PWD")


@given("a sequila session")
def step_sequila_session(context):
    context.sequila = (
        SequilaSession.builder.master("local[1]")
        .appName("SeQuiLa")
        .config("spark.driver.memory", "4g")
        .config("spark.driver.maxResultSize", "1g")
        .getOrCreate()
    )
    context.sequila.sparkContext.setLogLevel("ERROR")


@given("create alignment tables")
def step_create_tables(context):
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


@given("create target table")
def step_create_target_table(context):
    context.target_table_name = "targets"
    context.target_file = f"{root_dir}/features/data/targets.bed"
    context.sequila.sql(
        f"""
        CREATE TABLE IF NOT EXISTS {context.target_table_name} 
        USING org.biodatageeks.sequila.datasources.BED.BEDDataSource
        OPTIONS(path "{context.target_file}")
        """
    )
