from pyspark.sql import SparkSession

if __name__ == "__main__" :
    print("Application Started")

    spark = SparkSession.\
        builder.\
        appName("First Pyspark Demo").\
        master("local[*]").\
        getOrCreate()