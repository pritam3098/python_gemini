from pyspark.sql import SparkSession
from pyspark.sql.functions import col,sum,trim,lower,avg,desc

spark=SparkSession.builder.appName("data cleaning").getOrCreate()

# Set log level to ERROR to reduce console noise
spark.sparkContext.setLogLevel("ERROR")

# Load the CSV file into a DataFrame
# header=True tells Spark the first row is the column names
# inferSchema=True tells Spark to guess the data types
#Aapko Spark ko CSV padhte waqt hi batana hoga ki jahan bhi 'NULL' likha hai, use ek asli null value samjhe. Iske liye aap nullValue option ka use kar sakte hain.

df=spark.read.csv("file:///Users/pritamverma/Documents/vscode/python project/sales.csv",header=True,inferSchema=True,nullValue='NULL')

print("\n Raw data and context \n")
df.printSchema()
df.show()

print("\n cleaned data \n")
cleaned_df=df.withColumn("price",trim(col("price"))).withColumn("city",lower(col("city")))

cleaned_df.show()
print("\n filled null values \n")
filled_df=cleaned_df.na.fill({
    'quantity':0,
    'category':'unknown'}
    )
filled_df.show()

print("\n casting col \n")
final_df=filled_df.withColumn("price",col("price").cast('double'))
final_df.show()

print("\n Add new col \n")
final_df1=final_df.withColumn("total_sales",col("price")*col("quantity"))

print("\n cleaned and transformed data \n")
final_df1.show()

top_customers=final_df1.groupBy('customer_id').agg(sum('total_sales').alias('total_spent')).orderBy(desc('total_spent'))

top_customers.show()

avg_customers=final_df1.groupBy('customer_id').agg(avg('total_sales').alias('avg_spent')).orderBy(desc('avg_spent'))
avg_customers.show()