class Rectangle:
    def __init__(self, x, y, width, heigth):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = heigth

    def __str__(self):
        return f'Rectangle : {self.x}, {self.y}, {self.width}, {self.heigth}.'


rect_1 = Rectangle(5, 10, 50, 100)
print(rect_1)