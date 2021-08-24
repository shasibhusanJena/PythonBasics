# this example is to get Inheritance feature for classes like Book, Newspaper and Magazine

# todo  we will create new Parent/super class as Publisher > child class (Book and Periodic)
class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price


# todo Here Periodic is a new class - > that will have common attributes from NewsPaper and Magazine class
# todo Periodic reads all attribute from Publication and create couple more common types for sub classes
class Periodic(Publication):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price)
        self.publisher = publisher
        self.period = period


class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages


class Newspaper(Periodic):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)


class Magazine(Periodic):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)


b1 = Book('New world', 'Martin', 1200, 10)
n1 = Newspaper('Game changer', 'Time of India', 120, 30)
m1 = Magazine('GST', 'Daily Insider', 100, 50)

print(b1.title)
print(n1.period)
print(n1.publisher, b1.price, n1.price, m1.price)
