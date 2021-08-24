# this example is to get Inheritance feature for classes like Book, Newspaper and Magazine

class Book:
    def __init__(self,title,author,pages,price):
        self.title =title
        self.author = author
        self.pages = pages
        self.price = price

class Newspaper:
    def __init__(self,title,publisher,price,period):
        self.title = title
        self.publisher =publisher
        self.price = price
        self.period =period

class Magazine:
    def __init__(self,title,publisher,price,period):
        self.title =title
        self.publisher = publisher
        self.price = price
        self.period = period

b1 = Book('New world','Martin',1200,10)
n1 = Newspaper('Game changer','Time of India',120,30)
m1 = Magazine('GST','Daily Insider',100,50)

print(b1.title)
print(n1.period)
print(n1.publisher,b1.price,n1.price,m1.price)