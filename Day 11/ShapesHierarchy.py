from math import pi

class Shape:
    colour = ""

class Circle (Shape):
    radius = 0

    def __init__(self, c, r):
        self.radius = r
        self.colour = c

    def get_area(self):
        return pi * (self.radius ** 2)

class Rect(Shape):
    l = 0
    h = 0

    def __init__(self, c, lg, ht):
        self.l = lg
        self.h = ht
        self.colour = c

    def get_area (self):
        return self.l * self.h

my_shape = Rect("Red", 5, 10)

print (my_shape.get_area())