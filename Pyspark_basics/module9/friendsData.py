def parseLine(line):
    fields = line.split("::")
    age = int(fields[2])
    numFriends = int(fields[3])
    return (age, numFriends)


from pyspark import SparkContext

sc = SparkContext("local[*]", "friends by age")
line = sc.textFile("C:/workspace_data_engineering/week9/dataset/friendsdata.csv")
rdd1 = line.map(parseLine)
# (33,385) input
#(33,(385,1)) output
# in scala we used to access the elements of the tuple usinf x.1 x.2
# in python we access the element of the tuple using x[0],x[1]
totalsByAge =rdd1.mapValues(lambda x: (x,1)).reduceByKey(lambda x,y: (x[0]+y[0],x[1]+y[1]))
result =totalsByAge.mapValues(lambda  x: x[0]/x[1])
for a in result.collect():
    print(a)
#
# (26, 242.05882352941177)
# (40, 250.8235294117647)
# (68, 269.6)
# here output says age "26" have on an avg 242 friends
