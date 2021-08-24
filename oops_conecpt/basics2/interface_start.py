# this example is to add a interface and then try to invoke it
# in python we use 'class' and 'abstractmethod' in a combination to create a interface

from abc import ABC, abstractmethod


class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def caleArea(self):
        pass


class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def caleArea(self):
        return 3.14 * (self.radius ** 2)
    def toJSON(self):
        return f"{{\"square\" : {str(self.caleArea())} }}"

c1 = Circle(10)
print(c1.caleArea())
