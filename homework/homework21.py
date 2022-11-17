import re


# Task 1
# def check_date(d):
#     reg = r'([0-2][0-9]|3[]01)\-(0[0-9]|1[0-2])\-(20[0-9][0-9]|19[0-9][0-9])'
#     s = re.findall(reg, d)
#     if len(s[0]) == 3:
#         return s
#     else:
#         return "Я такой даты не знаю"
#
#
# test = '32-19-1921'
# print(check_date(test))
# your_date = input('Введите дату в формате dd-mm-YYYY: ')
# print(check_date(test))


# Task 2

# def check_number(num):
#     reg = r'^\+?7\s?\-?\(?\d{3}\)?\s?\-?\d{3}\s?\-?\d{2}\s?-?\d{2}'
#     s = re.findall(reg, num)
#     if len(s[0]) == len(num):
#         return s
#     else:
#         return "Номер введен неверно"
#
#
# test = "+7(499) 456 45-78"
# print(check_number(test))
# your_number = input('Введите ваш номер: ')
# print(check_number(your_number))
