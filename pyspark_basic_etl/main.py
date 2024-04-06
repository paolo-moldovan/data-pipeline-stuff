from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("Local ETL").getOrCreate()

input_df = spark.read.csv("inputs/example_input_data.csv", header=True, inferSchema=True)

transformed_df = input_df.withColumn("full_name", F.concat(F.col("name"), F.lit(" "), F.col("surname")))

transformed_df.write.csv("outputs/transformed_data", header=True)

spark.stop()
