# day = int(input('Введите день недели (цифрой): '))
# if 1 <= day <= 5:
#     print('Рабочий день - ', end='')
#     if day == 1:
#         print('понедельник')
#     elif day == 2:
#         print('вторник')
#     elif day == 3:
#         print('среда')
#     elif day == 4:
#         print('четверг')
#     else:
#         print('пятница')
# elif day == 6 or day == 7:
#     print('Выходной день - ', end='')
#     if day == 6:
#         print('суббота')
#     else:
#         print('воскресенье')
# else:
#     print('Такого дня недели не существует!')


# num = int(input('Введите количество ворон: '))
# if 0 <= num <= 9:
#     print('На ветке ', end='')
#     if num == 1:
#         print(num, 'ворона')
#     elif 2 <= num <= 4:
#         print(num, 'вороны')
#     else:
#         print(num, 'ворон')
# else:
#     print('Ошибка ввода данных')


# Тернарное выражение
# a, b = 10, 20
# minim =a if a < b else b
# print(minim)


# a, b = 10, 10
# print('a == b' if a == b else 'a > b' if a > b else 'b > a')

# num = int(input('Введите делимое: '))
# num2 = int(input('Введите делитель: '))
# print(num / num2 if num2 != 0 else 'На ноль делить нельзя')

# Исключения
# a = 0
# b = '2'
# print(a + int(b))

# try:
#     n = int(input('Введите целое число: '))
#     print(n * 2)
# except ValueError:
#     print('Что-то пошло не так')
#
# print("Код далее")

# try:
#     n = int(input('Введите делимое: '))
#     m = int(input('Введите делитель: '))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print('Нельзя вводить строки')
#     print('Нельзя делить на ноль')
# else:  # выполняется при корректных значениях, когда в блоке try не возникло исключений
#     print('Все нормально. Вы ввели числа', n, 'и', m)
# finally:  # выполняется в любом случае
#     print('Конец программы')


# n = (input('Введите первое число: '))
# m = (input('Введите второе число: '))
# try:
#     print(int(n) + int(m))
# except ValueError:
#     print(str(n) + str(m))


# i = 0
# while i < 5:
#     print('i =', i)  # 0,1,2,3,4
#     i += 1

# i = 10
# while i > 0:
#     i -= 1
#     print('i =', i)  # 1,2,3,4,5

# i = 1
# while i < 21:
#     if i % 2 == 0:
#         print('i =', i)

#     i += 1

# n = int(input('Введите количество символов: '))
# i = 0
# while i < n:
#     print('*', end='')
#     i += 1

# n = int(input('Введите количество символов: '))
# i = 0
# while n > 0:
#     print('*', end='')
#     n -= 1

# n = int(input('Введите количество символов: '))
# print('\n'.join('*'*n))

