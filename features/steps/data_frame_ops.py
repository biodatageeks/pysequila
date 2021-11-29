# pylint: disable=missing-function-docstring,missing-module-docstring,wildcard-import,undefined-variable,function-redefined,no-else-return

from behave import then


@then('row count is "{row_count}"')
def compare_row_count(contex, row_count):
    assert len(contex.result) == int(row_count)
