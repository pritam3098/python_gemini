#spark-submit --jars /Users/pritamverma/postgresql-42.6.0.jar "/Users/pritamverma/Documents/vscode/python project/pyspark_with_sql.py"
from pyspark.sql import *
from pyspark.sql.functions import *

spark=SparkSession.builder.appName("SQL using pyspark").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

jdbc_url="jdbc:postgresql://localhost:5432/source_db"
conn_properties={
    "user":"pritamverma",
    "password":"12345",
    "driver":"org.postgresql.Driver"
}

table_name="orders"

df=spark.read.jdbc(url=jdbc_url,table=table_name,properties=conn_properties)
df.show(truncate=False)

df_count=df.select("status").count()
print(df_count)

status_count=df.groupBy("status").count()
status_count.show()
spark.stop()