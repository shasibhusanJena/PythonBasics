# this example is about the Object comparision between Newspaper and the Book

# create class Newspaper
class Newspaper:
    def __init__(self,title):
        self.title =title
# create class Book
class Book:
    def __init__(self, title):
        self.title = title

b1 = Book('Game of Thrown')
b2 = Book('Orbit')

n1 = Newspaper('Times of india')
n2 = Newspaper('Samaj')

# here we will compare values with type() and instanceOf()

# lets test with type()
# print(type(b1) == type(b2))
# print(type(b2) == type(n1))

# lets test with instanceOf() function

print(isinstance(b1,Book))
print(isinstance(n1,Newspaper))
print(isinstance(n2,Book))
print(isinstance(b2,Book))

