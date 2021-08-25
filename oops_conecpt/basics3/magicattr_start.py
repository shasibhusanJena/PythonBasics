class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    # The __str__ function is used to return a user-friendly string representation of the object
    def __str__(self):
        return f"{self.title} by {self.author} , cost {self.price}"

    # todo __getattribute__ called when an attr is retrivied.
    # directly access the attr  name otherwise a recusrsive loop is created

    # todo __setattr__ called when an attribute value is set.
    # directly here otherwise a recursive loop cause an crash

    # todo __getattr__ when __getattribute__ lookup failed.
    # pretty much generate attributes on the fly with this method

b1 = Book('Ultimate Goal','Leonado',20.95)
b2 = Book('Frank','Anderson',32)


