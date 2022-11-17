# Словари (dict)

# s = ['one', 'two']
# print(s[0])
# d = {1: 'one', 2: 'two', 3: 'three'}
# print(d[1])

# d = {'one': 1, 'two': 2}
# print(d)
# print(type(d))
#
# d1 = dict(one=1, two=2)
# print(d1)
# print(type(d1))

# a = [('igor@gmail.com', 'igor'), ('irina@gmail.com', 'irina'), ('anna@gmail.com', 'anna')]
# d = dict(a)
# print(d)

# d = {a: a ** 2 for a in range(1, 7)}
# print(d)
# print(d[2])
# d[2] = 15
# print(d)
# d[6] = 4**2
# print(d)

# d = {0: 'text', 'one': 45, (1, 2.3): 'кортеж', 42: [2, 3, 6, 7], True: 1}
# print(d)
# print(d[True])
# print(d[(1,2.3)])
# print(d[42][1])
# print('one' in d)
# print('two' in d)
# print(d.keys())
# if 'one' in d:   # работает быстрее
#     print('TRUE')
#
# if 'one' in d.keys():
#     print('TRUE')
#
# key = 'four'
# # if key in d:
# #     del d[key]
#
# try:
#     del d[key]
# except KeyError:
#     print(f'Элемента с ключом {key} не существует')
#
# print(d)
# for key in d:
#     print(key, '->', d[key])

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# pro = 1
# for item in d:
#     pro *= d[item]
# print(pro)

# d = dict()
# for i in range(1, 5):
#     d[i] = input('->')
# print(d)

# d = {a: input('-> ') for a in range(1,5)}
# a = int(input('Какой элемент исключить? '))
# print(d)
# if a in d:
#     del d[a]
#     print(d)
# else:
#     print('Такого элемента нет')

# capitals = dict()
# capitals['Россия'] = 'Москва'
# capitals['Италия'] = 'Рим'
# capitals['Испания'] = 'Мадрид'
# print(capitals)
#
# countries = ['Россия', "Италия", "Франция", "Испания"]
#
# for country in countries:
#     if country in capitals:
#         print('Столица страны ' + country + ': ', capitals[country] )
#     else:
#         print('В базе нет страны с названием:', country)

# p = {1: ['Core-i3-4330', 9, 4500],
#      2: ['Core i5-4670', 3, 8500],
#      3: ['AMD FX-6300', 6, 3700],
#      4: ['Pentium 63220', 8, 2100],
#      5: ['Core i5-3450', 5, 6400]
#      }
# for i in p:
#     print(i, ') ', p[i][0], ' - ', p[i][1], ' шт. по ', p[i][2], 'руб', sep='')
# while True:
#     n = input('№ ')
#     if n != '0':
#         cnt = int(input('Количество: '))
#         if n in p:
#             p[n][1] = cnt
#     else:
#         break
#
# for i in p:
#     print(i, ') ', p[i][0], ' - ', p[i][1], 'шт. по ', p[i][2], 'руб', sep='')


# d = {'a': 1, 'b': 2, 'c': 3}
# # print(d['b'])
# # value = d.get('e', 'No')
# # print(value)
# # print(d)
# # # item = d.items()
# # # print(item)
# # # key = d.keys()
# # # print(key)
# # # value = d.values()
# # # print(value)
# # # for i, j in d.items():
# # #     print(j)
# # # d.clear()
# # # item = d.setdefault('e', 5)
# # # print(item)
# # d.update([('r', 7), ('q', 9)])
# # print(d)
# d2 = d
#
# print('D =', d)
# print('D2 =', d2)
# d['e'] = 7
#
# print('D =', d)
# print('D2 =', d2)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# c = x.copy()
# c.update(y)
# c = x | y
# print(c)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# new_d = dict()
# name = d.pop('name')
# salary = d.pop('salary')
# new_d.update({'name': name, 'salary': salary})
# print(d)
# print(new_d)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# d['location'] = d.pop('city')
# print(d)

# a = {
#     'First': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'Second': {
#         4: 'four',
#         5: 'five'
#     }
# }
# for i in a:
#     print(i)
#     for j in a[i]:
#         print('\t',j, ': ', a[i][j], sep='')
#
# print(a)


# d = {'один': 1, "два": 2, "три": 3, "четыре": 4}
# a = {value: key for key, value in d.items() if value <= 2}
# print(a)


# a = {i: i * 5 for i in [10, 20, 30, 40]}
# print(a)

# a = {i: i * 5 for i in 'Hello'}
# print(a)

# value = int(input('-> '))
# lt = [1, 2, 3, 4, 5]
# a = {i: value for i in range(1,9)}
# print(a)

# d = dict.fromkeys(['a', 'b'], 100)
# print(d)

# figures = {1: 'Rectangle', 2: 'Triangle', 3: 'Circle'}
# value = list(figures.items())
# print(value)

# lst = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
# d = {}
# s = ''
# for i in lst:
#     if type(i) == str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
# print(d)


# zip()

# d = dict(zip([12, 1, 2], ['Dec', 'Jan', 'Feb']))
# print(d)

# a = [12, 1, 2]
# b = ['Dec', 'Jan', 'Feb']
# f = {k: v for k, v in zip(a, b)}
# print(f)


# a = [1, 2, 3]
# print(set(zip(a)))

# print(list(zip(range(5), range(0, 100))))

# a = {'name': 'Igor', 'last_name': 'Doe', 'job': 'Consultant'}
# b = {'name': 'Irina', 'last_name': 'Smith', 'job': 'Manager'}
# c = {'name': 'Irina', 'last_name': 'Smith', 'job': 'Manager'}
# for (k1, v1), (k2,v2),(k3, v3) in zip(a.items(), b.items(), c.items()):
#     # print(k1, '->', v1)
#     # print(k2, '->', v1)
#     print(k1, ' -> ', v1, ', ', v2, ', ', v3,sep='')

# a = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# x, y = zip(*a)
# print(x)
# print(y)

# lst1 = [2, 1, 4, 3]
# lst2 = ['d', 'a', 'c', 'b']
# a1 = list(zip(lst2, lst1))
# print(a1)
# a1.sort()
# print(a1)

# month = ['January', 'February', 'March']
# total_sales = [52000.00, 51000.00, 48000.00]
# prod_cost = [46800.00, 45900.00, 43200.00]
# for sales, cost, m in zip( total_sales, prod_cost, month):
#     res = sales - cost
#     print('Чистая прибыль в', m, '=', res)

# one = {'apple': 0.4, 'orange': 0.35, 'banana': 0.6}
# two = {'peper': 0.2, 'onion': 0.55}
# print({**one, **two})
#
# for k, v in {**one, **two}.items():
#     print(k, '->', v)

