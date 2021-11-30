# pylint: disable=missing-function-docstring,missing-module-docstring,wildcard-import,undefined-variable,function-redefined,no-else-return

from behave import given


@given("I compute pileup with quals using SQL API")
def run_pileup_sql(context):
    context.result = context.sequila.sql(
        f"""
        SELECT * FROM pileup('{context.bam_table_name}', '{context.sample_id}', '{context.ref_file}', true, true)
    """
    )


@given("I compute pileup with quals using DataFrame API")
def run_pileup_dataframe(context):
    context.result = context.sequila.pileup(context.bam_file, context.ref_file, True)
