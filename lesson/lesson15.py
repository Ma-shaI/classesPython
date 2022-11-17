# print(int('100',2))
# print(int('100', 8))
# print(int('100', 16))
# print(int('100', 10))

# print(bin(18))  # 0b10010  #0B
# print(oct(18))  # 0o22  # 0O
# print(hex(18))  # 0x12  # 0X

# print(0B100 + 2)
# print(0o20)
# print(0x11)


# q = 'Pyt'
# w = 'hon'
# e = q + w
# print(e)
# print(e * 3)
# print('e' in e)
# print(e[1])
# e = e[:3] + 't' + e[4:]
# print(e)

# def change_char(s, c_old, c_new):
#     stroke = ''
#     for i in s:
#         if i == c_old:
#             stroka += c_new
#         else:
#             stroke += i
#     return stroke
#
#
# st = 'Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования'
# st2 = change_char(st, 'N', 'P')
# print('st1 = ', st)
# print('st2 =', st2)

# print(u"Привет")
# print(r'C:\file.txt')  # сырые строки игнорируют спец-символы
# print('C:\\file.txt\\')

# name = 'Дмитрий'
# age = 25
# print('Меня зовут ' + name + ". Мне " + str(age) + " лет")
# print('Меня зовут ', name, ". Мне ", str(age), " лет", sep='')
# print(f'Меня зовут {name}. Мне {age} лет')

# print(f'{round(2.356789, 2)}')
# print(f'{2.356789:.2f}')

# x = 10
# y = 5
#
# print(f'{x} x {y} /2 = {x*y/2}'
#       f' - выражение')


# d = 74
# print(f'{{{74}}}')

# dir_name = 'doc'
# file_name = 'data.txt'
# print(fr'home\{dir_name}\{file_name}')

# s = """<div>
#     <a href='#'>content</a>
# </div>
# """
# print(s)
# s1 = '''<div>
#     <a href='#'>content</a>
# </div>'''
# print(s1)

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# print(min.__doc__)


import math


def cylinder(r, h):
    """
    Вычисляет площадь цилиндра.

    Вычисляет площадь цилиндра, на основании заданной высоты и радиуса основания.

    :param r: положительное число, радиус основания цилиндра.
    :param h: положительное число, высота цилиндра.
    :return: положительное число, площадь цилиндра
    """

    return 2 * math.pi * r * (r + h)


print(cylinder(2, 4))
