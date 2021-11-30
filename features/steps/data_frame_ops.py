# pylint: disable=missing-function-docstring,missing-module-docstring,wildcard-import,undefined-variable,function-redefined,no-else-return
import io
from contextlib import redirect_stdout

from behave import then


@then('row count is "{row_count}"')
def compare_row_count(context, row_count):
    assert len(context.result.collect()) == int(row_count)


@then('explain plan contains "{token}"')
def compare_explain_plan(context, token):
    with io.StringIO() as buf, redirect_stdout(buf):
        context.result.explain()
        explain_plan = buf.getvalue()
        assert token in explain_plan
