from math import pi
class Shape:

    def __init__(self, name):
        self.name = name
    
    def area(self):
        raise NotImplementedError('derived classes need to override this method.')

class Rectangle(Shape):
    
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2
