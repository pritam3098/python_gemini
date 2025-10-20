#spark-submit "/Users/pritamverma/Documents/vscode/python project/data_clean_pysprak.py" -- to run the code

from pyspark.sql import SparkSession
from pyspark.sql.functions import col,to_date,initcap,sum as sum_

spark=SparkSession.builder.appName("simpleClean").getOrCreate()

# 2. Add this line to reduce the log noise
# "WARN" ya "ERROR" ka use karein
spark.sparkContext.setLogLevel("Error")
sales_data = [
    (101, "2025-10-01", "Laptop", "Electronics", "900.50", 1, "New York"),
    (102, "2025-10-01", "Mouse", "Electronics", "25.00", 2, "new york"),
    (103, "2025-10-02", "Book", "Books", "15.75", 5, "London"),
    (104, "2025-10-02", "T-Shirt", "Apparel", "30.00", None, "Tokyo"),
    (105, "2025-10-03", "Book", None, "12.00", 3, "London"),
    (106, "2025-10-04", "Keyboard", "Electronics", "75.00", 1, "New York")
]

schema = ["transaction_id", "transaction_date", "product_name", "category", "price", "quantity", "city"]

df=spark.createDataFrame(data=sales_data,schema=schema)
df.show()
df.printSchema()

df_casted=df.withColumn("price",col("price").cast("float"))\
            .withColumn("quantity",col("quantity").cast("integer"))\
            .withColumn("transactiondate",to_date(col("transaction_date"),"yyyy-MM-dd"))

# 3. Handle Missing Values using .na.fill()
# Fill missing quantities with a default value of 1
# Fill missing categories with 'Unknown'

df_filled=df_casted.na.fill({'quantity':1,'category':'Unknown'})

# 4. Standardize Text Data
# Use initcap to make city names consistent (e.g., 'new york' -> 'New York')

df_standardized=df_filled.withColumn("city",initcap(col("city")))

# 5. Create a New Column
df_with_total=df_standardized.withColumn("total_sales",col("price")*col("quantity"))

print("\n final cleaned data \n")

df_with_total.show()
df_with_total.printSchema()

# 6. Basic Analysis: Calculate total sales per city

sales_by_city=df_with_total.groupBy("city").agg(sum_("total_sales").alias("total_sales_in_city"))
print("\n--- Analysis: Total Sales by City ---")
sales_by_city.show()

print("\n--- Analysis: Total Sales by City lowest to highest---")
# Ab hum sales_by_city DataFrame ko sort kareng
sorted_sales=sales_by_city.sort(col("total_sales_in_city").asc())
sorted_sales.show()

# Filter the results to show only cities with total sales greater than 100
print("\n--- Filtered Analysis (Sales > 100) ---")

lowest_sales_cities=sorted_sales.filter(col("total_sales_in_city")<114)
lowest_sales_cities.show()


spark.stop()