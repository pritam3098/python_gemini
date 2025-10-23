from pyspark.sql import *
from pyspark.sql.functions import *

spark=SparkSession.builder.appName("practice").getOrCreate()
spark.sparkContext.setLogLevel("Error")

# Yeh data ek Python list of dictionaries hai
raw_employee_data = [
    {"emp_id": "101", "name": "Pritam Verma", "department": "Engineering", "salary": " 75000", "join_date": "2022-01-15", "status": "Full-Time"},
    {"emp_id": "102", "name": "Alex Johnson", "department": "engineering", "salary": "80000", "join_date": "2022/03/10", "status": "Full-Time"},
    {"emp_id": "103", "name": "Sonia Gupta", "department": "Sales", "salary": "60000", "join_date": "2023-05-20", "status": "Part-Time"},
    {"emp_id": "104", "name": "Rahul Sharma", "department": "Sales", "salary": "62000", "join_date": "2023-02-18", "status": "full-time"},
    {"emp_id": "105", "name": "Meera Das", "department": "Marketing", "salary": "55000", "join_date": "2022-07-30", "status": "Part-Time"},
    {"emp_id": "106", "name": "John Doe", "department": "HR", "salary": " ", "join_date": "2023-11-01", "status": "Contract"},
    {"emp_id": "107", "name": "Jane Smith", "department": "Engineering", "salary": "78000", "join_date": "2024-01-10", "status": "Full-Time"},
    {"emp_id": "108", "name": "Anil Kumar", "department": "Finance", "salary": "90000", "join_date": "2021-12-05", "status": None},
    {"emp_id": "109", "name": "Priya Singh", "department": "Marketing", "salary": "58000", "join_date": "2023-06-15", "status": "part-time"},
    {"emp_id": "109", "name": "Priya Singh", "department": "Marketing", "salary": "58000", "join_date": "2023-06-15", "status": "part-time"},
    {"emp_id": "110", "name": "Robert Brown", "department": "sales", "salary": "61000", "join_date": "2024-02-20", "status": "Full-Time"}
]



df=spark.createDataFrame(data=raw_employee_data)
df.show()

print("\n remove duplicates from empid \n")
remove_duplicate=df.dropDuplicates(["emp_id"])
remove_duplicate.show()

print("\n replace status to unknown \n")
replace_df=remove_duplicate.na.fill({'status':"Unknown"})
replace_df.show()

print("\n replace salary null value to none and also change the datatype of the salary column")
replace_df=replace_df.withColumn("salary",when (trim(col("salary"))=="",None).otherwise(col("salary")))
replace_df=replace_df.withColumn("salary",col("salary").cast("integer"))
replace_df.show()
replace_df.printSchema()

# Date ko handle karna (coalesce alag-alag formats ko try karta hai)
timestamp_df=replace_df.withColumn("join_date", 
    expr(
        """
case when join_date RLIKE '^[0-9]{4}-[0-9]{2}-[0-9]{2}$'
then to_date(join_date,'yyyy-MM-dd')
     WHEN join_date RLIKE '^[0-9]{4}/[0-9]{2}/[0-9]{2}$' 
                THEN to_date(join_date, 'yyyy/MM/dd')
            WHEN join_date RLIKE '^[0-9]{2}-[0-9]{2}-[0-9]{4}$' 
                THEN to_date(join_date, 'dd-MM-yyyy')
            ELSE NULL
        END

"""
    )
)
timestamp_df.show()

cap_df=timestamp_df.withColumn("department",initcap(col("department")))
cap_df.show()

exp_year=cap_df.withColumn("experience_years",int('2025')-year(col("join_date"))).withColumn("bonus",when(col("department")=="Sales",col("salary")*0.50)\
                                                                                             .otherwise(col("salary")*0.10)).na.drop(subset=["salary"])
exp_year.show()



spark.stop()