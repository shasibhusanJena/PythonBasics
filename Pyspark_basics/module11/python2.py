from pyspark import SparkContext
from sys import stdin
sc = SparkContext("local[*]","demo")
rating_rdd = sc.textFile("C:/workspace_data_engineering/Week11-Apache Spark Structured API Part-1/dataset/ratings-201019-002101.dat")
mapped_rdd = rating_rdd.map(lambda x: (x.split("::")[1],x.split("::")[2]))
new_mapped_rdd =mapped_rdd.mapValues(lambda x: (float(x),1.0))
reduce_rdd = new_mapped_rdd.reduceByKey(lambda x,y : (x[0]+y[0],x[1]+y[1]))
filtered_rdd = reduce_rdd.filter(lambda x:x[1][0] > 1000)
final_rdd = filtered_rdd.mapValues(lambda x: x[0]/x[1]).filter(lambda x:x[1] >4.5)

movies_rdd = sc.textFile("C:/workspace_data_engineering/Week11-Apache Spark Structured API Part-1/dataset/movies-201019-002101.dat")
movies_mapped_rdd = movies_rdd.map(lambda x: (x.split("::")[0],(x.split("::")[1],x.split("::")[2])))
joined_rdd = movies_mapped_rdd.join(final_rdd)
top_movies_rdd = joined_rdd.map(lambda x: x[1][0])
result = top_movies_rdd.collect()
for x in result:
    print(x)