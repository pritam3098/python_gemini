from pyspark.sql import *
from pyspark.sql.functions import *

spark=SparkSession.builder.appName("window_funs").getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

data = [
    ("Math", "Alice", 90), ("Math", "Ben", 85),
    ("Math", "Charlie", 90), ("History", "Alice", 88),
    ("History", "Ben", 95), ("History", "Charlie", 88)
]
columns = ["Subject", "Student", "Score"]
df = spark.createDataFrame(data, columns)

df.show()

subject_window=Window.partitionBy("Subject").orderBy("Score")

print("--Row number-----")
df_row_number=df.withColumn("row_number",row_number().over(subject_window))
df_row_number.show()

print("---rank---")
df_rank=df.withColumn("rank",rank().over(subject_window))
df_rank.show()

print("--dense rank---")
df_dense_rank=df.withColumn("dense_rank",dense_rank().over(subject_window))
df_dense_rank.show()

print("---lead function---")
df_lead_fun=df.withColumn("score_after",lead("Score",1).over(subject_window))
df_lead_fun.show()

print("---lag function---")
df_lag_fun=df.withColumn("score_before",lag("Score",1).over(subject_window))
df_lag_fun.show()


spark.stop()
