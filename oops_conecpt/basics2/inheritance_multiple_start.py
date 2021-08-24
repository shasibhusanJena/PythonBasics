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