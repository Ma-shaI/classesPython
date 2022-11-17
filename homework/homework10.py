# Task 1
# from random import *
#
#
# def get_count(numbers):
#     count = 0
#     for i in numbers:
#         if i > 0 and i % 13 == 0 and i > count:
#             count = i
#     return count if count > 0 else 'no such numbers'
#
#
# print('Примеры из задания:')
# print(get_count([2, 7, 0, 3, 1, 5]))
# print(get_count([2, 7, 0, 3, 1, 5, -13, 13]))
# print(get_count([26]))
# print(get_count([99, 99, 100, 34, -39]))
# print(get_count([99, 39, 99, 100, 34]))
# print('Рандомный список:')
# random_list = [randint(-1000, 1001) for _ in range(randint(1, 100))]
# print(random_list)
# print(get_count(random_list))
# print('Проверим ваш список! Введите число по одному, если хотите остановиться: введите 0')
# lst = []
# while True:
#     n = int(input('->'))
#     lst.append(n)
#     if n == 0:
#         break
# print('Ваш список:', lst)
# print('Наибольшее положительное число, кратное 13 из вашего списка:', end=' ')
# print(get_count(lst))


# Taks 2
# def get_elem(t, elem):
#     if elem in t:
#         return 'Yes'
#     else:
#         return 'No'
#
#
# tpl = ('ab', 'abcd', 'cde', 'abc', 'def')
# s = ('ab')
# print(get_elem(tpl, s))


# Task 3 с теми знаниями которые у нас есть

# def get_counts(tpl):
#     lst = []
#     for t in tpl:
#         if t not in lst:
#             lst.append(t)
#     return [('Количество', s, '=', tpl.count(s)) for s in lst]
#
#
# m = input('Введите по порядку, без пробелов, элементы кортежа: ')
# res = get_counts(tuple(m))
# for i in res:
#     for j in i:
#         print(j, end=' ')
#     print()


# Task 3 другой вариант


# def get_counts(tpl):
#     dct = {}
#     for i in tpl:
#         if i not in dct:
#             dct[i] = tpl.count(i)
#     return dct
#
#
# m = input('Введите по порядку, без пробелов, элементы кортежа: ')
# res = get_counts(tuple(m))
# for i in res.items():
#     print('Количество', i[0], '=', i[1], end='\n')





