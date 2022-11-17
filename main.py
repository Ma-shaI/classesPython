# name = "Maria"
# age = 27
# print('Hello,', name)
# print(age)
# print(type(name))
# print(type(age))
# a = 4
# b = 5
# a = b
# print(id(a))  # id
# print(id(b))
# a = b = c = 1
# print(a, b, c)
# a, b, c = 5, "Hello", 9.2
# print(a, b, c)

# name = "Bob"
# print(name)

# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# a = 'Hello'
# print(type(a))
# a = 3
# print(type(a))

# name = "Maria"
# age = 27
# print("My name is " + name + ". Мне " + str(age) + "age")
# print("My name is ", name, ". Мне ",age, "age")

# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
# a, b = b, a
# c = a
# a = b
# b = c

# a = a + b
# b = a - b
# a = a - b
# print("a:", a)
# print("b:", b)

# print("строка \
# символов")
# print('строка '
#       'символов')
# print('''Document "script.py"''')
# print("Document \"script.py\" находится \rпо заданному пути \n\tD:\\\Python\project")

# s1 = "hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!\t\t"
# print(s3*2)
# print("*" * 40)

# print(-456685653128313136646975533212355888)
# print(2.456685653128313136646975533212355888)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 / 2)  # всегда вещественное число 3.0
# print(7 / 2)  # 3.5
# print(6 // 2)  # 3
# print(7 // 2)  # 3
# print(7 % 2)  # 1
# print(7 ** 2)  # 49

# num = 10
# num += 5
# print(num)

# nums = 4321
# a = nums%10
# print(a)
# nums //=10
# b = nums%10
# print(b)
# nums //=10
# c = nums%10
# print(c)
# nums //=10
# d = nums%10
# print(d)
# print(a*1000+b*100+c*10+d)

# num = 4321
# res = (num % 10) * 1000
# num = num // 10
# res += (num % 10) * 100
# num = num // 10
# res += (num % 10) * 10
# num = num // 10
# res += (num % 10)
# print(res)

# num1 = "2"
# num2 = 3
# res = int(num1) + num2
# print(res)

# print(int(3.8))
# print(round(3.8255, 2))

# a = 5 / 2
# print(round(a, 2))

# a = '5.2'
# b = 10
# c = float(a) + b
# print(c)

# a = 1
# b = 2
# print('a:', a, '\nb:', b)

# name = 'Victor'
# age = 28
# print('My name is', name, ". I am ", age, 'age')
# print('My name is ' + name + ". I am " + str(age) + 'age')
# print('My name is ', name, ". I am ", age, ' age', sep="", end='!!!')
# print("Я учу Python", end="\n\n")
# print('qqq')
# print(5+2, 3+4, sep='+')

# print('*** Ваши данные ***')
# name = input('Введите ваше имя: ')
# city = input('Введите ваш город: ')
# print(name, city)

# num = int(input('Введите число: '))
# st = int(input('Введите степень: '))
# print('Число', num, 'в степени', st, 'равно:', num**st)


# print('Введите четыре числа:')
# a = int(input('1: '))
# b = int(input('2: '))
# c = int(input('3: '))
# d = int(input('4: '))
# print('Результат:', round(((a+b)/(c+d)),2))

# print(bool('python'))  # True
# print(bool(""))  # False
# print(bool(' '))  # True
# print(bool(0))  # False
# print(bool(4))  # True
# print(bool(0.0))  # False
# print((bool(0.5)))  # True
# print(bool(False))  # False
# print(bool(None))  # False

# test = None
# print(test)
# test = 5
# print(test)

# print(7 == 7)
# print(2 + 5 != 7)
# print(8 > 7)
# print(8 <= 8)
# print('привет' <= 'Привет')

# print(2 < 4 < 9)
# print(2 * 5 > 7 >= 4 + 3)
# print(9 * 3 <= 7 >= 2)

# a = 10
# b = 5
# c = a ==b
# print(a, b,c)

# print(5 - 3 == 2 and 1 + 3 ==4)  # True (True : True)
# print(5 - 3 == 2 and 1 + 3 < 4)  # False (True : False)
# print(5 - 3 > 2 and 1 + 3 == 4)  # False (False : True)
# print(5 - 3 > 2 and 1 + 3 < 4)  # False (False : False)

# print(5 - 3 == 2 or 1 + 3 == 4)  # True (True : True)
# print(5 - 3 == 2 or 1 + 3 < 4)  # True (True : False)
# print(5 - 3 > 2 or 1 + 3 == 4)  # True (False : True)
# print(5 - 3 > 2 or 1 + 3 < 4)  # False (False : False)

# print(not 9 - 7)
# print(not 7 - 7)

# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input('Введите свой возраст: '))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print('Доступ на сайт запрещен!!!')

# a = 5
# b = 15
# if a > b:
#     print("a > b")
# elif a < b:
#     print("b > a")5
# else:
#     print("b == a")

# a = int(input("Введите первую сторону: "))
# b = int(input("Введите вторую сторону: "))
# c = int(input("Введите третью сторону: "))
#
# if a == b == c:
#     print('Треугольник равносторонний')
# elif a == b or b == c or c == a:
#     print('Треугольник равнобедренный')
# else:
#     print('Треугольник разносторонний')

num = int(input('Введите номер месяца: '))
if num > 0 and num < 13:
    if 1 <= num <= 2 or num == 12:
        print('Зима')
    elif 3 <= num <= 5:
        print('Весна')
    elif 6 <= num <= 8:
        print('Лето')
    else:
        print('Осень')
else:
    print('Введите корректное число')

# int()- преобразовывает к целочисленному типу данных
# float()- преобразовывает к вещественному типу данных
# str() -преобразовывает к строковому типу данных
# bool() - преобразование к булевом типу данных
# False = 0, '', None, False
