# Абстрактные классы - тот класс в котором есть хотя бы один абстрактный метод
from abc import ABC, abstractmethod


# class Chess(ABC):
#     def draw(self):
#         print('Нарисовал шахматную фигуру')
#
#     @abstractmethod
#     def move(self):
#         print('Родитель')
#
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print('Переместил шахматную фигуру')
#
#
# q = Queen()
# q.draw()
# q.move()

# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     def print_value(self):
#         print(self.value, end=' ')
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = 'USD'
#
#     def convert_to_rub(self):
#         rub = self.value * Dollar.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=' ')
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = 'EUR'
#
#     def convert_to_rub(self):
#         rub = self.value * Euro.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=' ')
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# print('*' * 50)
# for elem in d:
#     elem.print_value()
#     print(f'= {elem.convert_to_rub():.2f}')
#
# print('*' * 50)
#
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
# for elem in e:
#     elem.print_value()
#     print(f'= {elem.convert_to_rub():.2f}')


class Father(ABC):
    @abstractmethod
    def display1(self):
        pass

    @abstractmethod
    def display2(self):
        pass


class Child(Father):
    def display1(self):
        print('Дочерний класс')


class GrandChild(Child):
    def display2(self):
        print('Внучатый класс')


gc = GrandChild()
gc.display2()
gc.display1()
