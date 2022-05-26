from pyspark import SparkContext

sc = SparkContext("local[*]","Demo")
sc.setLogLevel("Error")
input = sc.textFile("C:/workspace_data_engineering/week9/dataset/search_data.txt")
words = input.flatMap(lambda x:x.split(" "))
word_count = words.map(lambda x: (x,1))
final_count = word_count.reduceByKey(lambda  x,y :x+y)
result = final_count.collect()
for a in result:
    print(a)