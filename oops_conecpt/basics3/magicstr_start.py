# using __str__ and __repr__ method to print object

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author} cost {self.price}"

    def __repr__(self):
        return f"title={self.title},author={self.author},price={self.price} rupees only"


b1 = Book("Game of Thrown", "Marks", 200)

print(b1)
# todo  it is good to at least print the repr which make it easy while debugging
print(str(b1))
print(repr(b1))
