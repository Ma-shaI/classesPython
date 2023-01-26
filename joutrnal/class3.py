# a, b = int(input('-> ')), int(input('-> '))
import math
import random

# for i in range(a, b+1):
#     print(i)

# a, b = int(input('-> ')), int(input('-> '))
# for i in range(a, b + 1):
#     print(i) if i % 2 else ''

# a, b = int(input('-> ')), int(input('-> '))
# if a > b:
#     for i in range(a, b-1, -1):
#         print(i)
# else:
#     for i in range(b, a-1, -1):
#         print(i)

# a, b = int(input('-> ')), int(input('-> '))
# summa = 0
# count =0
# for i in range(a, b+1):
#     summa += i
#     count += 1
# print(summa)
# print(summa/count)

# a = int(input('-> '))
# print(math.factorial(a))

# a = int(input('-> '))
# print('*' * a)
#
# a, b = int(input('-> ')), input()
# print(b * a)

# a = int(input('-> '))
# for i in range(1, 10):
#     print(f'{a} * {i} = {a*i}')

# a, b = int(input('-> ')), int(input('-> '))
# lst = [i for i in range(a, b+1)]
# m = True
# while m:
#     c = int(input('-> '))
#     if c in lst:
#         for i in lst:
#             if c == i:
#                 print(f'!{c}!', end=' ')
#             else:
#                 print(i, end=' ')
#         m = False


# m = random.randint(1, 500)
# s = True
# count = 0
#
# while s:
#     a = int(input('-> '))
#     if a == m:
#         print(f'Win: {count}')
#         s = False
#     elif a == 0:
#         print('Game over')
#     elif a < m:
#         count += 1
#         print('Число больше загаданного')
#     else:
#         count += 1
#         print('Число меньше загаданного')

# a = int(input('-> '))
# for i in range(a):
#     print('*' * a)

# a, b = int(input('-> ')), int(input('-> '))
# for i in range(a):
#     print('*' * b)

# a = int(input('-> '))
# print(a * '*')
# for i in range(a - 2):
#     print('*', ' ' * (a-4), '*')
#
# print(a * '*')

# a, b = int(input('-> ')), int(input('-> '))
# print('*' * b)
# for i in range(a-2):
#     print('*', ' '*(a), '*')
# print(b*'*')

# a = int(input())
# summa = 0
# c = 0
# for i in str(a):
#     summa += int(i)
#     if i == 0:
#         c += 1
#
# print(len(str(a)), summa, int(summa / len(str(a))), c)


# print('level 1')
# count = 0
# for i in range(3):
#     a = random.randint(1, 5)
#     b = random.randint(1, 5)
#     print(a, b)
#     o = int(input('->'))
#     if o == a * b:
#         count += 1
# print(f'level 1: {count}')
# count = 0
# print('level 2')
# for i in range(5):
#     a = random.randint(3, 10)
#     b = random.randint(3, 10)
#     print(a, b)
#     o = int(input('->'))
#     if o == a * b:
#         count += 1
# print(f'level 2: {count}')

# for i in range(6):
#     print(' ' * (6 - i - 1) + '*' * (2 * i + 1) )
#
# for i in range(4, 0, -1):
#     print(' ' * (6 - i - 1) + '*' * (2 * i + 1))