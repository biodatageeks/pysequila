# pylint: disable=missing-function-docstring,missing-module-docstring,wildcard-import,undefined-variable,function-redefined,no-else-return

from behave import given, then


@given("I compute coverage")
def run_coverage(context):
    context.sequila.sparkContext.setLogLevel("INFO")
    context.result = context.sequila.sql(
        f"""
        SELECT * FROM coverage('{context.bam_table_name}', '{context.sample_id}', '{context.ref_file}')
    """
    ).collect()


@then('row count is "{row_count}"')
def compare_row_count(contex, row_count):
    assert len(contex.result) == int(row_count)
