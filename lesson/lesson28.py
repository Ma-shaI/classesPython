# Полиморфизм

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return self.a * 4
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# # print(r1.get_per_rect(), r2.get_per_rect())
#
# s1 = Square(10)
# s2 = Square(20)
# # print(s1.get_per_sq(), s2.get_per_sq())
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# # shape = [r1, r2, s1, s2, t1, t2]
# shape = [Rectangle(1, 2), Rectangle(3, 4), Square(10), Square(20), Triangle(1, 2, 3), Triangle(4, 5, 6)]
# for g in shape:
#     print(g.get_perimetr())


# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return self.value + int(a)
#
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return len(self.value + str(a))
#
#
# t1 = Number(10)
# t2 = Text('Python')
# print(t1.total(35))
# print(t2.total(35))


# class Cat:
#     def __init__(self, name, age):
#         if isinstance(name, str) and isinstance(age, (int, float)):
#             self.name = name
#             self.age = age
#         else:
#             raise TypeError('Введите правильно имя и возраст')
#
#     def info(self):
#         return f'Я кот. Меня зовут {self.name}. Мой возраст 2.5'
#
#     def make_sound(self):
#         return f'{self.name} мяукает'
#
#
# class Dog:
#     def __init__(self, name, age):
#         if isinstance(name, str) and isinstance(age, (int, float)):
#             self.name = name
#             self.age = age
#         else:
#             raise TypeError('Введите правильно имя и возраст')
#
#     def info(self):
#         return f'Я собака. Меня зовут {self.name}. Мой возраст 2.5'
#
#     def make_sound(self):
#         return f'{self.name} гавкает'
#
#
# c1 = Cat('Пушок', 2.5)
# d1 = Dog('Мухтар', 4)
# shape = [c1, d1]
#
# for i in shape:
#     print(i.info())
#     print(i.make_sound())


# class Human:
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print('\n', self.surname, self.name, self.age, end=' ')
#
#
# class Student(Human):
#     def __init__(self, surname, name, age, spec, group, ball):
#         super().__init__(surname, name, age)
#         self.spec = spec
#         self.group = group
#         self.ball = ball
#
#     def info(self):
#         super().info()
#         print(self.spec, self.group, self.ball, end=' ')
#
#
# class Teacher(Human):
#     def __init__(self, surname, name, age, course, grade):
#         super().__init__(surname, name, age)
#         self.course = course
#         self.grade = grade
#
#     def info(self):
#         super().info()
#         print(self.course, self.grade,  end=' ')
#
#
# class Graduate(Student):
#     def __init__(self, surname, name, age, spec, group, ball, diploma):
#         super().__init__(surname, name, age, spec, group, ball)
#         self.diploma = diploma
#
#     def info(self):
#         super().info()
#         print(self.diploma,  end=' ')
#
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
# for i in group:
#     i.info()


# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return  f'{self.__class__}: {self.name}'
#
#     def __str__(self):
#         return f'{self.name}'
#
#
# cat = Cat('Пушок')
# print(cat)

# class Point:
#     def __init__(self, *args):
#         self.__coord = args
#
#     def __len__(self):
#         return len(self.__coord)
#
#
# p = Point(5,7)
# print(len(p))

import math

# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# pt = Point(1, 2)
# print(pt.length)
# # pt.z = 3


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt = Point(1, 2)
# # print(pt.__dict__) # не работает если в классе есть slots
# pt2 = Point2D(1, 2)
# # print(pt2.__dict__)
# print('pt =', pt.__sizeof__())
# print('pt2 =', pt2.__sizeof__()+pt2.__dict__.__sizeof__())

# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = 'z',
#
#     def __init__(self, x, y, z):
#         super().__init__(x,y)
#         self.z = z
#
#
# pt = Point(1, 2)
# pt3 = Point3D(10, 20, 30)
# # pt3.z = 30
# print(pt3.x,pt3.y, pt3.z )
# # print(pt3.__dict__)


# функтор - объект классов, которые можно выполнять как функции

# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__counter += 1
#         print(self.__counter)
#
#
# c1 = Counter()
# c1()
# c1()
# c1()
# c1()
# c1()
#
# c2 = Counter()
# c2()
# c2()
# c2()

# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError('Аргумент должен быть строкой')
#
#         return args[0].strip(self.__chars)
#
#
# s1 = StripChars('?:!.; ')
# print(s1(' ?;Hello World! '))
#
#
# def strip_chars(chars):
#     def wrap(*args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError('Аргумент должен быть строкой')
#
#         return args[0].strip(chars)
#
#     return wrap
#
#
# s2 = strip_chars('?:!.; ')
# print(s2(' ?;Hello World! '))

a = 11
s = 6
c = 6

print('\n'.join([f"{' ' * (s - x - 1)}{'*' * (2 * x + 1)}" for x in range(0, s)]))
for i in range(0, c):
    print(' ' * (s - i - 1), '*'*(2 * i + 1))
