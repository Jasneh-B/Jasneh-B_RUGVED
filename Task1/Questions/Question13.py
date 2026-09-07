"""
Implement the following classes to understand abstraction in Python :
Note: Driver code makes all the function calls and print statements

Class Name: Shape (Abstract Class)
Attributes: color (String)
Constructor: Shape(c) -> assign value of c to color attribute
Methods: get_color() -> returns value of color
         get_area() -> abstract method with float return type
Class Name: Square (extends Shape)
Attributes: side (float)
Constructor: Square(c, side) -> calls super(c) to initialize the color and assigns the value to side.
Methods: get_area() -> returns the area of the square (side * side)
"""

class Shape:
    def __init__(self, c):
        self.color = c

    def get_color(self):
        return self.color

    def get_area(self):
        raise NotImplementedError("Abstract method")

class Square(Shape):
    def __init__(self, c, side):
        super().__init__(c)
        self.side = side

    def get_area(self):
        return float(self.side * self.side)


sq = Square("Blue", 5)
print(sq.get_color())
print(sq.get_area())