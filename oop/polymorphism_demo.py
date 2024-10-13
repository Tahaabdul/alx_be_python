import math

# Base Class - Shape
class Shape:
    def area(self):
        """This method must be overridden in derived classes."""
        raise NotImplementedError("Subclasses must implement the area method.")


# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width


# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)
