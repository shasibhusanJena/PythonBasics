# import time
# import datetime
# print(time.time())
# print(datetime.date.today())

print("from module one",__name__)

## when we call __main__ method directly then it gives the __main__ method
## when called from the other class then it gives us the called class name

if __name__ == "__main__" :
    print("Executed when Invoked directly")
else:
    print("Executed when imported")
