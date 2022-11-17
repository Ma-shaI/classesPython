# Вложенные функции

# def outer_func(who):
#     def inner_func():
#         print("Hello,", who)
#     inner_func()
#
#
# outer_func(" world")

# def func1():
#     a = 6
#
#     def func2(b):
#         a = 4
#         print('Сумма: ', a + b)
#
#     print('a:', a)
#     func2(4)
#
#
# func1()

# x = 25
#
#
# def fn():
#     global t
#     a = 30
#
#     print('global:', x)  # 25
#
#     def inner():
#         nonlocal a
#         a = 35
#         print('nonlocal:', a)  # 35
#
#     inner()
#     print(a)  # 35
#     t = a
#
#
# fn()
# z = x + t  # 25 + 30
# print(z)

# def fn1():
#     x = 25
#
#     def fn2():
#         #  x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print('fn2.x =', x)
#
#     fn2()
#     print('fn1.x =', x)
#
#
# fn1()


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#
#     inner()
#     return [a, b]
#
#
# res = outer(2, 3, -1, 4)
# print(res)


# def increment(number):
#     def inner():
#         return number + 1
#
#     return inner()
#
#
# print(increment(10))


# Замыкания

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# res = outer(5)
# print(res(10))
#
# print(outer(5)(10))
#
# res2 = outer(7)
# print(res2(5))

# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a +1
#         b = b + '_new'
#         return a, b, c
#
#     return func2

#
# func = func1()
# print(func())


# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res1 = func('Москва')
# res1()
# res1()
#
# res2 = func('Сочи')
# res2()
# res2()
# res2()

# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Elise': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
#
# def make_classifier(lower, upper):
#     def classify_student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return classify_student
#
#
# A = make_classifier(80, 100)
# B = make_classifier(70, 80)
# C = make_classifier(50, 70)
# D = make_classifier(0, 50)
# print(A(students))
# print(B(students))
# print(C(students))
# print(D(students))


def func(a, b):
    def add():
        return a + b

    def sub():
        return a - b

    def mul():
        return a * b

    def replace():
        pass

    replace.add = add
    replace.sub = sub
    replace.mul = mul
    return replace


obj1 = func(5, 2)
print(obj1.add())

obj2 = func(5, 2)
print(obj2.sub())

obj3 = func(5, 2)
print(obj3.mul())
