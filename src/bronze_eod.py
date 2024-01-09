import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Amazon S3
AmazonS3_node1703195967250 = glueContext.create_dynamic_frame.from_options(
    format_options={"jsonPath": "$.data.*", "multiline": False},
    connection_type="s3",
    format="json",
    connection_options={"paths": ["s3://lmu-marketstack-poc/bronze/"], "recurse": True},
    transformation_ctx="AmazonS3_node1703195967250",
)

# Script generated for node Amazon S3
AmazonS3_node1703196026449 = glueContext.getSink(
    path="s3://lmu-marketstack-poc/silver/eod/symbol=AAPL/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=["symbol", "date"],
    compression="snappy",
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1703196026449",
)
AmazonS3_node1703196026449.setCatalogInfo(
    catalogDatabase="default", catalogTableName="eod_bronze"
)
AmazonS3_node1703196026449.setFormat("glueparquet")
AmazonS3_node1703196026449.writeFrame(AmazonS3_node1703195967250)
job.commit()