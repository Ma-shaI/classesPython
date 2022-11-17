# Task 1
# num = int(input('Введите пятизначное число: '))
# a = num % 10
# num //= 10
# b = num % 10
# num //= 10
# c = num % 10
# num //= 10
# d = num % 10
# num //= 10
# e = num
# pro = a * b * c * d * e
# se = (a + b + c + d + e) / 5
# print('Произведение цифр числа ', num, ': ', pro, sep='')
# print('Среднее арифметическое:', se)


# Task 2
# num1 = int(input('Введите целое число: '))
# if num1 % 2 == 0:
#     print('Число', num1, '- четное')
# else:
#     print('Число', num1, '- нечетное')


# Task 3
# print('Выберите операцию: ')
# print('1 - "r" - применяет унарный минус к операнду')
# print('2 - "+" - сложение')
# print('3 - "-" - вычитание')
# print('4 - "/" - деление')
# print('5 - "*" - умножение')
# print('6 - "%" - деление по модулю (остаток от деления)')
# print('7 - "<" - минимальное из двух чисел')
# print('8 - ">" - максимальное число из двух чисел')
#
# num = int(input('Введите цифру: '))
# if num == 1:
#     a = int(input('Введите число: '))
#     print('Результат:', a * (-1))
# else:
#     a = int(input('Введите первое число: '))
#     b = int(input('Введите второе число: '))
#     if num == 2:
#         print('Результат', a + b)
#     elif num == 3:
#         print('Результат', a - b)
#     elif num == 4:
#         if b == 0:
#             print('На 0 делить нельзя')
#         else:
#             print('Результат', a / b)
#     elif num == 5:
#         print('Результат', a * b)
#     elif num == 6:
#         if b == 0:
#             print('На 0 делить нельзя')
#         else:
#             print('Результат', a % b)
#     elif num == 7:
#         if a < b:
#             print('Результат', a)
#         else:
#             print('Результат', b)
#     elif num == 8:
#         if a > b:
#             print('Результат', a)
#         else:
#             print('Результат', b)


# Task 4
num2 = int(input('Введите число от 1 до 99: '))
if 1 <= num2 <= 99:
    if num2 % 10 == 1 and num2 // 10 != 1:
        print(num2, 'копейка')
    elif (num2 % 10 == 2 or num2 % 10 == 3 or num2 % 10 == 4) and num2 // 10 != 1:
        print(num2, 'копейки')
    else:
        print(num2, 'копеек')
else:
    print('Некорректный ввод данных')
