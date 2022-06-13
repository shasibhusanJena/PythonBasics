
from pyspark import SparkContext

sc = SparkContext("local[*]","Demo")
sc.setLogLevel("Error")
rdd1 = sc.textFile("C:/workspace_data_engineering/week9-Apache Spark - General Purpose Cluster Computing Framework/dataset/customerorders.csv")

rdd2 = rdd1.map(lambda x: (x.split(",")[0],float(x.split(",")[2])))

rdd3 =rdd2.reduceByKey(lambda x,y : x+y)
rdd4 =rdd3.sortBy(lambda x: x[1],False)
result = rdd4.collect()
for a in result:
    print(a)