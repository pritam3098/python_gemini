#spark-submit "/Users/pritamverma/Documents/vscode/python project/pysparj_project4.py" -- to run the code

from pyspark.sql import SparkSession,Window
from pyspark.sql.functions import *

spark=SparkSession.builder.appName("Retail_pipline").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
spark.sparkContext.setLogLevel("WARN")
transaction_df=spark.read.csv("file:///Users/pritamverma/Documents/vscode/python project/transaction.csv",header=True,inferSchema=True,nullValue='NULL')
customer_df=spark.read.csv("file:///Users/pritamverma/Documents/vscode/python project/customers1.csv",header=True,inferSchema=True,nullValue='NULL')

print("---Transaction data------")
transaction_df.show()
print("---customer data------")
customer_df.show()

print("---remove duplicate from transaction------")
cleaned_df=transaction_df.dropDuplicates()
cleaned_df.show()

print("---remove null and trim and lower the description column from transaction------")
cleaned_df=cleaned_df.na.drop(subset=['Description','Country']).withColumn('Description',lower(trim(col('Description'))))
cleaned_df.show()

print(" remove the negative and zero value from the transactions")
cleaned_df=cleaned_df.filter((col('Quantity')>0) & (col('UnitPrice')>0))
cleaned_df.show(truncate=False)

print("--- Transformed df converting Quantity into integer, unitprice as float , change format of timestamp----")

transformed_df=cleaned_df.withColumn("Quantity",col("Quantity").cast("integer"))\
                         .withColumn("UnitPrice",col('UnitPrice').cast('float'))\
                         .withColumn("InvoiceDate",to_timestamp(col("InvoiceDate"),"M/d/yyyy H:mm"))

transformed_df.show(truncate=False)

print("-- calculate the total cost, invoice year and invoice month")

feature_df=transformed_df.withColumn("Total_cost",col("Quantity")*col("UnitPrice"))\
                         .withColumn("Invoice_year",year(col("InvoiceDate")))\
                         .withColumn("Invoice_month",month(col("InvoiceDate")))

feature_df.show()

print("--joining the datasets---")
joining_df=feature_df.join(customer_df,on="customerID",how="left").withColumnRenamed("Description","Product_Description")
joining_df.show(truncate=False)

print("\n--- Aggregating Data for Insights ---")

monthly_sales=joining_df.groupBy("Invoice_year","Invoice_month").agg(sum("Total_cost").alias("Total_sales")).orderBy(desc("Total_sales"))
monthly_sales.show()

print("Top 10 customers")
monthly_sales.show(10)




spark.stop()