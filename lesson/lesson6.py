# def hello(name, word):
#     print('Hello,', name, 'Say', word)
#
#
# hello('Irina', 'hi')
# hello('Ivan', 'hello')


# def get_sum(a, b):
#     print(a + b)
#
#
# z = 2
# y = 5
# get_sum(z, y)
# n = 3
# m = 5
# get_sum(n, m)
# get_sum('abc', 'def')


# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2:
#             print(a, end='')
#         else:
#             print(b, end='')
#
#
# symbol(9, '+', '-')
# print()
# symbol(7, 'X', 'O')
# print()
# c = int(input('Введите количество символов: '))
# x = input('1 символ: ')
# y = input('2 символ: ')
# symbol(c, x, y)


# def get_sum(a, b):
#     return a + b
#
#
# z = 2
# y = 5
# res = get_sum(z, y)
# print(res)


# def maximum(one, two):
#     if one > two:
#         return  one
#     else:
#         return two
#
#
# print(maximum(9, 6))

# def result(one, two):
#     if one > two:
#         return one - two
#     else:
#         return one + two
#
#
# a, b = int(input("Введите первое число: ")), int(input("Введите второе число: "))
# print(result(a, b))


# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     n = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, n)
#
#     return lst
#
# print(change([1, 2, 3]))

# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
# print(is_greater(10, 5))


# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#     # has_upper = 0
#     # has_lower = 0
#     # has_num = 0
#     # for i in password:
#     #     if i.islower():
#     #         has_lower +=1
#     #     if i.isupper():
#     #         has_upper +=1
#     #     if i.isdigit():
#     #         has_num +=1
#     # if len(password) >= 8 and has_upper and has_lower and has_num:
#     #     return True
#
#     for ch in password:
#         if 'A' <= ch <= 'Z':
#             has_upper = True
#         elif 'a' <= ch <= 'z':
#             has_lower = True
#         elif '0' <= ch <= '9':
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input('Введите пароль: ')
# if check_password(p):
#     print('Надежный пароль')
# else:
#     print('Ненадежный пароль')


# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# q = 2
# print(get_sum(1, 5, d=q))


# def get_str(n=20, symbol='-'):
#     return symbol * n
#
#
# print(get_str())
# num = int(input('Введите число: '))
# sym = input('Введите символ: ')
# print(get_str(num, sym))


# def digit_sum(n, even=True):
#     s = 0
#     m = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         elif even == False and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 10
#     # for i in (str(n)):
#     #     if int(i) % 2 == 0:
#     #         s += int(i)
#     return s
#
#
# print('Сумма четных цифр:')
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
# print('Сумма нечетных цифр:')
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))


# def display_info(name, age):
#     print('Name:', name, '\nAge:', age)
#
#
# display_info('Ira', 23)
# display_info(23, 'Ira')
# display_info(age=23, name='Ira')

# s = []
# for i in (str(123456)):
#         s.append(int(i))
# print(s)

