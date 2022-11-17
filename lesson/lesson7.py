# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
#
# print(id(lt1))
# print(id(lt2))
#
#
# a = 'hello'
# b = 'hello'
# print(id(a))
# print(id(b))

# ls1 = [1, 2, 3]
# print(id(ls1))
# ls1.append(4)
# print(id(ls1))
# ls1 = [1, 2]
# print(id(ls1))
#
# a = 'fff'
# print(id(a))
# a = 'sss'
# print(id(a))


# s = 'Hello'
# print(id(s))
# s += ' world'
# print(id(s))

# s = 'Hello'
# print(id(s))
# s = s[1:-1]
# print(s)
# print(id(s))


# КОРТЕЖ (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = 1, 2, 3, 4, 5
# print(type(a))
# print(a)
#
# b = tuple((1, 2, 3, 4, 5))
# print(type(b))
#
# c = tuple("Hello")
# print(c)

# t = (1,)
# print(type(t))

# b = tuple((1, 2, 3, 4, 5))
# print(b)
# print(b[3:])
# print(b[1:3])

# s = tuple(int(input('-> ')) for i in range(3))
# print(s)

# s = input('Строка: ')
# a = tuple(s)
# print(a)

# from random import *

# mas = [randint(0, 100) for i in range(10)]
# print(mas)
# tpl = tuple(mas)
# print(tpl)
#
# print(tuple(randint(0, 100) for _ in range(10)))

# print(tuple(2 ** i for i in range(1, 13)))

# t1 = tuple('hello')
# t2 = tuple('world')
# t3 = t1 + t2
# print(t3)
# print(len(t3))
# print(t3.count('l'))
# print(t3.count('m'))
# print(t3.index('l'))
#
# for i in t3:
#     print(i, end=' ')

# def ret_tuple(a, b):
#     if b not in a:
#         return tuple()
#     elif a.count(b) == 1:
#         return a[a.index(b):]
#     else:
#         return a[a.index(b):a.index(b, a.index(b) + 1) + 1]
#
#
# print(ret_tuple((1, 2, 3), 4))
# print(ret_tuple((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(ret_tuple((1, 2, 8, 5, 1, 2, 9), 8))

# def run(a, b):
#     return tuple(randint(a, b) for _ in range(10))
#
#
# tpl1 = run(0, 5)
# tpl2 = run(-5, 1)
# print(tpl1)
# print(tpl2)
# tpl3 = tpl1 + tpl2
# print(tpl3)
# print('0 =', tpl3.count(0))


# t = (10, 11, [1, 2, 3], (4, 5, 6), ['hello', 'world'])
# print(t, id(t))
# t[-1][0] = 'new'
# t[4].append('hi')
# print(t, id(t))

# def create_tuple(lst):
#     s = []
#     for i in lst:
#         if i not in s:
#             s.append(i)
#     return tuple(s)
#
#
# print(create_tuple([1, 2, 3, 3, 2]))
# print(create_tuple([2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]))

# t = (1, 2, 3)
# x, y, z = t
# print(x, y, z)
#
#
# def get_user():
#     names = 'Tom'
#     ages = 22
#     is_marrieds = False
#     return names, ages, is_marrieds
#
#
# user = get_user()
# print(user)
# print(user[0])
# name, age, is_married = user
# print(name)


# a = (1, 2, 3)
# del a

# a = (1, 2, 3)
# lst = list(a)
# lst.append(4)
# print(lst)
# tpl = tuple(lst)
# print(tpl)

# countries = (
#     ('Германия', 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ('Франция', 66, (("Париж", 2.2), ("Марсель", 1.6))),
# )
# # print(countries)
#
# for country in countries:
#     # print(country)
#     countryName, countryPopulation, cities = country
#     print('\nСтрана:', countryName, ',', 'Население страны =', countryPopulation, )
#     for city in cities:
#         cityName, cityPopulation = city
#         print('\tГород:', cityName, ',', 'Население города =', cityPopulation)
#     print()
