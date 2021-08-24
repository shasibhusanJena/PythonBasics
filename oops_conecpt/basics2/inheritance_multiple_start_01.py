# multiple inheritance where child class inherit both class A, B

class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "class A"


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "class B"
# todo here prob is if class C inherits A and B then which inherited method will get called

class C(A,B):
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.foo)
        print(self.bar)

c1 = C()
c1.showprops()
# todo AS we can see it is calling class A method not class B, it is because of ordering of Inherited class
# todo Python interpreter uses something called "method resolution order" to lookup in the class
# todo lookup start with current class > followed by inherited class > from left to Right  > in which way it is defined
# todo we can monitor order of the class using method called __MRO__
print(c1.name)
print(C.__mro__)