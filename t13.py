class Shape:
    def __init__(self, points):
        self.points = points

    def move(self):
        pass

class Line(Shape):
    def __init__(self, points):
        super().__init__(points)

    def move(self):
        print("* " * self.points)

class Triangle(Shape):
    def __init__(self, points):
        super().__init__(points)

    def move(self):
        for i in range(1, self.points + 1):
            if i == 1 or i == self.points:
                print("* " * i)
            else:
                print("* " + "  " * (i - 2) + "*")

class Rectangle(Shape):
    def __init__(self, points):
        super().__init__(points)

    def move(self):
        for i in range(self.points):
            if i == 0 or i == self.points - 1:
                print("* " * self.points)
            else:
                print("* " + "  " * (self.points - 2) + "*")

class NullShape(Shape):
    def __init__(self, points):
        super().__init__(points)

    def move(self):
        print("Bo'sh shakl")


L = Line(4)
L.move()

print()

T = Triangle(5)
T.move()

print()

R = Rectangle(4)
R.move()

print()

S = NullShape(10)
S.move()
