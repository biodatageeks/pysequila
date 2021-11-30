# pylint: disable=missing-function-docstring,missing-module-docstring,wildcard-import,undefined-variable,trailing-whitespace
from behave import given


@given("I compute interval join using SQL API")
def run_interval_join_sql(context):
    context.result = context.sequila.sql(
        f"""
        SELECT distinct  {context.bam_table_name}.contig FROM {context.bam_table_name} JOIN {context.target_table_name} ON 
        (
          {context.target_table_name}.contig={context.bam_table_name}.contig
          AND
          {context.bam_table_name}.pos_end >= {context.target_table_name}.pos_start
          AND
          {context.bam_table_name}.pos_start <= {context.target_table_name}.pos_end
        )
    """
    )


@given("I compute interval join using Dataframe API")
def run_interval_join_dataframe(context):
    reads_df = context.sequila.sql(
        f"""
        SELECT * FROM {context.bam_table_name}
        """
    )

    targets_df = context.sequila.sql(
        f"""
        SELECT * FROM {context.target_table_name}
        """
    )

    context.result = (
        reads_df.join(
            targets_df,
            (reads_df.contig == targets_df.contig)
            & (reads_df.pos_end >= targets_df.pos_start)
            & (reads_df.pos_start <= targets_df.pos_end),
        )
        .select(reads_df.contig)
        .distinct()
    )
