from abc import  ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def Area(self):
        pass

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def Area(self):
        return 0.5 * self.base * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Rectangle(Shape):
    def __init__(self,length,width):
        self.width = width
        self.length = length

    def Area(self):
        return self.width * self.length


rect = Rectangle(4, 5)
tri = Triangle(3, 4)
sq = Square(6)

print("Rectangle area:", rect.Area())
print("Triangle area:", tri.Area())
print("Square area:", sq.Area())
