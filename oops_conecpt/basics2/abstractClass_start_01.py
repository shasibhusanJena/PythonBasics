# this is an example of Abstract class
# to fix the issue lets import the ABC and abstractmethod from common pkg abc
from abc import ABC, abstractmethod

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def caleArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius
    def caleArea(self):
        return 3.14 * (self.radius ** 2)


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side
    def caleArea(self):
        return self.side * self.side


c1 = Circle(10)
s1 = Square(20)

print(c1.caleArea())
print(s1.caleArea())
