#spark-submit "/Users/pritamverma/Documents/vscode/python project/data_clean_pysprak.py" -- to run the code


from pyspark.sql import SparkSession
from pyspark.sql.functions import *
spark=SparkSession.builder.appName("ETL sales and customers").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
# Load the CSV file into a DataFrame
# header=True tells Spark the first row is the column names
# inferSchema=True tells Spark to guess the data types
#Aapko Spark ko CSV padhte waqt hi batana hoga ki jahan bhi 'NULL' likha hai, use ek asli null value samjhe. Iske liye aap nullValue option ka use kar sakte hain.
sales_df=spark.read.csv("file:///Users/pritamverma/Documents/vscode/python project/sales_1.csv",header=True,inferSchema=True,nullValue='NULL')
customer_df=spark.read.csv("file:///Users/pritamverma/Documents/vscode/python project/customers.csv",header=True,inferSchema=True,nullValue='NULL')
sales_df.show()
customer_df.show()

print("--- Cleaning Sales Data ---")

cleaned_df=sales_df.dropDuplicates(["order_id"]).na.drop(subset=['price','quantity']).withColumn('product_name',lower(trim(col('product_name'))))
print("Sales data after cleaning duplicates, nulls, and strings:")
cleaned_df.show()

print("--- Transforming Sales Data ---")

transformed_df=cleaned_df.withColumn('total_sales',col('price')*col('quantity'))\
.withColumnRenamed('transaction_date','sales_date')\
.withColumn('sale_category',
            when (col('total_sales')>90000 , 'High sales')\
            .otherwise('Lower sales')
)

transformed_df.show()

print("--- Joining Sales and Customer Data ---")

joining_df=transformed_df.join(customer_df,on='customer_id',how='left')
joining_df.show()

print("--- Aggregating Data for Insights ---")

sales_per_city=joining_df.groupBy('city').agg(sum('total_sales').alias('total_sales_in_city'),count('order_id').alias('order_count'))\
    .orderBy(desc('total_sales_in_city'))

sales_per_city.show()

final_report_df=joining_df.select(
    "order_id",
    "customer_name",
    "city",
    "product_name",
    "total_sales",
    "sale_category"
)
print("Final Report View:")
final_report_df.show()

print("--- Saving Final Report to Parquet ---")
# Parquet is a highly efficient format for big data
final_report_df.write.mode("overwrite").parquet("file:///Users/pritamverma/Documents/vscode/python project/sales_report_output.csv")
