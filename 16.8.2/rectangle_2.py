from rectangle import Reсtangle, Square, Circle
# задаем фигуры
rect_1 = Reсtangle (3,4)
rect_2 = Reсtangle(12, 5)
square_1 = Square(5)
square_2 = Square(10)
circle_1 = Circle(5)
circle_2 = Circle(10)

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2] #составляем список из фигур

for figure in figures:
    if isinstance(figure, Square): # если фигура соответвует классу квадрат, то выводим ее площадь
        print(figure.get_area_square())
    elif isinstance(figure, Circle): # если фигура соответвует классу круг, то выводим ее площадь
        print(figure.get_area_circle())
    else:
        print(figure.get_area()) # в противном случаи считаем что фигура прямоугольник и выводим ее площадь