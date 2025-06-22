from pyspark.context import SparkContext
from awsglue.context import GlueContext
import json
import os

# Local param file path
param_file_path = os.path.join("config", "job_params.json")

# Read parameters from local file
with open(param_file_path, "r") as f:
    params = json.load(f)

# Access parameters
name = params["name"]
age = params["age"]

# Initialize Spark and Glue Contexts
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Use parameters in logic
df = spark.createDataFrame([{"name": name, "age": age}])
print("🔥 Hello from Spark in Glue 5 (Local Mode)!")
df.show()


print("this is a change test to overwrite docker image!!!!!!!!!!")