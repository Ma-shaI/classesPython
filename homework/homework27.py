from math import sqrt


class Rectangle:

    def __init__(self, height, width):
        self.__height = self.__width = 0
        if Rectangle.__check_value(height) and Rectangle.__check_value(width):
            self.__height = height
            self.__width = width
            print('Длина прямоугольника:', self.__height)
            print('Ширина прямоугольника:', self.__width)

    def __check_value(z):
        if isinstance(z, int):
            return True
        return False

    def set_height(self, height):
        if Rectangle.__check_value(height):
            self.__height = height
        else:
            print('Длина должна быть целым числом ')

    def get_height(self):
        print('Длина прямоугольника:', self.__height)

    def set_width(self, width):
        if Rectangle.__check_value(width):
            self.__width = width

        else:
            print('Ширина должна быть целым числом ')

    def get_width(self):
        print('Ширина прямоугольника:', self.__width)

    def print_area(self):
        print('Площадь прямоугольника:', self.__height * self.__width)

    def print_perimetr(self):
        print('Периметр прямоугольника:', 2 * (self.__height + self.__width))

    def print_hypotenuse(self):
        print('Гипотенуза(диагональ) прямоугольника:', round(sqrt(self.__height ** 2 + self.__width ** 2), 2))

    def print_rectangle(self):
        for i in range(self.__height):
            print('*' * self.__width)


r1 = Rectangle(3, 9)
r1.print_area()
r1.print_perimetr()
r1.print_hypotenuse()
r1.print_rectangle()
r1.set_height(5)
r1.get_height()
r1.set_width(15)
r1.get_width()
r1.print_area()
r1.print_perimetr()
r1.print_hypotenuse()
r1.print_rectangle()