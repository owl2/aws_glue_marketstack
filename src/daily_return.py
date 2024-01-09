import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame


def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)


args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1704401546383 = glueContext.create_dynamic_frame.from_catalog(
    database="default",
    table_name="eod_bronze",
    transformation_ctx="AWSGlueDataCatalog_node1704401546383",
)

# Script generated for node SQL Query
SqlQuery0 = """
SELECT 
    *,
    ((close - LAG(close) OVER (ORDER BY date)) / LAG(clode) OVER (ORDER BY date)) * 100 AS Daily_Return
FROM 
    eod
ORDER BY 
    date

"""
SQLQuery_node1704401671607 = sparkSqlQuery(
    glueContext,
    query=SqlQuery0,
    mapping={"eod": AWSGlueDataCatalog_node1704401546383},
    transformation_ctx="SQLQuery_node1704401671607",
)

job.commit()