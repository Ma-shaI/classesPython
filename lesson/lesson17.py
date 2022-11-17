# Регулярные выражения

import re


# s = 'Я ищу совпадения в 2023 году. И я их_ найду в 20000000 счёта. 9578 19_45'
# reg = r'[12][09][0-9][0-9]'
# reg = r'[А-яё.]'
# reg = r'\A\w\s\w'
# reg = r'\bсов'
# reg = r'2[02]*'
# reg = r'^\w+\s\w+'  # работает от начала
# reg = r'\w+\s\w+$'  # работает с конца
# Повторения
# + - от 1 ддо бесконечности
# * - от 0 до бесконечности
# ? - 0 или 1

# print(s.find(reg))
# print(re.findall(reg, s))  # возвращает список, содержащий все совпадения
# print(re.findall('12', s))

# print(re.search(reg, s))  # месторасположение первого совпадения объекта
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())

# print(re.match(reg, s))  # поиск по заданному шаблону в начале строки

# print(re.split(reg, s))  # возвращает список, в котором строка разбита по шаблонам

# print(re.sub(reg, '!', s, 1))  # поиск и замена
# s1 = 'Ели[-ели].'
#
# pattern = r'[А-яё.\]\[]'
# print(re.findall(pattern, s1))

# print(re.findall(reg, s))

# text = "Час в 24-часовом формате от 00 до 23. 2021-06-15T21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09"
# reg = '[0-2][0-9]:[0-5][0-9]'
# print(re.findall(reg, text))
# s1 = "Цифры: 7, +17, -42, 0013, 0.35553"
# pattern = r'\S*\d+'
# pattern = r'[+-]?\d+[.\d]*'
# pattern = r'[+-]?\d\.?\d*'
# print(re.findall(pattern, s1))

# s1 = '05-03-1987 # Дата рождения'
# print('Дата рождения:', re.sub(r'#.*', '', s1))
# print('Дата рождения:', re.sub(r'-', '.', re.sub(r'#.*', '', s1)))

# s1 = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year=1831"
# pattern = r'\w+\s*=\s*[^;]+'
# print(re.findall(pattern, s1))
# # print(re.search(pattern, s1))

# s1 = '12  сентября 2021 года'
# reg = r'\d{2,4}'
# print(re.findall(reg, s1))

# test = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578'
# print(re.findall(r'\+?7\d{10}', test))

# def login(a):
#     return re.findall(r'[\w!@$#-]{8,25}$', a)
#
#
# print(login('admin_admin'))
# print(login('*admin!_admin&&'))

# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й', flags=re.ASCII))  # re.A
# print(re.findall(r'[а-я]', 'Я я', flags=re.IGNORECASE))  # re.I
# text = """
# one
# two
# """
# print(re.findall(r'one$', text, flags=re.MULTILINE))  # re.M
# print(re.findall(r'one.\w+', text, re.DOTALL))  # re.S
# print(re.findall("""
# [A-z.-]+   # part 1
# @          # поиск символа @
# [a-z_.-]+  # part 2
# """, 'test@mail.ru', flags=re.VERBOSE))  # re.X
# print(re.findall(r'\w\+', 'Я я', flags=re.DEBUG))
# text = """Python, python, PYTHON"""
# reg = '(?mi)^python'
# print(re.findall(reg, text))  # flags=re.IGNORECASE | re.MULTILINE

# test = '123456@i.ru, 123_456@ru.name.ru, Llogin@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru.'
# reg = r'[.\w-]+@[.\w]+[\w]{2,3}'
# print(re.findall(reg, test))

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall("<.+?>", text))

# *?, +?, ??
# {m,n}?, {,n}?, {m,}?

#
# t = "2324 786 22 4569"
# reg = r'\d{1,3}?'
# print(re.findall(reg, t))

# s = "<p>Изображение <img  alt='картинка' src='bg.jpg' title='подсказка'> - фон страницы</p>"
# # reg = r'<img[^>]*>'
# reg = r'<img\s+[^>]*src\s*=\s*[^>]+>'
# print(re.findall(reg, s))

# s = "Python (в русском языке встречаются названия питон[16] или пайтон[17]) - высокоуровненый язык программирования
# " \ "общего назначения с динамической строгой типизацией и автоматическим управлением памятью[18][19]."
# reg = r'\[
# \d+?\]' print(re.findall(reg, s))


# s = 'Петр и Ольга отлично учатся!'
# reg = 'Петр|Виталий|Ольга'
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0, double = 8.0f"
# # reg = r'int\s*=\s*\d[.\w+]*|double\s*=\s*\d[.\w+]*'
# reg = r'(?:int|double)\s*=\s*\d[.\w+]*'
# print(re.findall(reg, s))


# () - группирующая скобка
# (?:) - группирующая скобка, не сохраняющая

# s = '127.0.0.1'
# reg = r'(?:\d{1,3}.){3}\d{1,3}'
# print(re.findall(reg, s))

# s = "Word2016, PS6, AI5"
# reg = r'(([A-z]+)(\d*))'
# print(re.findall(reg, s))

# s = "5 + 7*2 -4"
# reg = r'\s*[+*-]\s*'  # ['5', '7', '2', '4']
# reg = r'\s*([+*-])\s*'  # ['5', '+', '7', '*', '2', '-', '4']
# reg = r'[^+*-]'
# print(re.split(reg, s))


# s = 'Я ищу совпадения в 2023 году. И я их_ найду в 2 счёта.'
# reg = r'([0-9]+)\s(\D+)'
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print(m[1])
# print(m[2])
# print(m[0])
