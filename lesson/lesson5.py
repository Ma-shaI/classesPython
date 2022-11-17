# Генерация случайных данных

# import random

# print(random.random())
# print(random.randint(0, 9))  # случайное число от 0 до 9 (включительно)
# print(random.randrange(0, 10, 2))

# from random import *

# print(randint(2, 9))
# print(randrange(1, 10, 3))
# print(round(uniform(10.5, 25.5), 2))
#
# s = [55, 66, 77, 88, 99, 20, 30, 80, 90]
# print(choice(s))  # возвращает случайное значение из списка
# print(choices(s, k=3))  # возвращает нужное количество случайных элементов, могут повторяться
# print(s)
# shuffle(s)  # перемешивает список случайным образом
# print(s)

# mas = [randint(0, 100) for i in range(10)]
# print(mas)

# lst = [5, 3, 2, 4, 1]
# print(len(lst))
# print(sum(lst))
# print(max(lst))
# print(min(lst))

# lst = [randint(0, 100) for i in range(10)]
# print(lst)
# l = lst.pop(lst.index(max(lst)))
# lst.insert(0, l)
# print(lst)

# lst = [randint(-20, 20) for i in range(10)]
# print(lst)
# lst.sort(reverse=True)
# print(lst)

# lst = [randint(0, 100) for i in range(10)]
# print(lst)
# print('Min:', min(lst))
# l = lst.index(min(lst))
# print('index min:', l)
# lst[:l] = []
# print(lst)

# x = list('1a2b3c4d')
# print(x)
# print('a' in x)
# print('e' in x)
# print('a' not in x)
# print('e' not in x)

# lst = []
# # if len(lst) ==0:
# print(bool(lst))
# if not lst:
#     print('Список пустой')

# n1 = int(input('Введите размер первого списка: '))
# n2 = int(input('Введите размер второго списка: '))
# lst1 = [randint(0, 10) for i in range(n1)]
# lst2 = [randint(0, 10) for j in range(n2)]
# print('Первый список:', lst1)
# print("Второй список:", lst2)
# lst3 = lst1 + lst2
# print("Третий список:", lst3)
# lst4 = []
# for i in lst3:
#     if i not in lst4:
#         lst4.append(i)
#
# print("Элементы обоих списков без повторений:", lst4)
# lst5 = []
# # for i in lst1:
# #     for j in lst2:
# #         if i == j and i not in lst5:
# #             lst5.append(i)
# for i in range(len(lst1)):
#     if lst1[i] in lst2 and lst1[i] not in lst5:
#         lst5.append(lst1[i])
# print("Список, содержащий элементы общие для двух списков:", lst5)
# lst6 = [min(lst1), min(lst2), max(lst1), max(lst2)]
# print("Содержащий только минимальное и максимальное значение каждого из списков:", lst6)

# n = int(input('Введите размер списка: '))
# lst = []
# for i in range(n):
#     m = randint(0, n)
#     if m not in lst:
#         lst.append(m)
# print(lst)

# n = int(input('Введите число: '))
# s=[]
# while len(s)<n:
#     k = randint(0, n-1)
#     if k not in s:
#         s.append(k)
# print(s)

# n = int(input('Введите число: '))
# s = [i for i in range(1, n + 1)]
# shuffle(s)
# print(s)
#
# m = [[1, 2, 3, 4],
#      [5, 6, 7, 8],
#      [9, 10, 11, 12]]
# print(m)
# print(m[1][2])

# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end='\t')
#     print()

# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end='\t')
#     print()

# m = [[1, 2, 3, 4],
#      [5, 6, 7, 8],
#      [9, 10, 11, 12]]
# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end='\t')
#     print()
# print()
# for row in m:
#     for x in row:
#         print(x**2, end='\t')
#     print()

# m = [[1, 2, 3, 4],
#      [5, 6, 7, 8],
#      [9, 10, 11, 12]]
#
# for row in m:
#     for x in row:
#         print(x, end='\t')
#     print()
# print()
# q =[[x**2 for x in row] for row in m]
# for row in q:
#     for x in row:
#         print(x, end='\t\t')
#     print()


# n, m = int(input('Введите высоту матрицы: ')), int(input('Введите ширину матрицы: '))
# matrix = [[0 for i in range(m)] for j in range(n)]
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()

# a = [[1, 2, 3], [3, 4, 5], [5, 6, 7], [7, 8, 9]]
# for x, y, z in a:
#     print(x, '+', y, '+', z, '=', x + y + z)

# w, h = 5, 4
# matrix = [[randint(0, 30) for i in range(w)] for j in range(h)]
#
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()

# w, h = 3, 4
# matrix = [[randint(-20, 10) for i in range(w)] for j in range(h)]
# count = 0
# for row in matrix:
#     for x in row:
#         if x < 0:
#             count += 1
#         print(x, end='\t\t')
#     print()
# print('Количество отрицательных элементов: ', count)

# w, h = 3, 4
# matrix = [[randint(0, 4) for i in range(w)] for j in range(h)]
# pro = 1
# for row in matrix:
#     for x in row:
#         if x != 0:
#             pro *= x
#         print(x, end='\t')
#     print()
# print('Произведение не нулевых элементов: ', pro)

# m = 6
# matrix = [[randint(0, 10) for i in range(m)] for j in range(m)]
# for row in matrix:
#     for x in row:
#         print(str(x).just(3), end='\t')
#     print()
#
# print()
# for row in range(len(matrix)):
#     if row % 2 == 0:
#         for x in range(len(matrix[row])):
#             print(str(matrix[row+1][x]).just(3), end='\t')
#         print()
#         for x in range(len(matrix[row])):
#             print(str(matrix[row][x]).just(3), end='\t')
#         print()

# import math

# print(dir(math))
# num1 = math.sqrt(2)
# print(num1)
# num2 = math.ceil(3.2)
# print(num2)
# num3 = math.floor(3.8)
# print(num3)
# print(math.pi)
# radius = 2
# print('Площадь окружность с радиусом', radius, '=>', math.pi * radius**2)

# radius = int(input('Введите радиус окружности: '))
# print(round((2 * math.pi * radius), 2))

import time

# second = time.time()
# local_time = time.ctime(16644712000)
# print('Секунды с начала эпохи: ', second)
# print(local_time)
# res = time.localtime(second)
# print(res)
# print(res.tm_year)
# print(time.strftime('Today is %B, %d, %Y'))
# print(time.strftime('%m/%d/%Y, %H:%M:%S', time.localtime(799979748)))

# pause = 5
# print('Program started...')
# time.sleep(pause)
# print(pause, 'seconds.')

# test = input('Название напоминания: ')
# local_time = float(input('Через сколько минут: '))
# local_time *= 60
# time.sleep(local_time)
# print(test)

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)


# import locale
# locale.setlocale(locale.LC_ALL, 'ru')
# print(time.strftime('Сегодня: %B, %d, %Y'))


