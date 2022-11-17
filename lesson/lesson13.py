#  анонимная функция lambda-выражение
import random

# print((lambda x, y: print('res=', x + y))(1, 2))
# print((lambda x, y: x + y)('a', 'b'))
#
# func = lambda x, y: x + y
# print(func(1, 2))
# print(func('a', 'b'))
#
# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# summ = lambda a=1, b=2, c=3: a + b + c
#
# print(summ())
# print(summ(10))
# print(summ(10, 20))


# func1 = lambda *args: args
#
# print(func1(1, 2, 3, 4))
# print(func1('a', 'b'))


# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4,
#      )
#
#
# for t in c:
#      print(t('abc_'))

# def inc(n):
#     return lambda x: x + n
#
#
# f = inc(42)
# print(f(3))


# def inc1(n):
#     def wrap(x):
#         return x + n
#
#     return wrap
#
#
# f = inc1(42)
# print(f(3))
#
# inc2 = (lambda n: (lambda x: x + n))
# f = inc2(42)
# print(f(3))
# print(inc2(42)(3))

# print((lambda n: (lambda x: x + n))(3)(42))


# sum3 = (lambda a: (lambda b: (lambda c: a + b + c)))
# print(sum3(2)(4)(6))
#
# print((lambda a: (lambda b: (lambda c: a + b + c)))(2)(4)(6))

# d = {'b': 15, 'a': 10, 'c': 4}
#
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# print(lst)
#
# dict1 = dict(lst)
# print(dict1)


# players = [{'name': 'Антон', 'last name': 'Бирюков', 'raiting': 9},
#            {'name': 'Алексей', 'last name': 'Бодня', 'raiting': 10},
#            {'name': 'Федор', 'last name': 'Сидоров', 'raiting': 4},
#            {'name': 'Михаил', 'last name': 'Семенов', 'raiting': 6}
#            ]
#
# res = sorted(players, key=lambda i: i['last name'])
# print(res)
# print(sorted(players, key=lambda i: i['raiting'], reverse=True))
# print(sorted(players, key=lambda i: i['raiting']))

# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
# b = a[2](12, 5)
# print(b)

# a = {'one': lambda x: x - 1, 'two': lambda x: abs(x) - 1, 'three': lambda x: x}
# b = [-3, 10, 0, 1]
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i >0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))

# d = {
#     1: (lambda: print('Понедельник')),
#     2: (lambda: print('Вторник')),
#     3: (lambda: print('Среда')),
#     4: (lambda: print('Четверг')),
#     5: (lambda: print('Пятница')),
#     6: (lambda: print('Суббота')),
#     7: (lambda: print('Воскресенье')),
# }
#
# d[5]()

# maximum = (lambda a,b: a if a > b else b)
# print(maximum(15, 13))


# minimum = (lambda a, b, c: a if a < b else b if b < c else c)
# print(minimum(1, 0, 5))


#  Функция map()


# def multiple(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# print(list(map(multiple, lst)))
# print(list(map(lambda t: t*2,range(2,10))))

# t = 2.88, -1.75, 100.55
# print(list(map(lambda x: str(x), t)))
# a = ['2.88', '-1.75', '100.55']
#
# print(list(map(float, a)))
# print(list(map(int, map(float, a))))

# areas = [3.85233554, 5.5213369, 7.2589634, 56.7412589, 9.0123456, 32.7789456]
# print(list(map(round, areas, range(1,7))))

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
# lst = list(map(lambda x, y: (x, y), st, num))
# print(lst)
# tp = dict(lst)
# print(tp)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# print(list(map(lambda x, y: (x + y), l1, l2)))


# filter (func, iterable)

# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)
#
# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# prinz

# lst = [random.randint(1, 40) for i in range(10)]
# print(lst)
# res = list(filter(lambda s: 10 <= s <= 20, lst))
# print(res)


lst = [45, 55, 60, 37, 100, 105, 220]
res = list(filter(lambda s: s % 15 == 0, lst))
print(res)
