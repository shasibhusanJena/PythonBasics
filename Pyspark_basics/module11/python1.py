from sys import stdin
from pyspark import SparkContext, StorageLevel

## using spark-submit we can execute this file  too
## spark-submit C:\workspace_python_basic\PythonBasics\Pyspark_basics\module11\python1.py
## this example is to show an example for the . persist and cache and then execute using spark- submit example
## get the premium customer pending more the 5000
sc = SparkContext("local[*]","Premium customer")

base_rdd = sc.textFile("C:/workspace_data_engineering/week9-Apache Spark - General Purpose Cluster Computing Framework/dataset/customerorders.csv")

mapped_input = base_rdd.map(lambda x: (x.split(",")[0],float(x.split(",")[2])))
total_by_customer =mapped_input.reduceByKey(lambda x,y : x+y)

# put filter to get total more then 5000
premium_customer =total_by_customer.filter(lambda x:x[1]>5000)

# then we want to multiple by 2 total amount
doubled_amount =premium_customer.map(lambda x : (x[0],x[1]*2)).persist(storageLevel=StorageLevel.MEMORY_ONLY)

results = doubled_amount.collect()

for x in results:
    print(x)

stdin.readline()