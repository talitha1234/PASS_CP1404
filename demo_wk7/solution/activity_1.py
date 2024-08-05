from math import pi


class Circle:
    def __init__(self, radius=0):
        self.radius = radius

    def __str__(self):
        return "Circle with radius {}".format(self.radius)

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


if __name__ == "__main__":
    circle = Circle(8)
    print(circle)
    print("Area of {} is {:.2f}".format(circle, circle.area()))
    print("Perimeter of {} is {:.2f}".format(circle, circle.perimeter()))
