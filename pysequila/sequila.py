"""Entrypoint to Sequila - tool for large-scale genomics on Spark."""
from pyspark.sql import SparkSession
from pyspark.sql.context import SQLContext
from pyspark.sql.dataframe import DataFrame


class SequilaSession(SparkSession):
    """Wrapper for SparkSession."""

    def __init__(self, session: SparkSession, jsparkSession=None):
        """Create a new SequilaSession."""
        SparkSession.__init__(self, session.sparkContext)
        seq_session = session._jvm.org.apache.spark.sql.SequilaSession(session._jsparkSession)  # pylint: disable=W0212

        session._jvm.org.apache.spark.sql.SequilaSession.register(seq_session)
        session._jvm.org.biodatageeks.sequila.utils.UDFRegister.register(seq_session)
        session._jvm.SequilaSession.setDefaultSession(seq_session)
        sequila_session = SequilaSession._instantiatedSession

        self._sc = sequila_session._sc
        self._jsc = self._sc._jsc
        self._jvm = session._jvm

        if jsparkSession is None:
            if (
                self._jvm.SequilaSession.getDefaultSession().isDefined()
                and not self._jvm.SequilaSession.getDefaultSession().get().sparkContext().isStopped()
            ):
                jsparkSession = self._jvm.SequilaSession.getDefaultSession().get()
            else:
                jsparkSession = self._jvm.SequilaSession(self._jsc.sc())
        self._jsparkSession = jsparkSession
        self._jwrapped = self._jsparkSession.sqlContext()
        self._wrapped = SQLContext(self._sc, self, self._jwrapped)
        if SequilaSession._instantiatedSession is None or SequilaSession._instantiatedSession._sc._jsc is None:
            SequilaSession._instantiatedSession = self
            self._jvm.SparkSession.setDefaultSession(self._jsparkSession)

    def coverage(self, path: str, refPath: str) -> DataFrame:
        """
        Create a :class:`DataFrame` with depth of coverage for a specific aligment file.

        .. versionadded:: 0.3.0
        Parameters
        ----------
        path : str
            the alignment file in BAM/CRAM format (with an index file)
        refPath : str
           the refernce file in FASTA format (with an index file)
        Returns
        -------
        :class:`DataFrame`
        Examples
        --------
        >>> ss.coverage(bam_file, ref_file).show(1)
        +------+---------+-------+---+--------+
        |contig|pos_start|pos_end|ref|coverage|
        +------+---------+-------+---+--------+
        |     1|       34|     34|  R|       1|
        +------+---------+-------+---+--------+
        only showing top 1 row
        """
        jdf = self._jsparkSession.coverage(path, refPath)
        return DataFrame(jdf, self._wrapped)

    def pileup(self, path: str, refPath: str, qual: bool) -> DataFrame:
        """
        Create a :class:`DataFrame` with pileup for a specific aligment file.

        .. versionadded:: 0.3.0
        Parameters
        ----------
        path : str
            the alignment file in BAM/CRAM format (with an index file)
        refPath : str
           the refernce file in FASTA format (with an index file)
        qual: bool, default True
            whether to include base qualities pileup in the output
        Returns
        -------
        :class:`DataFrame`
        Examples
        --------
        >>> ss.pileup(bam_file, ref_file, True).where("alts IS NOT NULL").show(1)
        +------+---------+-------+---+--------+--------+-----------+---------+--------------------+
        |contig|pos_start|pos_end|ref|coverage|countRef|countNonRef|     alts|               quals|
        +------+---------+-------+---+--------+--------+-----------+---------+--------------------+
        |     1|       69|     69|  A|       7|       6|          1|{99 -> 1}|{65 -> [0, 0, 0, ...|
        +------+---------+-------+---+--------+--------+-----------+---------+--------------------+
        only showing top 1 row

        """
        jdf = self._jsparkSession.pileup(path, refPath, qual)
        return DataFrame(jdf, self._wrapped)
