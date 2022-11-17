# a = [letter * 2 for letter in 'Hello']
# print(a)
#
# for i in 'Hello':
#     print(i * 2)
#
# num = [i for i in range(30) if not i % 2 ]
# print(num)

# print([i for i in range(30) if i % 2 == 0])

# Списки

# num = [8, 3, 'one', 3.2, [1, 2, 3]]
# print(num)
# print(type(num))
# print(num[1])
# print(num[-1][1])
# print(num[-2])
# num[2] = 256
# print(num)
# num[1] += 100
# print(num)

# num = [8, 3, 'one', 3.2, [1, 2, 3]]
# print('Длина списка: ', len(num))

# s =[]
# print(type(s))
# b = list('Hello')
# print(b)

# s = [5, 1] * 6
# print(s)

# n = list(range(2, 10, 2))
# print(n)
# n2 = [[2, 4, 6, 8]]
# print(n2)
#
# if n == n2:
#     print('списки равны')
# else:
#     print('списки разные')

# [выражение for переменная счетчик in последовательность]

# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)

# a = [1, 2, 3]
# b = [5, 6]
# c = a + b
# print(c)
# print(a)
# d = c * 2
# print(d)

# a = [0] * int(input('Введите количество элементов списка: '))
# print(a)
# for i in range(len(a)):
#     a = int(input('Введите элемент: '))
# print(a)

# a = [int(input('-> ')) for i in range(int(input('Количество элементов: ')))]
# print(a)

# a = [4, 8, 9, 3, 2]
# for i in range(len(a)):
#     print(a[i] + 1, end=' ')
# print()
# for elem in a:
#     print(elem + 1, end=' ')

# lst = ['one', 'two', 'three']
# for elem in lst:
#     print(elem, end=' ')
# print()
# for i in range(len(lst)):
#     print(lst[i], end=' ')

# a = [int(input('-> '))for i in range(int(input('Введите количество элементов: ')))]
# summa = 0
# for i in a:
#     summa += i if i<0 else 0
# print('Сумма отрицательных элементов:', summa)

# a = [i for i in range(21, 41)]
# summa = 0
# count = 0
# for i in a:
#     summa += i if i%2 else 0
#     count += 1 if not i%2 else 0
#
# print('Количество четных элементов списка: ', count)
# print('Сумма нечетных элементов: ', summa)

# a = [int(input('-> '))for i in range(int(input('Введите количество элементов: ')))]
# count = 0
# summa = 0
# for i in a:
#     summa += i
#     count += 1 if i != 0 else 0
# print('Среднее арифметическое: ', summa/count)

# a = [int(input('-> ')) for i in range(int(input('Введите количество элементов: ')))]
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end=' ')

# a = [7, 8, 2, 1, 17]
# print(a)
# a[0], a[-1] = a[-1], a[0]
# print(a)

# a = [int(input('-> ')) for i in range(int(input('Введите количество элементов: ')))]
# for i in range(1, len(a) - 1):
#     if a[i] > a[i + 1]:
#         print(a[i], end=' ')

# Срезы

# список[start:stop:step]
# s = [5, 9, 3, 7, 1, 8]
# print(s[1:4])
# print(s[2:])
# print(s[:2])
# print(s[::2])
# print(s[1::2])
# print(s[::-1])
# print(s[-2:2:-1])
# print(s[1:4:-1])
# print(s[10:20])

# s = [i for i in range(1, 8)]
# print(s[:])
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[:1])
# print(s[-1:])
# print(s[3:4])
# print(s[4:])
# print(s[-3:1:-1])
# print(s[2:5])
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# s[3] = 30
# print(s)

# Методы списков

# s = [1, 20, 0, 30, 4, 5, 6, 7]
# print(s)
# s.append(99)  # добавляет элемент в конец списка
# print(s)
# s.extend([9, 8, 3])  # добавляет множество элементов в конец списка
# print(s)
# s.extend('ass')
# print(s)
#
# # s = []
# # for i in range(1, 11):
# #     s.extend([i**2])
# # print(s)
# s.insert(1, 100)  # добавляет заданное значение (второй параметр) по указанному индексу (первое значение)
# print(s)
#
# lst = []
# n = int(input('Введите количество элементов: '))
# for num in range(n):
#     x = int(input('Введите число: '))
#     # lst.append(x)
#     # lst.extend([x])
#     lst.insert(-1, x )  # при добавлении в конец списка - работает не так как надо (2,3,1)
#
# print(lst)

# n = int(input('Введите количество элементов списка: '))
# i = 0
# lst = []
# while i < n:
#     x = int(input('Ввведите число кратное 3: '))
#     if x % 3 != 0:
#         print(x, 'число не делится на 3 без остатка')
#     else:
#         lst.append(x)
#     i += 1
# print(lst)

# lst = []
# n = int(input("Введите количество элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         lst.append(x)
#     else:
#         print("Не делится")
#     num += 1
# print(lst)

# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 3, 7]
# c = []
#
# for i in a:
#     for j in b:
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3, 55, 6, 7,522 ]
# b = [11, 22, 33, 44, 4, 5]
# c = []
# for i in range(len(a)):
#     for j in range(len(b)):
#         if i == j:
#             c.append(a[i])
#             c.append(b[j])
# print(c)
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(b[i])
#         c.append(a[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)

# s = [1, 10, 0, 30, 4, 5, 6, 7]
# s[4:] =[]
# s[2:4] = []
# if 2 in s:
#     s.remove()  # удаляет элемент по значение, первое совпадение
# print(s)
# last = s.pop()  # удаляет последний элемент из списка и возвращает удаленный элемент
# print(last)
# print(s)
# second = s.pop(0) # удаляет элемент по индексу и возвращает удаленный элемент
# print(s)
# # s.clear()  # ощичает полностью список
# del s[:]  # удаляет элемент по индексу, работает с разными списками данных
# print(s)


# s = []
# m = [int(input('-> ')) for i in range(int(input('Введите количество элементов: ')))]
# k = int(input('Введите индекс: '))
# print(m)
# del m[k]  # s.pop(k)
# print(m)

# s = [1, 20, 0, 30, 4, 0, 5, 6, 7, 0, 2]
# num = s.count(0)  # Считает количество заданных значений в списке
# print(num)
# ind = s.index(0, 3)  # Возвращает положение(индекс) первого индекса с заданным значением
# print(ind)

# a = [1, 2, 3]
# b = a
# s_copy = a.copy()  # возвращает копию списка, расположенную по другому адресу
# print('a =',a)
# print('b =', b)
# a.append(20)
# b.append(4)
# s_copy.append(444)
# print('a =',a)
# print('b =', b)
# print('s_copy =', s_copy)
# print(id(a))
# print(id(b))
# print(id(s_copy))

s = [1, 20, 0, 30, 4, 0, 5, 6, 7, 0, 2]
# s.reverse()  # возвращает None, переставляет элементы списка в обратном порядке
# print(s)
#
# s.sort(reverse=True)  # возвращает None, переставляет элементы списка отсортированным
# print(s)
#
# s2 =['Виталий', "Сергей", "Александр", "Анна"]
# s2.sort(key=len)
# print(s2)

# srt = sorted(s)
# print(srt)
# print(s)

