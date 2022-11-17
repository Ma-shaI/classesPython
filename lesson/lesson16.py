# print(ord('a'))
# while True:
#     n = input('-> ')
#     if n != '-1':
#         print(ord(n))
#     else:
#         break

# string = 'Test string for me'
# lst = [ord(i) for i in string]
# print(lst)
# sa = int(sum(lst) / len(lst))
# lst.insert(0, sa)
# print('Среднее арифметическое', lst)
# lst += [x for x in [ord(x) for x in (input('-> ')).replace(' ', '')[:3]] if x not in lst]
# print(lst)
# if lst[-1] in lst[:-1]:
#     print('Количество последних элементов:', lst.count(lst[-1]) - 1)
# print(sorted(lst, reverse=True))

# print(chr(97))
# print(chr(35))
# a = 122
# b = 97
# if a > b:
#     for i in range(b, a+1):
#         print(chr(i), end=' ')
# else:
#     for i in range(a, b+1):
#         print(chr(i), end=' ')


# print('apple' == 'Apple')
# print('apple' > 'Apple')
# print(ord('a'))  # 97
# print(ord('A'))  # 65


# from random import  randint
#
# SHORTEST = 6
# LONGEST = 16
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_password():
#     random_length = randint(SHORTEST, LONGEST)
#     password = ''
#     for i in range(0, random_length):
#         password += chr(randint(MIN_ASCII, MAX_ASCII))
#     return password
#
#
# print('Ваш случайный пароль:', random_password())

# s = 'hello, WORLD! I am learning Python.'
# print(s.capitalize())
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
#
# print(s.count('l', 3))  # подсчитывает количество вхождений подстроки в строку
# print(s.find('Python1'))  # ищет в строке заданную подстроку, и возвращает
# # индекс первого вхождения, если совпадений нет то -1


# s = input('Введите два слова через пробел: ')
# b = s[:s.find(' ')]
# c = s[s.find(' ')+1:]
# print(c, b)

# s = 'ab12c59p7dq'
# lst = []
# for i in s:
#     if i in '1234567890':
#         lst.append(int(i))
# print(lst)

# digits = []
# for i in s:
#     if '1234567890'.find(i) != -1:
#         digits.append(int(i))
# print(digits)

# print(s)
# print(s.index('Python1'))  # ищет в строке заданную подстроку, если она найдена, то
# возвращает индекс первого вхождения подстроки, если нет - то возвращает исклчение ValueError
# print(s.rfind('l'))
# print(s.rindex('l'))

# a = 'I am learning Python. hello, WORLD!'
# first = a.find('h')
# last = a.rindex('h')+1
# print(a[:first] + a[last:])

# print('abc123'.isalnum())  # состоит ли строка из цифр или/и букв
# print('ABCabc'.isalpha())  # состоит ли строка только из букв
# print('1234'.isdigit())  # состоит ли строка только из цифр
# print('abc'.islower())  # определяет все ли буквы строчные
# print('ABC'.isupper())  # определяет все ли буквы заглавные
# print('   '.isspace())  # состоит ли строка только из пробелов

# print('py'.center(10, '-'))
# print(' py '.center(30, '*'))


# print('       py'.lstrip())  # удаляют пробельные символы
# print('py       '.rstrip())
# print('       py           '.strip())
# print('https://www.python.org'.lstrip('/:pths'))  # удаляет символы подряд которые есть в перечне
# print('py.$$$;'.rstrip('.$;'))
#
# print('https://www.python.org'.lstrip('/:pths').rstrip('.org'))

# st = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(st)
# print(st.replace("Nython", "Python" ))

# s = "-"
# seq = ('a', 'e', 'c')
# print(s.join(seq))
#
# print('..'.join(['1', '2']))
#
# print(':'.join('Hello'))

# print('Строка разделенная пробелами'.split())
# # print('Строка_разделенная_пробелами'.split('_'))
# # print('Строка_разделенная_пробелами'.split('а'))
# print('www.python.org'.split('.',1))

# a = list(map(int, input('->').split()))
# print(type(a[0]))

# a = input('Введите ФИО: ').split()
# print(a[0], ' ', a[1][0], '.', a[2][0], '.', sep='')
# print(f'{a[0]} {a[1][0]}. {a[2][0]}.')

# print('www.python.org.ru'.rsplit('.', 2))
# print('www...python...org'.rsplit('.'))

# a = input('Введите строку: ').split(' ')
# print('*'.join(a))

