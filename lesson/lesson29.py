# Класс как декоратор

# class MyDecorator:
#     def __init__(self, fn):
#         self.func = fn
#
#     def __call__(self, a, b):
#         print('перед вызовом функции')
#         res = self.func(a, b)
#
#         return str(res) + '\nпосле вызова функции'
#
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# print(func(2, 5))

# def MyDecorator(fn):
#     def wrap(a, b):
#         print('перед вызовом функции')
#         fn(a,b)
#         print('после вызова функции')
#
#     return wrap
#
#
# @MyDecorator
# def func(a, b):
#     print('func')
#
# func()


# class Power:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self, a, b):
#         return self.fn(a, b) ** 2
#
#
# @Power
# def func(a, b):
#     return a * b
#
#
# print(func(2, 3))


# class MyDecorator:
#     def __init__(self, fn):
#         self.func = fn
#
#     def __call__(self, *args, **kwargs):
#         print('перед вызовом функции')
#         res = self.func(*args, **kwargs)
#         return str(res) + '\nпосле вызова функции\n'


# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# @MyDecorator
# def func1(a, b, c):
#     return a * b * c
#
#
# @MyDecorator
# def func2(a, b, c):
#     return a * b * c
#
#
# print(func(2, 5))
# print(func1(2, 5, 2))
# print(func1(2, 5, c=3))

# class MyDecorator:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, fn):
#         def wrap(a, b):
#             print('перед вызовом функции')
#             print(self.name, end=': ')
#             fn(a, b)
#             print('после вызова функции')
#
#         return wrap
#
#
# @MyDecorator('test2')
# def func(a, b):
#     print(a, b)
#
#
# func(2, 5)


# Декорирование методов

# def dec(fn):
#     def wrap(*args, **kwargs):
#         print('*' * 20)
#         fn(*args, **kwargs)
#         print('*' * 20)
#
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f'{self.name} {self.surname}')
#
#
# p1 = Person('Виталий', "Карасев")
# p1.info()


# Дескрипторы
# __get__, __set__, __delete__

# class StringD:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = StringD(name)
#         self.surname = StringD(surname)
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         self.__name = value
#
#     @property
#     def surname(self):
#         return self.__surname
#
#     @surname.setter
#     def surname(self, value):
#         self.__surname = value


# p = Person('Ivan', 'Petrov')
# p.name.set('Vasya')
# print(p.name.get(), p.surname.get())

class ValidateString:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        print('get')
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.__name} должно быть строкой')
        instance.__dict__[self.__name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.__name]


class Person:
    name = ValidateString()
    surname = ValidateString()

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


p = Person('Ivan', 'Petrov')
p.name = 'Oleg'
#
# print(p.name)
# print(p.surname)
