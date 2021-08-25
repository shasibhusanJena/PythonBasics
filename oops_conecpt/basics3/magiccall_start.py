class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    # The __str__ function is used to return a user-friendly string representation of the object
    def __str__(self):
        return f"{self.title}  by {self.author} , cost {self.price}"

    def __call__(self, title, author,price):
        self.title = title
        self.author = author
        self.price = price

b1 = Book('Ultimate Goal','Leonado',20.95)
b2 = Book('Frank','Anderson',32.37)


print(b1)
# here call function is used as a function and we are able to change the value if the object at run,
# that is one of the benefit of it
b1("Anna","Leo",49.50)
print(b1)