from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark=SparkSession.builder.appName("json data").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

df=spark.read.json("file:///Users/pritamverma/Documents/vscode/codes/python_gemini/pyspark projects/simple_data.json")

df.show()

df_agg=df.groupBy("city").agg(sum(col("age")).alias("sumOfAges"),avg(col("age")).alias("avgOfAges")).orderBy(desc("sumOfAges"))
df_agg.show()
spark.stop()

