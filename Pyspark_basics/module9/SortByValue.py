from pyspark import SparkContext

sc = SparkContext("local[*]","Demo")
sc.setLogLevel("Error")
input = sc.textFile("C:/workspace_data_engineering/week9/dataset/search_data.txt")
words = input.flatMap(lambda x:x.split(" "))
word_count = words.map(lambda x: (x,1))
# here we are trying to implement both sortByKey and sortBy , and we will get same result

#final_count = word_count.reduceByKey(lambda x,y : x+y).map(lambda  x : (x[1],x[0]))
#result= final_count.sortByKey(False).map(lambda x: (x[1],x[0])).collect()

final_count = word_count.reduceByKey(lambda x,y : x+y)
result = final_count.sortBy(lambda x : x[1],False).collect()

for a in result:
    print(a)