# n = input('Введите целое число: ')
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print('Число не целое')
#         n = input('Введите целое число')
# if n % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')


# i = 0
# while i < 10:  # True
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=' ')
#     if i == 5:
#         break
#     i += 1
# print('\nЦикл завершен')


# while True:
#     n = int(input('Введите положительное целое число: '))
#     if n > 0:
#         break
#
#
# n = int(input('Введите любое число: '))
# count = 1
# while n != 0:
#     count *= n
#     n = int(input('Введите любое число: '))
# print('Произведение чисел:', count)

# count = 1
# while True:
#     n = int(input('Введите любое число: '))
#     if n == 0:
#         break
#     count *= n
# print('Произведение чисел:', count)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print('Цикл окончен, i =', i)

# i = 1
# while i < 5:
#     print('Внешний цикл: i =', i)
#     j = 1
#     while j <4:
#         print('\tВложенный цикл: j =', j)
#         j += 1
#     i += 1


# i = 1
# while i<10:
#     j = 1
#     while j<10:
#         print(i, '*', j, '=', i*j, end='\t\t')
#         j += 1
#     print()
#     i += 1

# n = int(input('Укажите количество символов: '))
# i = 0
# while i <n:
#     print('*', end ='')
#     i += 1

# i =0
# while i<3:
#     j = 0
#     while j<6:
#         print('^', end='')
#         j +=1
#     print()
#     i+=1

# i = 1
# while i <= 5:
#     j=0
#     while j<20:
#         if i%2!=0:
#             print('+', end='')
#         else:
#             print('-', end='')
#         j+=1
#     print()
#     i+=1


# for element in collection:
#       print(element)

# for i in 'Hello!':
#     print(i)

# i = 1
# for color in 'red', 'orange', 'yellow':
#     print(i, 'color:', color)
#     i += 1


# for i in range(n):
#    Тело цикла

# range(start, stop, step)

# for i in range(2, 9, 3):
#     print(i, end=' ')
# print()
# j = 2
# while j < 9:
#     print(j, end=' ')
#     j += 3

# for i in range(100, 0, -10):
#     print(i, end=' ')
# j = 100
# print()
# while j > 0:
#     print(j, end=' ')
#     j -= 10


# n = int(input('Введите целое число: '))
# for i in range(1, n):
#     if n % i == 0:
#         print(i, end=' ')


# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=' ')

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print('done')

# for i in range(3):
#     print('+++')
#     for j in range(2):
#         print('-----')


# n = int(input("Введите длину прямоугольника: "))
# m = int(input("Введите высота прямоугольника: "))
# # for i in range(m):
# #     for j in range(n):
# #
# #         print('*', end='')
# #     print()
#
# for i in range(m):
#     print('*'*n)

# n = int(input("Введите длину прямоугольника"))
# m = int(input("Введите высота прямоугольника"))
# for i in range(m):
#     if i == 0 or i == m -1:
#         print('*'*n, end='\n')
#     else:
#         print('*', ' '*(n-4), '*')

# a = int(input("высота прямоугольника"))
# b = int(input("Ширина прямоугольника"))
# for i in range(a):
#     print()
#     for j in range(b):
#         if 0 < i < a - 1 \
#                 and 0 < j < b - 1:
#             print(" ", end="")
#         else:
#             print(i, end="")


n = int(input("Введите длину прямоугольника"))
m = int(input("Введите высота прямоугольника"))
for i in range(m):
    for j in range(n):
        if i == 0 or j == 0 or i == m - 1 or j == n - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
