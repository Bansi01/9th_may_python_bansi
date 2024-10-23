#Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle
import math

class Circle:
    def __init__(self, r):
        self.radius = r

    def circle_area(self):
        return math.pi * (self.radius ** 2)

    def circle_perimeter(self):
        return 2 * math.pi * self.radius

newCircle = Circle(5)
print(f"Area of the circle: {newCircle.circle_area():.2f}")
print(f"Perimeter of the circle: {newCircle.circle_perimeter():.2f}")
