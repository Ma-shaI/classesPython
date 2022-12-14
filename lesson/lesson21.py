# ООП

# class Point:
#     """Класс для представления координат точек на плоскости"""
#     x = 1
#     y = 1


# print(Point.__doc__)
# print(Point.__name__)
# print(dir(Point))
# p1 = Point()
# p2 = Point()
# print('p1:', p1.x)
# print('p2:', p2.x)
# print('Point =', Point.x)
# # print(type(p1))
# p1.x = 100
# p2.x = 200
# print('p1 = ', p1.x)
# print('p2 = ', p2.x)
# print('Point=', Point.x)
# print(id(p1))
# print(id(p2))
# print(id(Point))
# Point.y = 300
# Point.x = 400
# print('p1 = ', p1.y)
# print('p2 = ', p2.y)
# print('Point=', Point.y)
# print('p1 = ', p1.x)
# print('p2 = ', p2.x)
# print('Point=', Point.x)


# class Point:
#     """Класс для представления координат точек на плоскости"""
#     x = 1
#     y = 1


# p1 = Point()
# p1.x = 5
# p1.y = 10
# p1.z = 20
# print(p1.x, p1.y)
# print(p1.__dict__)  # используется для просмотра всех свойств класса или его экземпляра
# # print(Point.__dict__)


# class Point:
#     """Класс для представления координат точек на плоскости"""
#     x = 1
#     y = 1
#
#     def set_coords(self):
#         print(self.__dict__)


# p1 =Point()
# print(p1.x)
# p1.x =5
# p1.y =10
# p1.set_coords()
# Point.set_coords(p1)
# p2 = Point()
# p2.x =2
# p2.y =7
# p2.set_coords()


# class Point:
#     """Класс для представления координат точек на плоскости"""
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point()
# p1.set_coord(5, 10)
# print(p1.__dict__)
# print(p1.x)
# p2 = Point()
# p2.set_coord(2, 7)
# print(p2.__dict__)
# print(p2.x)
# Point.set_coord(p2, 5, 8)
# print(p2.__dict__)
# print(p2.x)


# class Human:
#     name = 'name'
#     birthday = '00.00.0000'
#     phone = '00-00-00'
#     country = 'country'
#     city = 'city'
#     address = 'street, house'
#
#     def print_info(self):
#         print(' Персональные данные '.center(40, '*'))
#         print(f'Имя:{self.name}\nДата рождения:{self.birthday}\nНомер телефона: {self.phone}\n'
#               f'Страна: {self.country}\nГород: {self.city}\nДомашний адрес: {self.address}')
#         print('=' * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):
#         if isinstance(name, str):
#             self.name = name
#
#     def get_name(self):
#         return self.name
#
#     def set_birthday(self, birthday):
#         self.birthday = birthday
#
#     def get_birthday(self):
#         return self.birthday
#
#     def set_phone(self, phone):
#         self.phone = phone
#
#     def get_phone(self):
#         return self.phone
#
#     def set_country(self, country):
#         self.country = country
#
#     def get_country(self):
#         return self.country
#
#     def set_city(self, city):
#         self.country = city
#
#     def get_city(self):
#         return self.city
#
#     def set_address(self, address):
#         self.address = address
#
#     def get_address(self):
#         return self.address
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info('Юля', '23.05.1986', '45-46-98', 'Россия', 'Москва', 'Чистопрудный бульвар, 1А')
# h1.print_info()
# h1.set_name('Алевтина')
# h1.print_info()
# print(h1.get_name())
# h1.set_birthday('18.05.1995')
# print(h1.get_birthday())


# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def print_info(self):
#         print('Данные сотрудника:', self.name, self.surname )
#
#     def add_skill(self, k):
#         self.skill += k
#         print('Квалификация сотрудника:', self.skill, '\n')
#
#
# p1 = Person('Viktor', 'Reznik')
# p1.print_info()
# p1.add_skill(3)
#
# p2 = Person('Anna', 'Dolgih')
# p2.print_info()
# p2.add_skill(2)

# class Point:
#     # def __new__(cls, *args, **kwargs):
#     #     print('Конструктор')
#     #     return super().__new__(cls)
#     def __init__(self, x, y):
#         print('Инициализатор')
#         self.x = x
#         self.y = y
#
#     def __del__(self):
#         print(f'Удаление экземпляра: {self.__class__.__name__}')
#
#     def print_coord(self):
#         print(f'x: {self.x}, y: {self.y}')
#
#
#
# p1 = Point(5, 10)
# p1.print_coord()
# print(id(p1))
# p2 = Point(2,7)
# p2.print_coord()
# print(id(p2))


# class Point:
#     count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#     def print_count(self):
#         print(self.count)
#
#
# p1 = Point(5, 10)
# p1.print_count()
# p2 = Point(7, 2)
# print('->',Point.count)
# p2.print_count()
# p3 = Point(3, 4)
# p3.print_count()
# print(Point.count)
#
# print(id(p1.count))
# print(id(p2.count))
# print(id(p3.count))
# print(id(Point.count))


# class Robot():
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         Robot.k += 1
#         print(f'Инициализация робота: {self.name}')
#
#     def __del__(self):
#         print(self.name, 'выключается')
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(self.name, "был последним")
#             # print('Численность роботов:', Robot.k)
#         else:
#             print('Работающих роботов осталось:', Robot.k)
#
#     def say_hi(self):
#         print('Приветствую! Меня зовут:', self.name)
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid3 = Robot('RP-0')
# droid3.say_hi()
# print("Численность роботов:", Robot.k)
#
# print('\nЗдесь роботы могут проделать какую-то работу\n')
# print('Роботы закончили свою работу. Давайте их выключим\n')
# del droid1
# del droid2
# del droid3
# print('Численность роботов:', Robot.k)

# class Point:
#     __slots__ = ['__x', '__y', 'z']
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print('Координаты должны быть числами')
#
#     def set_coord_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print('Координаты должны быть числами')
#
#     def set_coord_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print('Координаты должны быть числами')
#
#     def get_coord(self):
#         return self.__x, self.__y
#
#     def get_coord_x(self):
#         return self.__x
#
#     def get_coord_y(self):
#         return self.__y
#
#
# p1 = Point(5, 10)
# p1.z = 154
# print(p1.z)
# print(p1.__dict__)
# # print(p1.get_coord())
# # p1.set_coord(1, 33)
# # print(p1.get_coord())
# # # p1.__x = 100
# # # p1.__y = 'abc'
# # # # print(p1.x, p1.y)
# # p1.set_coord_x(8)
# # print(p1.get_coord_x())
# # p1.set_coord_y(9)
# # print(p1.get_coord_y())
# #
# # print(p1.__dict__)
# p1._Point__x=111
# print(p1._Point__x)
# print(p1.__dict__)

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __set_x(self, x):
#         print('Вызов __set_x')
#         self.__x = x
#
#     def __get_x(self):
#         print('Вызов __get_x')
#         return self.__x
#
#     def __del_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100
# print(p1.x)
# del p1.x

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def x(self):
#         print('Вызов __get_x')
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         print('Вызов __set_x')
#         self.__x = x
#
#     @x.deleter
#     def x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     # x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100
# print(p1.x)
# del p1.x

# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print('Килограммы задаются только числами')
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#
# weight = KgToPounds(12)
# print(weight.kg, 'кг =>', end=' ')
# print(weight.to_pounds(), 'фунтов', end='\n')
# weight.kg = 41
# print(weight.kg, 'кг =>', end=' ')
# print(weight.to_pounds(), 'фунтов', end='\n')
# weight.kg = 'ten'


# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, new_age):
#         self.__age = new_age
#
#     @age.deleter
#     def age(self):
#         del self.__age
#
#
# p1 = Person('Irina', 26)
# print(p1.__dict__)
# p1.name = "Igor"
# print(p1.name)
# p1.age = 31
# print(p1.age)
# del p1.age

# class Point:
#     __count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#
# p1 = Point(5, 10)
# p2 = Point(4, 8)
# p3 = Point(2, 7)
# print(Point.get_count())

# class Change:
#     @staticmethod
#     def inc(x):
#         return  x+1
#
#     @staticmethod
#     def dec(x):
#         return x-1
#
# print(Change.inc(10), Change.dec(10))

# import math


# class Change:
#     @staticmethod
#     def maximum(a, b, c, d):
#         return max(a, b, c, d)
#
#     @staticmethod
#     def minimum(a, b, c, d):
#         return min(a, b, c, d)
#
#     @staticmethod
#     def arif(a, b, c, d):
#         return (a + b + c + d) / 4
#
#     @staticmethod
#     def fact(a):
#         # return math.factorial(a)
#         first = 1
#         for i in range(1, a + 1):
#             first *= i
#         return first
#
#
# p1 = Change()
# print('Максимальное число: ', p1.maximum(3, 5, 7, 9))
# print('Минимальное число:', p1.minimum(3, 5, 7, 9))
# print('Среднее арифметическое', p1.arif(3, 5, 7, 9))
# print("Факториал числа", p1.fact(5))


# class Numbers:
#     @staticmethod
#     def max(*args):
#         max1 = 0
#         for i in args:
#             max1 = max1 if i < max1 else i
#         return max1
#
#
# print(Numbers.max(3, 5, 7, 9, 11, 15))

# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split('.'))
#         date1 = cls(day, month, year)
#         return date1
#
#     def string_to_db(self):
#         return f'{self.year}-{self.month}-{self.day}'
#
#
# string_date = Date.from_string('23.10.2022')
# print(string_date.string_to_db())
# string_date1 = Date.from_string('12.12.2022')
# print(string_date1.string_to_db())