from pyspark import SparkContext

sc = SparkContext("local[*]","Demo")
input = sc.textFile("C:/workspace_pyspark/pythonProject/read.txt")
words = input.flatMap(lambda x:x.split(" "))
word_count = words.map(lambda x: (x,1))
final_count = word_count.reduceByKey(lambda  x,y :x+y)
result = final_count.collect()
for a in result:
    print(a)