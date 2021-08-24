# Abstract class example where c1.caleArea() and s1.caleArea() setting to None instead of caleArea() value

class GraphicShape:
    def __init__(self):
        super().__init__()

    def caleArea(self):
        pass

class Circle(GraphicShape):
    def __init__(self,radius):
        self.radus = radius

class Square(GraphicShape):
    def __init__(self,side):
        self.side = side

c1 = Circle(10)
s1 = Square(20)
# As we can see the cakeArea() method throws the None value and Abstraction method caleArea() is not implemented my
# the sub class, it meas abstraction is not happening correctly
print(c1.caleArea())
print(s1.caleArea())
