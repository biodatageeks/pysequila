"""Entrypoint to Sequila - tool for large-scale genomics on Spark."""
from pyspark.sql import SparkSession
from pyspark.sql.context import SQLContext
from typeguard import check_argument_types


def register(session: SparkSession):
    """
    Register SQL extensions for a Spark session.

    :param session: Spark session
    """
    assert check_argument_types()
    # pylint: disable=W0212
    spark_session = session._jvm\
        .org.apache.spark.sql.SparkSession\
        .builder().enableHiveSupport().getOrCreate()

    seq_session = session._jvm \
        .org.apache.spark.sql \
        .SequilaSession(spark_session)

    session._jvm \
        .org.biodatageeks.sequila.utils \
        .SequilaRegister.register(seq_session)
    session._jvm \
        .org.biodatageeks.sequila.utils \
        .UDFRegister.register(seq_session)


class SequilaSession (SparkSession):
    """Wrapper for SparkSession."""

    def __init__(self, session: SparkSession, jsparkSession=None):
        """Create a new SequilaSession."""
        SparkSession.__init__(self, session.sparkContext)
        seq_session = session._jvm\
            .org.apache.spark.sql\
            .SequilaSession(session._jsparkSession)  # pylint: disable=W0212

        session._jvm\
            .org.biodatageeks.sequila.utils\
            .SequilaRegister.register(seq_session)
        session._jvm\
            .org.biodatageeks.sequila.utils\
            .UDFRegister.register(seq_session)
        session._jvm\
            .SequilaSession.setDefaultSession(seq_session)
        sequila_session = SequilaSession._instantiatedSession

        self._sc = sequila_session._sc
        self._jsc = self._sc._jsc
        self._jvm = session._jvm

        if jsparkSession is None:
            if self._jvm.SequilaSession.getDefaultSession().isDefined() \
                    and not self._jvm\
                    .SequilaSession.getDefaultSession().get() \
                    .sparkContext().isStopped():
                jsparkSession = self._jvm\
                    .SequilaSession.getDefaultSession().get()
            else:
                jsparkSession = self._jvm.SequilaSession(self._jsc.sc())
        self._jsparkSession = jsparkSession
        self._jwrapped = self._jsparkSession.sqlContext()
        self._wrapped = SQLContext(self._sc, self, self._jwrapped)
        if SequilaSession._instantiatedSession is None \
                or SequilaSession._instantiatedSession._sc._jsc is None:
            SequilaSession._instantiatedSession = self
            self._jvm.SparkSession.setDefaultSession(self._jsparkSession)
