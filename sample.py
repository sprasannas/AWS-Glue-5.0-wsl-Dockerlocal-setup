from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions

import sys
import os
import json

# -------------------------------
# Read parameters from local file
# -------------------------------
param_file_path = os.path.join("config", "job_params.json")
with open(param_file_path, "r") as f:
    params = json.load(f)

# Example parameters
name = params.get("name", "Unknown")
age = params.get("age", 0)

# -------------------------------
# AWS Glue boilerplate setup
# -------------------------------
#args = getResolvedOptions(sys.argv, ['JOB_NAME'])
args = {'JOB_NAME': 'test_job'}

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# -------------------------------
# Main ETL Logic
# -------------------------------
print("🔥 Hello from Spark in Glue 5 (Local Mode)!")

df = spark.createDataFrame([{"name": name, "age": age}])
df.show()

# -------------------------------
# Commit the job (important in Glue)
# -------------------------------
job.commit()



