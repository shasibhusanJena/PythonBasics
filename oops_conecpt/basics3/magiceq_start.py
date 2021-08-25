class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    # todo the __eq__ method check for equality between objects
    def __eq__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare Book with non-book")

        return (self.title == value.title and
                self.author == value.author and
                self.price == value.price)

    # todo the _ge__ establishes >= relationship with another obj
    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare Book with non-book")
        return (self.price >= value.price)

    # todo the _lt__ establishes < relationship with another obj
    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare Book with non-book")
        return (self.price < value.price)


b1 = Book("Title", "Author", 25)
b2 = Book("Title 1","Author 1", 15)
b3 = Book("Title", "Author", 25)
b4 = Book("Title", "Author", 10)
b5 = Book("Title", "Author", 55)

# todo check for equality
print(b1 == b3)
print(b1 == b2)

# todo check for greater and lesser value
# print(b1 >= b4)
# print(b1 < b5)

# todo now we can sort them too

books = [b1,b2,b3,b4,b5]
books.sort()
print([{book.title, book.price} for book in books])
