# using class level and the static method
class Book:  # todo This should be rewritten
# todo prperties defined by class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER","PAPERBACK","EBOOK")

# todo Double Underscore proerties are hidden from the other class
    __booklist = None
# todo create a class method
# create  a class Object , works with class instnace
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

# todo create a static method
    @staticmethod
    def getBookList():
        if Book.__booklist ==None:
            Book.__booklist = []
        return Book.__booklist

    # instance method receive specific  object instance as an argument
    # And operate on a date specific to the object instance
    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title,booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f'{booktype} is not a valid book')
        else:
            self.booktype =booktype

# todo access the class attributes

print("Book types ",Book.getbooktypes())

# todo create some book instance

b1 = Book("Title 1",'HARDCOVER')
#b2 = Book("Title 2",'comic')
b2 = Book("Title 2",'PAPERBACK')

# Use the static method to access a singleton object
thisbooks = Book.getBookList()
thisbooks.append(b1)
thisbooks.append(b2)
print(thisbooks)
