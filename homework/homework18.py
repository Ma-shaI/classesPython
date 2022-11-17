# Task 1
# def get_str(s):
#     return s[s.find('(')+1: s.find(')')]
#
#
# test = 'Дана ст(рока символов, среди которых есть одна открыв)ающаяся'
# print(get_str(test))

# Task 2 variant 1

# s = input('Строка: ')
# old = input('Ее заменяемая подстрока: ')
# new = input('Новая подстрока: ')
#
# print(s.replace(old, new))

# Task 2 variant 2

# s = input('Строка: ')
# old = input('Ее заменяемая подстрока: ')
# new = input('Новая подстрока: ')
#
# while s.find(old) != -1:
#     m = s.find(old)
#     s = s[:m] + new + s[m + len(old):]
#
# print(s)

# Task 3

# text = """Ежевику для ежат
# Принесли два ежа.
# Ежевику еле-еле
# Ежата возле ели съели.
# """
# print(text)
# print(text.count('Е')+ text.count(' е'))
