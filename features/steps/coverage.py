# pylint: disable=missing-function-docstring,missing-module-docstring,wildcard-import,undefined-variable,function-redefined,no-else-return

from behave import given, then


@given("I compute coverage using SQL API")
def run_coverage_sql(context):
    context.result = context.sequila.sql(
        f"""
        SELECT * FROM coverage('{context.bam_table_name}', '{context.sample_id}', '{context.ref_file}')
    """
    ).collect()


@then('row count is "{row_count}"')
def compare_row_count(contex, row_count):
    assert len(contex.result) == int(row_count)


@given("I compute coverage using DataFrame API")
def run_coverage_dataframe(context):
    context.result = context.sequila.coverage(context.bam_file, context.ref_file).collect()
