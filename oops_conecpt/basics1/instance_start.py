# define a class
class Book:
# add some more new attributes to the class
    def __init__(self, title,author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
    def getPrice(self):
        if hasattr(self,'_discount'):
            print("discount applied")
            return self.price - (self.price * self._discount)
        else:
            return self.price
    # here _ says a developer that the this attribute is internal to the class and may change
    # And Python dont have a formal way of enforcing this
    def setDiscount(self,amount):
        self._discount =amount
# instantiate a class
b1 = Book('Ultimate Goal','Leonado',1200,20.95)
b2 = Book('Frank','Anderson',400,32)

# Print the proce of B1 Obj
print(b1.getPrice())
print(b2)

# Apply discount and check
print(b2.getPrice())
# set some discount and then print again
b2.setDiscount(0.25)
print(b2.getPrice())