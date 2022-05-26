from pyspark import SparkContext
import os
import sys

sc = SparkContext("local[*]","usercount")
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

input_value = sc.textFile("./sample.txt")
#input_value = sc.textFile("C:/workspace_python_basic/PythonBasics/sample.txt")

words = input_value.flatMap(lambda x : x.split(" "))
word_map = words.map(lambda x : (x,1))
final_count = word_map.reduceByKey(lambda x,y: x+y)
result = final_count.collect()
for a in result:
    print(a)