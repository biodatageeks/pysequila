# pylint: disable=missing-function-docstring,missing-module-docstring,wildcard-import,undefined-variable
import os

from behave import *
from pyspark.sql import SparkSession

from pysequila import SequilaSession


@given("a sequila session")
def step_impl(context):
    context.spark = (
        SparkSession.builder.master("local[1]")
        .appName("SeQuiLa")
        .config("spark.jars.packages", f"org.biodatageeks:sequila_2.12:{os.getenv('SEQUILA_VERSION','0.7.3')}")
        .config("spark.driver.memory", "2g")
        .config("spark.driver.maxResultSize", "1g")
        .getOrCreate()
    )
    context.sequila = SequilaSession(context.spark)
