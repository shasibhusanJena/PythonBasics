from pyspark import SparkConf
from pyspark.sql import SparkSession

## repartition and where clause new ly added on top of python3 file
my_conf = SparkConf()
my_conf.set("spark.app.name","Demo")
my_conf.set("spark.master","local[*]")

spark = SparkSession.builder.config(conf=my_conf).getOrCreate()
order_df = spark\
    .read\
    .option("header",True)\
    .option("inferSchema",True)\
    .csv("C:/workspace_data_engineering/Week11-Apache Spark Structured API Part-1/dataset/orders-201019-002101.csv")

group_df =order_df\
    .repartition(4)\
    .where("order_customer_id >10000")\
    .select("order_id" , "order_customer_id")\
    .groupBy("order_customer_id").count()

group_df.printSchema()
group_df.show()