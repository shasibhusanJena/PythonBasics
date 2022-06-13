# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]
#
# Input : [1, 2, 3]
# Output : [3, 2, 1]

def swapList(newList):

    temp = newList[0]
    newList[0] = newList[len(newList)-1]
    newList[len(newList)-1] = temp

    return newList

newList = [12,35,9,56,24]
print("Before swapping",newList)
print("after swapping ",swapList(newList))

newList = [1,2,3]
print("Before swapping",newList)
print("after swapping ",swapList(newList))