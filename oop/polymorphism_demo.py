# polymorphism_demo.py

import math

class Shape:
    def area(self):
        """Base method to calculate area. Must be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement this method")


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        """Initialize Rectangle with length and width"""
        self.length = length
        self.width = width

    def area(self):
        """Calculate area of the rectangle"""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius: float):
        """Initialize Circle with radius"""
        self.radius = radius

    def area(self):
        """Calculate area of the circle"""
        return math.pi * (self.radius ** 2)