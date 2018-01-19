import math


def shape_menu():
    typeOf = input("What kind of shape are you interested in? \n"
                   "You can enter Rectangle, Circle, Square, \n"
                   "or Triangle to view the various properties \n"
                   "of each.\n"
                   "")
    typeOf = typeOf.lower()
    return typeOf


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @classmethod
    def square(cls, side_length):
        return cls(side_length, side_length)

    def print_shape(self):
        if self.width == self.height:
            print("This square has side length of {0} and an area of {1} units squared.".format(self.width,
                                                                                                self.calc_area()))
        else:
            print(f"This rectangle has a width of {self.width} units,"
                  f"\n a height of {self.height} units, and an area of {self.calc_area()} units squared.")

    def calc_area(self):
        return self.height * self.width


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return math.pi * self.radius * self.radius

    def print_shape(self):
        print("This circle has a radius of {0} units and the area is {1} units squared.".format(self.radius,
                                                                                                round(self.calc_area(),
                                                                                                      2)))


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calc_area(self):
        return (self.base * self.height) / 2

    def print_shape(self):
        print("This triangle has a base of {0} units, a height of {1} units, and an area of {2} units squared"
              .format(self.base, self.height, round(self.calc_area(), 2)))


def end_menu():
    cont = input("Would you like to enter another shape? (y/n) ")
    cont = cont.lower()
    if cont == "1" or cont == "y" or cont == "yes":
        return True
    else:
        return False


while True:
    shape = shape_menu()

    if shape == "triangle":
        v1 = int(input("What is the base of your {0}? ".format(shape)))
        v2 = int(input("What is the height of your {0}? ".format(shape)))
        triangle = Triangle(v1, v2)
        triangle.print_shape()
        if not end_menu():
            break
    elif shape == "rectangle":
        v1 = int(input("What is the width of your {0}? ".format(shape)))
        v2 = int(input("What is the height of your {0}? ".format(shape)))
        rectangle = Rectangle(v1, v2)
        rectangle.print_shape()
        if not end_menu():
            break
    elif shape == "square":
        v1 = int(input("What is the length of your {0}".format(shape)))
        square = Rectangle.square(v1)
        square.print_shape()
        if not end_menu():
            break
    elif shape == "circle":
        v1 = int(input("What is the radius of your {0}".format(shape)))
        circle = circle(v1)
        circle.print_shape()
        if not end_menu():
            break
    else:
        print("Sorry, that isn't a shape I recognize.")

print("Goodbye!")
