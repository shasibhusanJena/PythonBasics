from pyspark import SparkConf
from pyspark.sql import SparkSession

my_conf = SparkConf()
my_conf.set("spark.app.name","Demo")
my_conf.set("spark.master","local[*]")

spark = SparkSession.builder.config(conf=my_conf).getOrCreate()
order_df = spark\
    .read\
    .option("header",True)\
    .option("inferSchema",True)\
    .csv("C:/workspace_data_engineering/Week11-Apache Spark Structured API Part-1/dataset/orders-201019-002101.csv")

order_df.printSchema()
order_df.show()