import math


class Shape:
    def __init__(self, color):
        if not isinstance(color, str):
            raise TypeError('Цвет должен быть строкой')
        self.color = color

    def get_perimetr(self):
        raise NotImplementedError('В дочернем классе должен быть определен метод get_perimetr()')

    def get_area(self):
        raise NotImplementedError('В дочернем классе должен быть определен метод get_area()')

    def get_picture(self):
        raise NotImplementedError('В дочернем классе должен быть определен метод get_picture()')

    def print_info(self):
        raise NotImplementedError('В дочернем классе должен быть определен метод print_info()')

    def get_color(self):
        print('Цвет:', self.color)


class Square(Shape):
    def __init__(self, color, a):
        super().__init__(color)
        if not isinstance(a, int):
            raise TypeError('Сторона должна быть целым числом')
        self.a = a

    def get_perimetr(self):
        perimetr = self.a *4
        print(f'Периметр: {perimetr}')

    def get_area(self):
        print(f'Площадь: {self.a ** 2}')

    def get_picture(self):
        for i in range(self.a):
            print('*' * self.a)

    def print_info(self):
        print('===Квадрат===')
        print('Сторона:', self.a)
        super().get_color()
        self.get_area()
        self.get_perimetr()
        self.get_picture()


class Rectangle(Shape):
    def __init__(self, color, a, b):
        super().__init__(color)
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError('Обе стороны должны быть целым числом')
        self.a = a
        self.b = b

    def get_perimetr(self):
        perimetr = (self.a + self.b) * 2
        print(f'Периметр: {perimetr}')

    def get_area(self):
        area = self.a * self.b
        print(f'Площадь: {area}')

    def get_picture(self):
        for i in range(self.a):
            print('*' * self.b)

    def print_info(self):
        print('===Прямоугольник===')
        print('Длина:', self.a)
        print('Ширина:', self.b)
        super().get_color()
        self.get_area()
        self.get_perimetr()
        self.get_picture()


class Triangle(Shape):
    def __init__(self, color, a, b, c):
        super().__init__(color)
        if not isinstance(a, int) or not isinstance(c, int) or not isinstance(c, int):
            raise TypeError('Все стороны должны быть целыми числами')
        self.a = a
        self.b = b
        self.c = c

    def get_perimetr(self):
        perimetr = self.a + self.b + self.c
        print(f'Периметр: {perimetr}')

    def get_area(self):
        p = (self.a + self.b + self.c) / 2
        area = round(math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)), 2)
        print(f'Площадь: {area}')

    def get_picture(self):

        m = 0
        if (self.a == self.b and self.a != self.c) or self.a == self.c and self.a != self.b:
            for i in range(0, self.a):
                print(' ' * (self.a - i - 1), '*' * (2 * i + 1))
        elif self.b == self.c and self.b != self.a:
            for i in range(0, self.b):
                print(' ' * (self.b - i - 1), '*' * (2 * i + 1))
        elif self.a == self.b == self.c:
            m = (2 * self.a) - 2
            for i in range(0, self.a):
                for j in range(0, m):
                    print(end=' ')
                m -= 1
                for j in range(0, i + 1):
                    print('*', end=' ')
                print(' ')
        else:
            print('К сожалению я не могу нарисовать разносторонний треугольник')

    def print_info(self):
        print('===Треугольник===')
        print('Сторона 1:', self.a)
        print('Сторона 2:', self.b)
        print('Сторона 3:', self.c)
        super().get_color()
        self.get_area()
        self.get_perimetr()
        self.get_picture()


s1 = Square('red', 3)
s1.print_info()
print()
r1 = Rectangle('green', 3, 7)
r1.print_info()
print()
t1 = Triangle('yellow', 11, 6, 6)
t1.print_info()
