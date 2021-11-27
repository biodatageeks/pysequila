# pylint: disable=missing-function-docstring,missing-module-docstring,wildcard-import,undefined-variable,function-redefined,no-else-return


def before_feature(context, feature):
    if "setup_tables" in feature.tags:
        context.execute_steps(
            """
            Given a sequila session
             create alignment tables
        """
        )
