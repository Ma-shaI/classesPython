import math


class Square:
    __count = 0

    @staticmethod
    def square_geron(a, b, c):
        Square.__count += 1
        p = 1 / 2 * (a + b + c)
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return s

    @staticmethod
    def square_triangle(a, h):
        Square.__count += 1
        s = 1 / 2 * a * h
        return s

    @staticmethod
    def square_s(a):
        Square.__count += 1
        s = a ** 2
        return s

    @staticmethod
    def square_rect(a, b):
        Square.__count += 1
        s = a * b
        return s

    @staticmethod
    def get_count():
        return Square.__count


s1 = Square()
print(s1.square_geron(3, 4, 5))
print(s1.square_triangle(6, 7))
print(s1.square_s(7))
print(s1.square_rect(2,6))
print(s1.get_count())
