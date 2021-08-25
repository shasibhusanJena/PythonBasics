class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    # The __str__ function is used to return a user-friendly string representation of the object
    def __str__(self):
        return f"{self.title} by {self.author} , cost {self.price}"

    # todo __getattribute__ called when an attr is retried.
    # directly access the attr  name otherwise a recursive loop is created
    def __getattribute__(self, name):
        if name == 'price':
            p = super().__getattribute__('price')
            d = super().__getattribute__('_discount')
            return p - (p*d)

    # todo __setattr__ called when an attribute value is set.
    # directly here otherwise a recursive loop cause an crash
    def __setattr__(self, name, value):
        if name == 'price':
            if type(value) is not float:
                raise ValueError("the Price attr value must be a float")
        return super().__setattr__(name,value)

    # todo __getattr__ when __getattribute__ lookup failed.
    # pretty much generate attributes on the fly with this method
    def __getattr__(self, name):
        return name + " is not here!"

b1 = Book('Ultimate Goal','Leonado',20.95)
b2 = Book('Frank','Anderson',32.37)


# b1.price =38.95
# print(b1)

# b2.price =40
# print(b2)

print(b1.randomprop)  # todo should print " randomprop is not here!" fix it